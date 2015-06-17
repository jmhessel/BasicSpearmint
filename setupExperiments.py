import os
import subprocess
import time
import zlib
import numpy as np
import json
import sys
import cPickle as pickle

### SET THESE THINGS ###
secondsPerTrial = 3600
#this is how many train/val/test splits you have made
numTrials = 10
#this is the location of spearmint's main in your filesystem.
#for me, this line is set as...
#spearmintMain = "/usr/local/lib/python2.7/dist-packages/spearmint-0.1-py2.7.egg/spearmint/main.py"
spearmintMain = ''
########################

if len(spearmintMain) == 0:
    print "Please set your spearmint main variable at the top of setupExperiments.py"
    quit()

def decompress_array(a):
    return np.fromstring(zlib.decompress(a['value'].decode('base64'))).reshape(a['shape'])

for i in range(numTrials):
    os.system("cp experiment.py " + str(i))
    os.system("cp config.json " + str(i))
    p = subprocess.Popen(["python",spearmintMain,
                          str(i)])
    time.sleep(secondsPerTrial)
    p.kill()
    os.system("mongoexport --db spearmint --collection basicSVMSpearmint.jobs --out tmp.jsons")
    runs = []
    with open('tmp.jsons') as f:
        for line in f:
            runs.append(json.loads(line))
    
    #the output will be a list of of param settings coupled with their objective values
    output = []
    for r in runs:
        cOut = {}
        params = []
        for p,v in r['params'].iteritems():
            params.append((p,decompress_array(v['values'])))
        cOut['params'] = params
        cOut['objective'] = r['values']['main']
        output.append(cOut)
    with open(str(i) + "/results.p", 'w') as f:
        pickle.dump(output, f)
        
    os.system('rm tmp.jsons')
    os.system('mongo spearmint --eval "db.dropDatabase()"')
