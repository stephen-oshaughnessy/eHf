from ehf import compress
import os
import argparse
import numpy as np
import pickle


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help='Path to files')
args = ap.parse_args()
path = args.path


# generate the Huffman feature data and labels
def feature_set(path):
    X = []
    y = []
    print("Computing Huffman features")
    for root, subdirs, files in os.walk(path):
        for f in files:
            filepath = os.path.join(root, f)
            try:
                X.append(compress(open(filepath, 'rb').read())) # Huffman feature vector
                y.append(filepath.split("/")[-2])  # family label
            except:
                continue
    for k in X:  # choose k-smallest dims
        del k[min(map(len, X)):]
    # convert to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # save the data & labels if you intend to do many runs,
    # e.g. when tuning classifier hyperparams
    pickle.dump(X, open('eHf-data', 'wb'))
    pickle.dump(y, open('eHf-labels', 'wb'))
    return X, y


if __name__ == '__main__':

    # generate feature set and labels
    # ready to pass to classifier
    X, y = feature_set(path)
