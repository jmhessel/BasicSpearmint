# Introduction
I really like the bayesian optimization tool Spearmint (https://github.com/HIPS/Spearmint) but I found that some of its functionality was confusing and overkill if one is trying to run a few tests locally on some data. I have built some tools to streamline the process of small-scale hyperparameter optimization. Hopefully the tool is simple enough to understand -- it's just a few python scripts. I mostly made this repository for myself, but if others find it useful, that's awesome too!

## Features supported

* Basic HP optimization, geared towards supervised learning tasks
* Train/validation/test splits

## Dependencies

* Python 2.7
* [numpy](http://www.numpy.org/)
* [Spearmint](https://github.com/HIPS/Spearmint) (and all of its dependencies)
* [PrettyTable](https://pypi.python.org/pypi/PrettyTable)

# Get started quickly with an example

Included with this repository is an example configuration and dataset, under the `example` directory. Copy the `config.json` and `experiment.py` into the root directory of this repository, and then unzip `exampleData` into the `experiments` directory. Then, run `setupExperiments.py`, followed by `viewExperiments.py`.

# How to use with your own data

1. Get your dataset and determine how many train/val/test splits you want to make
2. Fill the experiment folder with your data from each of your splits (see readme in the folder for specifics)
3. Fill in what hyperparameters you want to optimize in `config.json` (see [Spearmint's config json examples](https://github.com/HIPS/Spearmint/tree/master/examples/simple) or example/config.json)
4. Fill in your training/evaluation functions in `experiment.py` (see comments in file for help, and the example in example/experiment.py)
5. Set the 3 parameters in basicSpearmint.json appropriately
6. Run `python setupExperiments.py` and watch the magic of Bayesian Optimization!
7. Once that is done, run `python viewResults.py` and wait for your results to be tested.
8. Testing results using best hyperparameter settings will be printed in a table, and validation results will be saved in pickle files under the `results` directory.