# BasicSpearmint
A simple tool for small scale bayesian optimization

# Introduction
I really like the bayesian optimization tool Spearmint (https://github.com/HIPS/Spearmint) but I found that some of its functionality was confusing and overkill if one is trying to run a few tests locally on some data. I have built some tools to streamline the process of small-scale hyperparameter optimization. Hopefully the tool is simple enough to understand -- it's just a few python scripts. I mostly made this repository for myself, but if others find it useful, that's awesome too!

## Features supported

* Basic HP optimization, geared towards supervised learning tasks
* Train/validation/test splits

## Dependencies

* Python 2.7
* numpy (http://www.numpy.org/)
* Spearmint (and all of its dependencies) (https://github.com/HIPS/Spearmint)
* PrettyTable (https://pypi.python.org/pypi/PrettyTable)

# How to use

1. For your particular experiment, create numbered subdirectories
(i.e. "0", "1", "2", etc.) of the experiments folder. By default, these should
contain 6 .npy files (created from `numpy.save()`). They should be called...
  *`train.npy` (a numExamples by numFeatures matrix of your training data)
  *`val.npy` (a numExamples by numFeatures matrix of your validation data)
  *`test.npy` (a numExamples by numFeatures matrix of your testing data)
  *`trainLabel.npy` (a length numExamples array of training labels)
  *`valLabel.npy` (a length numExamples array of validation labels)
  *`testLabel.npy` (a length numExamples array of training labels)
This is where you 