import cPickle as pickle
import numpy as np
import sys
import os
from prettytable import PrettyTable
from loadBar import LoadBar

### SET THESE THINGS ###
params = ['C','gamma']
numTrials = 10
########################

tab = PrettyTable(["Run", "ValObj"] + params + ["TestObj"])
tab.align = 'l'
print "Generating Results Table..."
lb = LoadBar(np.min([numTrials, 30]))
lb.setup()
for i in range(numTrials):
    if lb.test(i, numTrials): lb += 1
    with open(str(i) + "/results.p") as f:
        x = pickle.load(f)
    objectives = np.array([a['objective'] for a in x])
    cMin = x[np.argmin(objectives)]
    paramDict = dict(cMin['params'])
    sys.path.append(str(i))
    from basicSVMSpearmint import test
    acc = test(str(i) + "/", paramDict)
    tab.add_row([i, "{:.4f}".format(cMin['objective'])]
                + ["{:.4f}".format(paramDict[p][0]) for p in params]
                + ["{:.4f}".format(acc)])
lb.clear()
print tab
