import os
import subprocess
import time
import zlib
import numpy as np
import json
import sys
import cPickle as pickle
import json

with open('basicSpearmint.json') as f:
    params = json.load(f)

spearmintMain = params['spearmintMain']
numSplits = params['numSplits']
secondsPerSplit = params['secondsPerSplit']

print "Performing bayesian optimization over {} splits, with {} seconds per split".format(numSplits, secondsPerSplit)
print "This will take a total of {} seconds.".format(numSplits*secondsPerSplit)
time.sleep(1)

print "Checking experiment setup..."

#Check to make things are setup properly...
if not os.path.exists(spearmintMain):
    print "Please modify basicSpearmint.json's spearmintMain variable to point towards the location of spearmint's main!"
    quit()

def checkExperimentFolder(directory):
    files = os.listdir(directory)
    neededFiles = ['train.npy','val.npy','test.npy',
                   'trainLabel.npy', 'valLabel.npy','testLabel.npy']

    if not set(neededFiles).issubset(set(files)):
        print "Invalid experiment directory: " + directory
        print "The directory must contain the following files..."
        for n in neededFiles:
            print n
        quit()

for i in range(numSplits):
    if not os.path.exists('experiments/' + str(i)):
        print "Experiment directory missing: experiments/" + str(i)
        print "Please make sure that this directory exists!"
        quit()
    checkExperimentFolder('experiments/'+str(i))

#### end formatting checks
def decompress_array(a):
    return np.fromstring(zlib.decompress(a['value'].decode('base64'))).reshape(a['shape'])

os.system('mongo spearmint --eval "db.dropDatabase()"')
os.system('rm -rf .tempResults')
for i in range(numSplits):
    os.system('mkdir .tempResults')
    os.system("cp experiment.py experiments/" + str(i))
    os.system("cp config.json experiments/" + str(i))
    p = subprocess.Popen(["python",spearmintMain,
                          'experiments/' + str(i)])
    time.sleep(secondsPerSplit)
    p.kill()
    os.system("mongoexport --db spearmint --collection experiment.jobs --out .tempResults/tmp.jsons")
    runs = []
    with open('.tempResults/tmp.jsons') as f:
        for line in f:
            runs.append(json.loads(line))
    
    #the output will be a list of of param settings coupled with their objective values
    output = []
    for r in runs:
        if r['status'] != 'complete':
            continue
        cOut = {}
        params = []
        for p,v in r['params'].iteritems():
            params.append((p,decompress_array(v['values'])))
        cOut['params'] = params
        cOut['objective'] = r['values']['main']
        output.append(cOut)
    if len(output) == 0:
        print "No runs were completed! Please allocate more time per split in basicSpearmint.json"
        quit()
        
    with open('results/' + str(i) + "_results.p", 'w') as f:
        pickle.dump(output, f)
        
    os.system('rm -rf .tempResults')
    os.system('mongo spearmint --eval "db.dropDatabase()"')
