""" Quick median module """
from dataclasses import dataclass
from math import ceil
import time
from luta.crawler import Crawler # pylint: disable=E0401
from sahibinden.toolkit import extract_crawler_prices, SearchInput

@dataclass
class PageAnalysis:
    """ Sayfa analizi """
    is_multi_page: bool = False
    page_count: int = 0
    mid_page: int = 0
    crawler: Crawler = None

class QuickMedian():
    """ Quick median class """
    URL_SORT_SUFFIX = "sorting=price_asc"

    def __init__(self, search_input: SearchInput):
        self._input = search_input
        self.median = 0

        self._ensure_url_sorted_by_price()
        self._search()

    def _search(self):
        analysis = self._analyse_initial_page()

        if not analysis.is_multi_page or analysis.mid_page == 0:
            self.median = QuickMedian._get_mid_price(analysis.crawler)
            return

        if self._input.post_sleep > 0:
            time.sleep(self._input.post_sleep)

        url_suffix = f"&pagingOffset={ str(20 * analysis.mid_page) }"
        url = self._input.url + url_suffix
        mid_crawler = Crawler(url)
        self.median = QuickMedian._get_mid_price(mid_crawler)

    def _analyse_initial_page(self) -> PageAnalysis:
        result = PageAnalysis()
        result.crawler = Crawler(self._input.url)
        html = result.crawler.html

        if "sayfa içerisinde" in html:
            pages_str = result.crawler.get_value_between('<p class="mbdef">Toplam',
                                                         'sayfa içerisinde')
            if pages_str == "":
                raise Exception("Cant determine page count; possibly front end change")
            pages_str = pages_str.replace(" ", "")
            pages_int = int(pages_str)

            result.is_multi_page = True
            result.page_count = pages_int
            result.mid_page = ceil(pages_int / 2) - 1
        else:
            result.is_multi_page = False
            result.page_count = 1
            result.mid_page = 0

        return result

    @staticmethod
    def _get_mid_price(crw: Crawler) -> float:
        prices = extract_crawler_prices(crw)
        if len(prices) <= 0:
            raise Exception("No price found")
        price_pos = ceil(len(prices) / 2) - 1
        return prices[price_pos]

    def _ensure_url_sorted_by_price(self):
        if QuickMedian.URL_SORT_SUFFIX in self._input.url:
            return
        separator = "&" if "?" in self._input.url else "?"
        self._input.url += f"{ separator }{ QuickMedian.URL_SORT_SUFFIX }"
