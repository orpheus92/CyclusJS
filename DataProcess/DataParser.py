import json
from cyclus.lib import Hdf5Back
import uuid
import csv
from pyne import nucname

'''
This Object is very customize right now !!!! 
'''


# This class is defined to extract the attribute value from input json file
class JSONReader:
    def __init__(self, data):
        self.data = data

    def setData(self, data):
        self.data = data

    def getReactorAttribute(self, att):
        return self.data['simulation']['facility'][2]['config']['Reactor'][att]

    def getControlAttribute(self, att):
        return self.data['simulation']['control'][att]

    def getInstitutionAttribute(self, att):
        return self.data['simulation']['region']['institution']['config']['DeployInst'][att]['val'][2]

    def getAttribute(self):
        attributes = []
        attributes.append(self.getReactorAttribute('refuel_time'))
        attributes.append(self.getReactorAttribute('cycle_time'))
        attributes.append(self.getReactorAttribute('power_cap'))
        attributes.append(self.getControlAttribute('duration'))
        attributes.append(self.getInstitutionAttribute('build_times'))
        attributes.append(self.getInstitutionAttribute('lifetimes'))
        return attributes


class HDF5Reader:
    def __init__(self, db):
        self.db = db

    def setDB(self, db):
        self.db = db

    def getU235(self):
        pass

    def getTotalPower(self):
        TimeSeriesPower = db.query('TimeSeriesPower')
        SUM = 0
        for i, sid in enumerate(TimeSeriesPower.SimId):
            SUM += TimeSeriesPower.loc[i].Value
        return SUM
    def getTables(self):
        return db.tables


######################################################################################################

output = [['refuel_time', 'cycle_time', 'power_cap', 'duration', 'build_times', 'lifetimes', 'Totalpower']]
for i in range(0, 1000):
    with open('new' + str(i) + '.json', 'r') as f:
        data = json.load(f)
    db = Hdf5Back('out' + str(i) + '.h5')

    jsonreader = JSONReader(data)
    hdfread = HDF5Reader(db)
    tables = hdfread.getTables()

    entry = jsonreader.getAttribute()
    if "TimeSeriesPower" in tables:
        entry.append(hdfread.getTotalPower())
    else:
        entry.append(0)
    output.append(entry)

with open('output.csv', 'w') as f:
    write = csv.writer(f)
    for entry in output:
        write.writerow(entry)
