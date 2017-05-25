import json
import random
import subprocess
#import cyclus.lib as cl
#import cyclus.simstate
from collections import OrderedDict
#class JSONObject:
#    def __init__(self, d):
#        self.__dict__ = d

def changere(datain,ind,facility, attr, val ):
    datain['simulation']['facility'][ind]['config'][facility][attr] = val
    return datain

def changeinst(datain, att, ind, val ):
    datain['simulation']['region']['institution']['config']['DeployInst'][att]['val'][ind] = val
    return datain

def changectrl(datain, att, val ):
    datain['simulation']['control'][att] = val
    return datain
for i in range(100):

    with open('1.json', 'r') as f:
        data = json.load(f)
        #print(data['simulation']['region']['institution']['config']['DeployInst'])

    # change refuel_time for facility at index 2 (reactor)
    newd = changere(data, 2, 'Reactor', 'refuel_time', random.randint(1,3))
    # change cycle_time for facility at index 2 (reactor)
    newd = changere(data, 2, 'Reactor', 'cycle_time', random.randint(14,20))
    # change power capacity for facility at index 2 (reactor)
    newd = changere(data, 2 ,'Reactor', 'power_cap', random.uniform(200,1200))
    # change duration for simulation
    dur = random.randrange(12, 600, 6)
    newd = changectrl(newd, 'duration', dur)
    # change build_time for facility at index 2(reactor)
    newd = changeinst(newd, 'build_times', 2, random.randint(1,dur))
    # change lifetime for facility at index 2(reactor)
    newd = changeinst(newd, 'lifetimes', 2, random.randint(12,dur))


    with open('new'+str(i)+'.json', 'w') as f2:
        json.dump(newd, f2,indent=4, sort_keys=True)
    #myc = cyclus.simstate.SimState('new.json')
    #cyclus.main.run_simulation('new.json')
    #mysim = cyclus

    #cyclus ('new.json')
    #mysim = cl.Timer.run_sim(self,'new.json')
    subprocess.call(['cyclus','new'+str(i)+'.json', '-o', 'out'+str(i)+'.h5'])
