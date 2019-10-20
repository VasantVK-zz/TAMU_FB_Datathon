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


#### SEARCH ####
while cur_traverse < max_traverse:
	n_val = 0
	notFoundP = True
	notFoundN = True
	kP = 1
	kN = -1

	while notFoundP: 
		if isclose(targetLon, f.loc[row + kP]["longitude"], rel_tol=0e-13, abs_tol=0.0): 
			notFoundP = False
		else:
			kP += 1

	while notFoundN: 
		if isclose(targetLon, f.loc[row - kN]["longitude"], rel_tol=0e-13, abs_tol=0.0): 
			notFoundN = False
		else:
			kN -= 1

	minLonP = f.loc[row + (j + kP)]["longitude"]
	minLonN = f.loc[row - (j + kN)]["longitude"]
	
	while n_val <= 75:
		minLatP = f.loc[row + i]["latitude"]
		minLatN = f.loc[row - i]["latitude"]
		minValLatP = f.loc[row + i]["val"]
		minValLatN = f.loc[row - i]["val"]


		if minValLatP > 75: 
			n_val = minValLatP
			optLat = minLatP
			optLong = minLonP
			max_traverse = cur_traverse
			cur_traverse = adj_traverse
			i = 1
			j += kP

		if minValLatN > 75: 
			n_val = minValLatN
			optLat = minLatN
			optLong = minLonN
			max_traverse = cur_traverse
			cur_traverse = adj_traverse
			i = 1
			j += kN

		i += 1
		cur_traverse += 1

	adj_traverse += 1

print("CLOSEST: ")
print(optLat)
print(optLong)