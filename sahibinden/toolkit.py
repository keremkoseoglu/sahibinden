""" Sahibinden toolkit """
from dataclasses import dataclass
from typing import List
from luta.crawler import Crawler # pylint: disable=E0401

HOST = "http://www.sahibinden.com"

def parse_price(price: str) -> float:
    """ Parses new price """
    if price is None:
        return 0
    prc = price.strip()
    if len(prc) <= 0:
        return 0
    prc_split = prc.split(" ")
    if len(prc_split) <= 0:
        return 0
    prc_text = prc_split[0].strip()
    prc_text = prc_text.replace(".", "").replace(",", ".")
    return float(prc_text)

def extract_crawler_prices(crw: Crawler) -> List[float]:
    """ Extract prices from crawler """
    result = []
    prices = crw.get_values_between('<td class="searchResultsPriceValue">', '</div>')
    for price in prices:
        float_price = parse_price(price)
        result.append(float_price)
    result.sort()
    return result

@dataclass
class SearchInput:
    """ Search input """
    url: str
    post_sleep: int = 0
