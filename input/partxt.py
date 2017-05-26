import subprocess
import numpy as np
import random
import json
import string

def myconst(val,num):
    return [val] * num

# dictionary that stores sample functions
sammpleDict = {"rint": random.randint,
               "rdouble": random.uniform,
               "rrange": random.randrange,
               "lins": np.linspace,
               "const": myconst}

with open('spec.json', 'r') as f:
    spec = json.load(f)

    numparam = len(spec["config"])

for i in range(100):
    file = open(spec["input"]["name"], 'r')
    contents = file.read()
    for j in range(numparam):
        cfunc = sammpleDict[spec["config"][str(j)]["samplef"]]
        contents = contents.replace(spec["config"][str(j)]["key"], str(cfunc(*spec["config"][str(j)]["range"])))

    tfile = open('new' + str(i) + '.json', 'w')
    tfile.write(contents)
    tfile.close()
    subprocess.call(['cyclus', 'new' + str(i) + '.json', '-o', 'out' + str(i) + '.h5'])
    file.close()