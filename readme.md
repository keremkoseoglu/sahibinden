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

Here is a sample Python code:

```
from sahibinden.search import Search
search = Search("https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai/benzin/manuel?a277_max=2013&a277_min=2013&a276_min=100000&a276_max=200000")
for price in search.result.prices:
    print(str(price))
print(search.result.price_median)
```

Search also takes a value called post_sleep. If sahibinden.com receives too many requests in a row, it blocks your further requests. To prevent that, you can pass a post_sleep value (in seconds) to wait between each HTTP request.

```
from sahibinden.search import Search
search = Search("https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai/benzin/manuel?a277_max=2013&a277_min=2013&a276_min=100000&a276_max=200000", post_sleep=10)
for price in search.result.prices:
    print(str(price))
print(search.result.price_median)
```