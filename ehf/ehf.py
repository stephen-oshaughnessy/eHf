import numpy as np
from collections import Counter


def position(probability, value, index):
    for j in range(len(probability)):
        if (value >= probability[j]):
            return j
    return index - 1


def codewords(probability):
    """ returns the feature vector of Huffman codes"""
    num = len(probability)
    huffman = [''] * num
    for i in range(num - 2):
        val = probability[num - i - 1] + probability[num - i - 2]
        if huffman[num - i - 1] != '' and huffman[num - i - 2] != '':
            huffman[-1] = ['1' + symbol for symbol in huffman[-1]]
            huffman[-2] = ['0' + symbol for symbol in huffman[-2]]
        elif huffman[num - i - 1] != '':
            huffman[num - i - 2] = '0'
            huffman[-1] = ['1' + symbol for symbol in huffman[-1]]
        elif huffman[num - i - 2] != '':
            huffman[num - i - 1] = '1'
            huffman[-2] = ['0' + symbol for symbol in huffman[-2]]
        else:
            huffman[num - i - 1] = '1'
            huffman[num - i - 2] = '0'

        pos = position(probability, val, i)
        probability = probability[0:(len(probability) - 2)]
        probability.insert(pos, val)
        if isinstance(huffman[num - i - 2], list) and isinstance(huffman[num - i - 1], list):
            complete_code = huffman[num - i - 1] + huffman[num - i - 2]
        elif isinstance(huffman[num - i - 2], list):
            complete_code = huffman[num - i - 2] + [huffman[num - i - 1]]
        elif isinstance(huffman[num - i - 1], list):
            complete_code = huffman[num - i - 1] + [huffman[num - i - 2]]
        else:
            complete_code = [huffman[num - i - 2], huffman[num - i - 1]]

        huffman = huffman[0:(len(huffman) - 2)]
        huffman.insert(pos, complete_code)

    huffman[0] = ['0' + symbol for symbol in huffman[0]]
    huffman[1] = ['1' + symbol for symbol in huffman[1]]

    if len(huffman[1]) == 0:
        huffman[1] = '1'
    count = 0
    symbols = [''] * num
    for i in range(2):
        for j in range(len(huffman[i])):
            symbols[count] = huffman[i][j]
            count += 1
    symbols = sorted(symbols, key=len)
    symbols = [i for i in symbols if i]
    return [np.int32(i) for i in symbols] # return the signed int feature set


def compress(sequence):
    """Get the frequencies of each alphabet char
       and compute the corresponding Huffman codes"""
    freq = Counter(sequence)
    freq = sorted(freq.items(), key=lambda a: a[1], reverse=True)
    probabilities = sorted([float("{:.2f}".format(frequency[1] / len(sequence))) for frequency in freq], reverse=True)
    return codewords(probabilities)




