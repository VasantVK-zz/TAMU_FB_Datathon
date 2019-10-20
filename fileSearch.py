import pandas as pd
import numpy as np
from math import isclose
from sys import exit

# Sample part 3 implementation file
file = "3001120103003.csv"
f = pd.read_csv(file)
row = 228233
targetLat = f.loc[row]["latitude"]
targetLon = f.loc[row]["longitude"]

print("TARGET: ")
print(targetLat)
print(targetLon)

print()

#### INITIALIZATION ####
# Initializing search for closest road
#n_val = 0 # initialized later
# Traverses are based on L1/Manhattan distance
cur_traverse = 1 # for each lat iteration
adj_traverse = 0 # for each lon iteration
max_traverse = 100000 # max iterations (readjusted when there is a new optimal lat/lon)
i = 1 # lat interval (1 so it doesn't count itself)
j = 1 # long interval (1 so it doesn't count itself)
notFound = True
k = 1 # long increment (1 so it doesn't count itself)
while notFound: 
	if isclose(targetLon, f.loc[row + k]["longitude"], rel_tol=0e-13, abs_tol=0.0): 
		notFound = False
	else:
		k += 1


print(k)
#### SEARCH ####
while cur_traverse < max_traverse:
	n_val = 0

	minLonP = f.loc[row + j*k]["longitude"]
	minLonN = f.loc[row - j*k]["longitude"]

	
	while n_val <= 75:
		minLatP = f.loc[row + i]["latitude"]
		minLatN = f.loc[row - i]["latitude"]
		minValLatP = f.loc[row + i]["val"]
		minValLatN = f.loc[row - i]["val"]

		print(f.loc[row + j*k]["longitude"])

		if minValLatP > 75: 
			n_val = minValLatP
			optLat = minLatP
			optLong = minLonP
			max_traverse = cur_traverse
			cur_traverse = adj_traverse

		if minValLatN > 75: 
			n_val = minValLatN
			optLat = minLatN
			optLong = minLonN
			max_traverse = cur_traverse
			cur_traverse = adj_traverse

		i += 1
		cur_traverse += 1

	adj_traverse += 1
	j += 1

print()
print(optLat)
print(optLong)