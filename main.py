""" Sahibinden main module """
from sahibinden.search import Search

def run_test():
    """ Just a test """
    search = Search("https://www.sahibinden.com/arazi-suv-pickup-nissan-qashqai/benzin/manuel?a277_max=2013&a277_min=2013&a276_min=100000&a276_max=200000")
    for price in search.result.prices:
        print(str(price))
    print(search.result.price_median)

if __name__ == "__main__":
    run_test()
