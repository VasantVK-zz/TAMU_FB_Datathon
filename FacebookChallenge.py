import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 
import os
import glob

# Pulling all the files from the directory into a list
file_list = []

directory = '/Users/Satish/Desktop/TAMUDatathon/ml_preds_csv/'

startFile = '/Users/Satish/Desktop/TAMUDatathon/ml_preds_csv/3001120103133.csv'

populationFile = '/Users/Satish/Desktop/TAMUDatathon/tz_popdens_sample.csv'


for files in os.listdir(directory):
    file_list.append(files)

left = 0
right = len(file_list) - 1


# Returns index of x in arr if present, else -1 
def binarySearch (currFile, topLong, bottomLong, topLat, bottomLat, targetLong, targetLat, l, r): 
  
    # Check base case 
    if (bottomLong <= targetLong and targetLong <= topLong) and (topLat <= targetLat and targetLat <= bottomLat):

        return currFile  
  
    else: 
        mid = (r - l) // 2

        if targetLong > topLong:
            if targetLat
            l = mid
            currDirectory = directory + file_list[l]
            theFile = pd.read_csv(currDirectory)
            convertCurrFile = np.array(theFile)
            FirstLat = convertCurrFile[0][3]
            LastLat = convertCurrFile[len(convertCurrFile) - 1][3]
            FirstLon = convertCurrFile[0][4]
            LastLon = convertCurrFile[len(convertCurrFile) - 1][4]

            return binarySearch(currDirectory, LastLon, FirstLon, FirstLat, LastLat, targetLong, targetLat, l, r)

        elif targetLong < topLong:
            r = mid
            currDirectory = directory + file_list[r]
            theFile = pd.read_csv(currDirectory)
            convertCurrFile = np.array(theFile)
            FirstLat = convertCurrFile[0][3]
            LastLat = convertCurrFile[len(convertCurrFile) - 1][3]
            FirstLon = convertCurrFile[0][4]
            LastLon = convertCurrFile[len(convertCurrFile) - 1][4]

            return binarySearch(currDirectory, LastLon, FirstLon, FirstLat, LastLat, targetLong, targetLat, l, r)
    
    return currFile

def inFileSearch (objFile, l, lengthOfFile, x, y): 
    if lengthOfFile >= l: 
  
        mid = l + (lengthOfFile - l)/2

        if objFile[mid][3] == x and objFile[mid][4] == y: 
            return mid
            
        elif objFile[mid][3] > x : 
            if objFile[mid][4] > y:
                return inFileSearch(objFile, l, mid-1, targetLat, targetLong) 
   
        else: 
            if objFile[mid][3] < x : 
                if objFile[mid][4] < y:
                    return inFileSearch(objFile, mid + 1, lengthOfFile, targetLat, targetLong) 
  
    else: 
        return -1



    

readCurrPopFile = pd.read_csv(populationFile)

currPopFile = np.array(readCurrPopFile)


for files in currPopFile:
    # Read from the starting file which is the 32nd file
    currFile = pd.read_csv(startFile)
    currentFile = np.array(currFile)
    FirstLat = currentFile[0][3]
    LastLat = currentFile[len(currentFile)-1][3]
    FirstLon = currentFile[0][4]
    LastLon = currentFile[len(currentFile)-1][4]
    # Gets the current latitude and longitude in the list
    TargetLat = files[1]
    TargetLon = files[2]
    # Performs binary search and returns file with the value in it
    newFile = binarySearch(currFile, LastLon, FirstLon, FirstLat, LastLat, TargetLon, TargetLat, left, right)

    objFile = np.array(objFile)

    lengthOfFile = len(objFile)

  
    result = inFileSearch(objFile, 0, lengthOfFile-1, TargetLat, TargetLon) 




