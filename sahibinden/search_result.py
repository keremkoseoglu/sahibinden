""" Sahibinden search result module """
from typing import List


class SearchResult():
    """ Search result class """
    def __init__(self, prices:List[float]):
        self._prices = prices
        self._prices.sort()
        self._price_count = len(self._prices)
        self._price_sum = 0
        self._price_sum_calculated = False
        self._price_avg = 0
        self._price_avg_calculated = False
        self._price_med = 0
        self._price_med_calculated = False



    @property
    def prices(self) -> List[float]:
        return self._prices


    @property
    def price_sum(self) -> float:
        """ Sum of all prices """
        if not self._price_sum_calculated:
            for price in self._prices:
                self._price_sum += price
            self._price_sum_calculated = True
        return self._price_sum


    @property
    def price_median(self) -> float:
        """ Returns the median of prices """
        if not self._price_med_calculated:
            if self._price_count > 0:
                pos = int(self._price_count / 2)
                self._price_med = self._prices[pos]
            self._price_med_calculated = True
        return self._price_med


    @property
    def price_average(self) -> float:
        """ Returns average price """
        if not self._price_avg_calculated:
            if self._price_count> 0:
                self._price_avg = self.price_sum / self._price_count
            self._price_avg_calculated = True
        return self._price_avg
