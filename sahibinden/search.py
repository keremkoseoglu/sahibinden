""" Search module """
import time
from luta.crawler import Crawler
from sahibinden.search_result import SearchResult

_HOST = "http://www.sahibinden.com"

class Search():
    """ Search class """
    def __init__(self, url: str, post_sleep: int = 0):
        self._url = url
        self._post_sleep = post_sleep
        self._html = ""
        self._prices = []
        self._search()
        self.result = SearchResult(self._prices)

    @staticmethod
    def _parse_price(price: str) -> float:
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

    def _search(self):
        url = self._url
        while True:
            crw = Crawler(url)
            if self._post_sleep > 0:
                time.sleep(self._post_sleep)

            prices = crw.get_values_between('<td class="searchResultsPriceValue">', '</div>')
            for price in prices:
                float_price = Search._parse_price(price)
                self._prices.append(float_price)

            next_url = crw.get_last_value_between('<a href="', '" class="prevNextBut" title="Sonraki"')
            if next_url == "":
                return
            url = _HOST + next_url
