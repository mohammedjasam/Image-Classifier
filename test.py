import ast
import csv
from collections import defaultdict
from scipy.spatial import distance

# Declaring the user location
aLa='40.4535915'
aLo='-80.0008071'
a = (40.4535915,-80.0008071)

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
print(len(target))

# print(target[0])


for x in range(len(target)):
    try:
        dst = distance.euclidean(a,(float(target[x][0]),float(target[x][1])))
        if dst<=0.1:
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
                    business_id.append((line[0],[line[1],line[2]]))
            except:
                fail=1

business_id = business_id[0:10]
if fail==1 and len(business_id)==0:
    print("Sorry, no restaurants nearby!\n")
business_id = dict(business_id)
# for x in range(5):
# print(business_id)





### Checking the sentiment for the restaurants!
with open('yelp_reviews.csv') as freviews:
    print("user_id, business_id, latitude, longitude")
    for i,line in enumerate(freviews):
        if i==0:
            pass
        line = line.split(",")
        # print(line[1])

        if line[1] in business_id.keys():
            if int(line[7])>20: ## Checks for sentiment

                print(line[0],line[1], line[7])#, business_id[line[1]])
        # if line[1] in



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
