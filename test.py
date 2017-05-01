from scipy.spatial import distance
a = (1,2,3)
b = (4,5,6)

a = (33.4373,-112.0078)
b = (33.4544,-111.8857)
c = (33.3062,-111.8413)
# 33.4373° N, 112.0078° W
dst = distance.euclidean(a,b)
print(dst)
dst = distance.euclidean(a,c)
print(dst)
