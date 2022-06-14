""" Search module """
import time
from luta.crawler import Crawler # pylint: disable=E0401
from sahibinden.search_result import SearchResult
from sahibinden.toolkit import extract_crawler_prices, HOST, SearchInput

class Search():
    """ Search class """
    def __init__(self, search_input: SearchInput):
        self._input = search_input
        self._html = ""
        self._prices = []
        self._search()
        self.result = SearchResult(self._prices)

    def _search(self):
        url = self._input.url
        while True:
            crw = Crawler(url)
            prices = extract_crawler_prices(crw)
            for price in prices:
                self._prices.append(price)

            next_url = crw.get_last_value_between('<a href="',
                                                  '" class="prevNextBut" title="Sonraki"')
            if next_url == "":
                return
            url = HOST + next_url

            if self._input.post_sleep > 0:
                time.sleep(self._input.post_sleep)
