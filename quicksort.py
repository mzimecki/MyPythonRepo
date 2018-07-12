import sys
from time import time
from random import shuffle, randint
from contextlib import contextmanager

sys.setrecursionlimit(10000)


@contextmanager
def measure(name):
    t = time()
    yield
    print('[{}] finished in {} ms'.format(name, int((time() - t) * 1000)))


def quicksort(list):
    """quicksort with pivot as first element"""
    if len(list) < 2:
        return list
    pivot = list[0]
    greater = [elem for elem in list[1:] if elem >= pivot]
    less = [elem for elem in list[1:] if elem < pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def quicksort2(list):
    """quicksort with random pivot"""
    if len(list) < 2:
        return list
    piv_idx = randint(0, len(list) - 1)
    pivot = list.pop(piv_idx)
    greater = [elem for elem in list if elem >= pivot]
    less = [elem for elem in list if elem < pivot]
    return quicksort2(less) + [pivot] + quicksort2(greater)


myList = list(range(10000))
shuffle(myList)
with measure('quicksort'):
    quicksort(myList)
with measure('quicksort2'):
    quicksort2(myList)
