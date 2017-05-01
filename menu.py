import ast
import csv
from collections import defaultdict
from scipy.spatial import distance


# print(dst)

aLa='33.4255'
aLo='-111.9400'
a = (33.4255,-111.9400)



columns = defaultdict(list)

with open('yelp_business1.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

# print(columns)
l=[]
latlon=[]
longi=[]
ctr=0

locs=[]

la={}
lo={}


for x in columns['latitude']:
    try:
        la[x[0:2]].append(x)
    except:
        la[x[0:2]]=[x]
# print(la)
for x in columns['longitude']:
    try:
        lo[x[0:2]].append(x)
    except:
        lo[x[0:2]]=[x]
# print(lo)

tarLa=la[aLa[0:2]]
tarLo=lo[aLo[0:2]]
print(tarLo)

    # for y in columns['longitude']:
for x in range(len(tarLa)):
    # for y in tarLo:
        dst = distance.euclidean(a,(float(tarLa[x]),float(tarLo[x])))
        # print(dst)
        if dst<=0.1:
            print(dst)

            locs.append((tarLa[x],tarLo[x]))

print(locs)


# for x in columns['latitude']:
#     for y in columns['longitude']:
#         dst = distance.euclidean(a,(float(x),float(y)))
#         if dst<=0.3:
#             locs.append((x,y))
#
# print(locs)

# print("HI")
#
# for x in columns['categories']:
#     jj=ast.literal_eval(x)
#     if 'Restaurants' in jj:
#         l.append(jj)
#
# main=[]
#
# for x in l:
#     for y in x:
#         main.append(y)
#
# main=list(set(main))
#









# print(main)
