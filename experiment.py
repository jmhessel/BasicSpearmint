import numpy as np

def main(job_id, params):
    '''Params is a dictionary mapping from parameters specified in the
    config.json file to values that Spearmint has sugguested. This
    function will likely train a model on your training data, and
    return some function evaluated on your validation set. Small =
    better! Spearmint minimizes by default, so negate when it is so
    required.
    '''
    train = np.load("train.npy")
    val = np.load("val.npy")
    
    trainLabels = np.load("trainLabel.npy")
    valLabels = np.load("valLabel")

    #Fill in your training/validation code here, based on the this params setting

    return -1.


def test(relativePath, params):
    '''This function is the testing function -- it's handed a relative
    path (which you may likely ignore) and the best setting of the
    parameters, as determined by spearmint. The function returns some
    evaluation of these parameters on the testing data.'''

    train = np.load(relativePath + "train.npy")
    test = np.load(relativePath + "test.npy")

    trainLabel = np.load(relativePath + "trainLabel.npy")
    testLabel = np.load(relativePath + "testLabel.npy")

    #Fill in your training/testing code here, based on this "optimal" parameter setting

    return -1.
