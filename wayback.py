#!/usr/bin/env python3

import argparse
import json
import os
from datetime import datetime

import progressbar
import requests
import tabulate
from colorama import Fore, Style

banner = '''
                        __               __  
 _    __ ___ _  __ __  / /  ___ _ ____  / /__
| |/|/ // _ `/ / // / / _ \/ _ `// __/ /  '_/
|__,__/ \_,_/  \_, / /_.__/\_,_/ \__/ /_/\_\ 
              /___/                          
'''

success = Style.BRIGHT + '[ ' + Fore.GREEN + '✔' + Fore.RESET + ' ] ' + Style.RESET_ALL
information = Style.BRIGHT + '[ ' + Fore.YELLOW + '✻' + Fore.RESET + ' ] ' + Style.RESET_ALL
failure = Style.BRIGHT + '[ ' + Fore.RED + '✘' + Fore.RESET + ' ] ' + Style.RESET_ALL


def args():
    usage = "Usage: python3 wayback.py -t [domain] [options]"
    description = "Command line utility for the Wayback machine. Version 1.1"
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument('--version', action='version', version='%(prog)s 1.1')
    parser.add_argument("-t", "--target", action="store", required=True,
                        dest="target", help="(required) specifies the target domain")
    parser.add_argument("-m", "--match", action="store", choices=["exact", "prefix", "host", "domain"],
                        dest="match", help="(optional) return matches for an exact url"
                                           "exact (default): return exactly matching results"
                                           "prefix: return results for all results under the path"
                                           "host: return result for the given host"
                                           "domain: return results from host and all sub-hosts")
    parser.add_argument("-f", "--filter", action="store",
                        dest="filter", help="(optional) you can specify different criteria"
                                            "'!' before the query inverts the match"
                                            "Filter for 'OK' response codes: statuscode:200"
                                            "Filter for mime type: mimetype:text/html")
    parser.add_argument("--from", action="store",
                        dest="start", help="(optional) you can specify the starting date"
                                           "date format: yyyyMMddhhmmss"
                                           "Example: --from=2015")
    parser.add_argument("--to", action="store",
                        dest="end", help="(optional) you can specify the ending date"
                                         "date format: yyyyMMddhhmmss"
                                         "Example: --to=2017")
    parser.add_argument("-l", "--limit", action="store",
                        dest="limit", help="(optional) limits the number of results -N returns the last N result")

    return parser.parse_args()


def row(data, index):
    try:
        date = datetime.strptime(data[index][1], "%Y%m%d%H%M%S").strftime("%Y.%m.%d.")
        time = datetime.strptime(data[index][1], "%Y%m%d%H%M%S").strftime("%H:%M:%S")
    except ValueError:
        # some dates can't be formatted, so I just leave them like that
        date = str(data[index][1])
        time = str(data[index][1])

    # link format = web archive url + snapshot date + target domain
    link = "https://web.archive.org/web/" + str(data[index][1]) + "/" + str(data[index][2])
    mime_type = str(data[index][3])
    status_code = str(data[index][4])
    # optional columns
    # digest = data[index][5]
    # length = str(data[index][6])

    return [date, time, link, mime_type, status_code]


def main(arguments):
    print(success + f"Target: {arguments.target}")

    parameters = {"url": arguments.target,
                  "limit": arguments.limit,
                  "match": arguments.match,
                  "filter": arguments.filter,
                  "from": arguments.start,
                  "to": arguments.end,
                  "output": "json"}

    print(information + "Downloading data, please wait...")
    response = requests.get(url="http://web.archive.org/cdx/search/cdx?", params=parameters, stream=True)
    if response.ok:
        content = ""
        for chunk in progressbar.progressbar(response.text):
            content = content + str(chunk)
        data = json.loads(content)
        print(success + "Download successfully finished!")

        print(information + "Parsing data, this may also take some time...")
        table = list()
        for index in progressbar.progressbar(range(1, len(data))):
            table.append(row(data, index))

        file_name = arguments.target + ".txt"
        print(information + f"Writing data to {file_name}...")
        output_file = open(file_name, "w")
        output_file.write(tabulate.tabulate(table, tablefmt="fancy_grid", stralign="center",
                                            headers=["Date", "Time", "Link", "Mime Type", "Status Code"]))
        output_file.close()
        print(success + f"Result successfully saved to {file_name}!")
    else:
        print(failure + "Failed to download snapshot list! Exiting...")


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    main(args())
