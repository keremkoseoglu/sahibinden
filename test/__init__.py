""" Tests module """
from sahibinden.search import Search
from sahibinden.quick_median import QuickMedian
from sahibinden.toolkit import SearchInput

def regular_search():
    """ Regular search """
    search_input = SearchInput(url="https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai/benzin/manuel?a277_max=2013&a277_min=2013&a276_min=100000&a276_max=200000")
    search = Search(search_input)
    for price in search.result.prices:
        print(str(price))
    print(search.result.price_median)

def quick_median_single_page():
    """ Quick median single page """
    _quick_median_with_url("https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai/benzin/manuel?a277_max=2013&a277_min=2013&a276_min=100000&a276_max=200000")

def quick_median_multi_page_no_offset():
    """ Quick median multiple page without offset """
    _quick_median_with_url("https://www.sahibinden.com/bas-gitar?query_text_mf=fender+jazz+bass&query_text=fender+jazz+bass")

def quick_median_multi_page_with_offset():
    """ Quick median multiple page with offset """
    _quick_median_with_url("https://www.sahibinden.com/bas-gitar?query_text_mf=bass")

def _quick_median_with_url(url: str):
    search_input = SearchInput(url=url)
    quick_median = QuickMedian(search_input)
    print(str(quick_median.median))
