import cPickle as pickle
import numpy as np
import sys
import os
from prettytable import PrettyTable
from loadBar import LoadBar
import json

with open('basicSpearmint.json') as f:
    params = json.load(f)

spearmintMain = params['spearmintMain']
numSplits = params['numSplits']
secondsPerSplit = params['secondsPerSplit']


if not os.path.exists('results/0_results.p'):
    print "No results found! Please run some setupExperiments.py before viewing results!"
    quit()

with open('results/0_results.p') as f:
    x = pickle.load(f)
    params = [y[0] for y in x[0]['params']]

tab = PrettyTable(["Run", "NumEvals", "ValObj"] + params + ["TestObj"])
tab.align = 'l'
print "Generating Results Table/Testing Hyperparameters..."
lb = LoadBar(np.min([numSplits, 30]))
lb.setup()
for i in range(numSplits):
    if lb.test(i, numSplits): lb += 1
    with open("results/" + str(i) + "_results.p") as f:
        x = pickle.load(f)
    objectives = np.array([a['objective'] for a in x])
    cMin = x[np.argmin(objectives)]
    paramDict = dict(cMin['params'])
    sys.path.append(str(i))
    from experiment import test
    acc = test('experiments/' + str(i) + "/", paramDict)
    tab.add_row([i, len(objectives), "{:.4f}".format(cMin['objective'])]
                + ["{:.4f}".format(paramDict[p][0]) for p in params]
                + ["{:.4f}".format(acc)])
lb.clear()
print tab
