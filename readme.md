# Sahibinden

This is a Python library to extract prices from [sahibinden.com](http://www.sahibinden.com). It is heavily based on [Luta](https://www.github.com/keremkoseoglu/luta).

You need to provide the inital search result page. The library will extract all prices, and follow next pages.

## Installation

First, install [Luta](https://www.github.com/keremkoseoglu/luta) by following its documentation.

Then, install sahibinden by:
```
pip install git+https://github.com/keremkoseoglu/sahibinden.git
```

## Usage

Check the test folder for sample Python codes.

Search also takes a value called post_sleep. If sahibinden.com receives too many requests in a row, it blocks your further requests. To prevent that, you can pass a post_sleep value (in seconds) to wait between each HTTP request.
