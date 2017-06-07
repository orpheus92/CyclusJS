import random
import csv

with open('data.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    #print(headers)
    total = []
    for row in f_csv:
#    for row in f_csv:
#print(row)
    	total.append(row)
#print(total)
ind = random.sample(range(1, 100000), 100)
newlist = []
for i in ind:
    newlist.append(total[i])
#print(newlist)
with open('select.csv','w') as f2:
    f_csv = csv.writer(f2)
    f_csv.writerow(headers)
    f_csv.writerows(newlist)
