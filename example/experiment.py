import numpy as np
from sklearn.svm import SVC as svm

def test(relativePath, params):
    cSVM = svm(C = 10.**params['C'], gamma = 10.**params['gamma'])
    train = np.load(relativePath + "train.npy")
    test = np.load(relativePath + "test.npy")
    trainLabel = np.load(relativePath + "trainLabel.npy")
    testLabel = np.load(relativePath + "testLabel.npy")
    cSVM.fit(train, trainLabel)
    preds = cSVM.predict(test)
    return -np.sum(np.equal(preds,testLabel))*1./len(testLabel)

def main(job_id, params):
    cSVM = svm(C = 10.**params['C'], gamma = 10.**params['gamma'])
    train = np.load("train.npy")
    val = np.load("val.npy")
    trainLabel = np.load("trainLabel.npy")
    valLabel = np.load("valLabel.npy")
    cSVM.fit(train, trainLabel)
    preds = cSVM.predict(val)
    return -np.sum(np.equal(preds,valLabel))*1./len(valLabel)
