import heapq
from collections import Counter
import numpy as np


def k_smallest(array):
    """ Returns a dataset of uniform vectors. Each vector is reduced to the min length vector
       - this is necessary if you are passing the feature set to a classification algorithm """

    for k in array:
        del k[min(map(len, array)):]
    return array


def ehf_set(data):
    """input: any data sequence, including files
       output: array of Huffman codewords"""

    # get the frequencies of each symbol
    frequency = Counter(data)
    # create a heap with the weight, symbol and an empty space for the codeword
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    # add nodes to the heap
    while len(heap) > 1:
        leftchild = heapq.heappop(heap)
        rightchild = heapq.heappop(heap)
        for value in rightchild[1:]:
            value[1] = '0' + value[1]
        for value in leftchild[1:]:
            value[1] = '1' + value[1]
        heapq.heappush(heap, [rightchild[0] + leftchild[0]] + rightchild[1:] + leftchild[1:])

    # sorted array of signed int Huffman codewords
    codewords = [np.int32(i) for i in np.array(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))[:, 1]]
    return codewords
