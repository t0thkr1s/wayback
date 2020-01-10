# wayback

[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://forthebadge.com/images/badges/built-with-love.svg)](https://gitHub.com/t0thkr1s/)

The Wayback Machine is a digital archive of the World Wide Web, founded by the Internet Archive.
This is a standalone script written in Python 3 for querying the web archive.
You can get a nice list of archive links with dates, times, status codes and mime types.
You also have the ability to specify criteria like date range and result filter.

## Download

```
git clone https://github.com/t0thkr1s/wayback
```

## Install

The script has 4 dependencies:

*   [requests](https://pypi.org/project/requests/)
*   [colorama](https://pypi.org/project/colorama/)
*   [tabulate](https://pypi.org/project/tabulate/)
*   [progressbar2](https://pypi.org/project/progressbar2/)

You can install these by typing:

```
python3 setup.py install
```

## Run

```
python3 wayback.py -t [target_domain]
```

## Screenshot

![Screenshot](https://i.imgur.com/NBYHmzX.png)

### Disclaimer

> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
