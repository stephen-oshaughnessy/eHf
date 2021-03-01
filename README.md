# eHf - Efficient Huffman Features

eHf is a library that converts input data from any format into a feature vector set, usually for the purposes of classification. The advantage of using eHf is that no internal knowledge is required to convert the data, so features can easily be extracted from even complex binary files.


## Features

- Parse data in any format into a feature vector
- Fast runtime computation
- Represents data in a compressed format, using a modified Huffman coding algorithm
- Vectors are generated as numpy arrays, so are "out of the box" ready to pass to classification algorithms

## Installation

eHf requires [numpy](https://pypi.org/project/numpy/) to run.

```sh
pip install numpy
```

## Example usage
```sh
python simple-example.py # generates an eHf vector for a simple input string
```
```sh
python generate-ehf.py -p <path-to-data># generates an eHf vector and corresponding labels for use as a dataset 
