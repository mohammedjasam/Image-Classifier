import ast
import csv
from collections import defaultdict
from scipy.spatial import distance

## Generates accessible Latitudes and Longitudes
def extract_ll(la,lo,code):
    la=la[:-3]
    lo=lo[1:-3]
    if code == 1:
        return la+","+lo
    elif code == 2:
        return la+",-"+lo
    elif code == 3:
        return "-"+la+","+lo
    elif code == 4:
        return "-"+la+",-"+lo

"""==================================================="""
""" ENTER THE LATITUDE AND LONGITUDE & ALSO THE RADIUS"""
"""==================================================="""

s="36.1699° N, 115.1398° W"
### Distance is in Meters
dist = 100
"""==================================================="""
dist = dist/1000
la,lo = s.split(',')
if la[-1]=='N':
    if lo[-1]=='E':
        location=extract_ll(la,lo,1)
    else:
        location=extract_ll(la,lo,2)
else:
    if lo[-1]=='E':
        location=extract_ll(la,lo,3)
    else:
        location=extract_ll(la,lo,4)
# extract_ll()
lat,lon = location.split(",")

a=(float(lat),float(lon))
# print(a)

aLa = str(lat)
aLo = str(lon)
# aLa='33.4255'
# aLo='-111.9400'
# a = (33.4255,-111.9400)

columns = defaultdict(list)

with open('yelp_business1.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

l=[]
latlon=[]
longi=[]
ctr=0

NearByLocations=[]

la={}
lo={}


# print(columns['latitude'][2][0:2])
# print(len(columns['latitude']))

### Indexes the Latitudes for better search
ind = {}
for x in range(len(columns['latitude'])):
    try:
        ind[columns['latitude'][x][0:2]].append((columns['latitude'][x],columns['longitude'][x]))
    except:
        ind[columns['latitude'][x][0:2]] = [(columns['latitude'][x],columns['longitude'][x])]
# print(ind)

# print(aLa[0:2])
target = ind[aLa[0:2]]
# print(len(target))

# print(target[0])


for x in range(len(target)):
    try:
        dst = distance.euclidean(a,(float(target[x][0]),float(target[x][1])))
        if dst<=dist:   ### Specify the distance in KM
            # print(x,dst)   ### Returns the id number and the distance between the locations
            NearByLocations.append((target[x][0],target[x][1]))
    except:
        pass
# '''### Contains all the Restaurants near a 1000m radius'''
# print(NearByLocations)

### Dict of (Lat:Long)
# print(dict(NearByLocations))
NearByLocations=dict(NearByLocations)

fail=0
business_id=[]  ## Used to store the restaurant business_id!
with open('yelp_business1.csv') as f:
    for i,line in enumerate(f):
        if i==0:
            pass
        else:
            line = line.split(",")
            try:
                if NearByLocations[line[1]]:
                    #                    business_id,Name,Rating,City,Latitude,Longitude
                    business_id.append((line[0],[line[3],line[4],line[5],line[1],line[2]]))
            except:
                fail=1

business_id = business_id[0:10]
if fail==1 and len(business_id)==0:
    print("Sorry, no restaurants nearby!\n")
business_id = dict(business_id)
# for x in range(5):
# print(business_id)



finalRes = {}

### Checking the sentiment for the restaurants!
with open('yelp_reviews.csv') as freviews:
    # print("City, Restaurant, Rating, Latitude, Longitude")#, business_id, latitude, longitude")
    for i,line in enumerate(freviews):
        if i==0:
            pass
        line = line.split(",")
        # print(line[1])

        if line[1] in business_id.keys():
            if int(line[7])>0: ## Checks for sentiment
                if float(business_id[line[1]][1])>3:
                    finalRes[business_id[line[1]][0]]=(business_id[line[1]][2], business_id[line[1]][0], business_id[line[1]][1], business_id[line[1]][3],business_id[line[1]][4])
                # print(business_id[line[1]][2], business_id[line[1]][0], business_id[line[1]][1], business_id[line[1]][3],business_id[line[1]][4])#, line[0], line[1])#, line[7])
        # if line[1] in
# finalRes = list(set(finalRes))

# print(finalRes)

# print (l[0].ljust(10), l[1].ljust(30), l[2].ljust(20))
# print("{:<8} {:<15} {:<10}".format('City','Restaurant','Rating'))
print("City".ljust(10), "Restaurant".ljust(30), "Rating".ljust(20))
print("-------------------------------------------------")
for k, v in finalRes.items():
    l = v
    print (l[0].ljust(10), l[1].ljust(30), l[2].ljust(20))

    # print ("{:<8} {:<15} {:<10}".format(l[0], l[1], l[2]))
# for x in finalRes.values():
#     print(x)


### Finds out the categories in the restaurants
# main=[]
#
# for x in columns['categories']:
#     jj=ast.literal_eval(x)
#     if 'Restaurants' in jj:
#         l.append(jj)
#
# for x in l:
#     for y in x:
#         main.append(y)
#
# main=list(set(main))
#
# print(main)
