import sys
import random
from ast import literal_eval
from PIL import Image
import time

start = time.time()
#Convert input to array and read kVal
vectors = literal_eval(sys.stdin.read())
kVal = int(sys.argv[1])

#choose k initial random unequal points
centerPoints = []
while len(centerPoints) != kVal:
    candidate = random.choice(random.choice(vectors))
    if candidate not in centerPoints:
        centerPoints.append(candidate)

#clustering
testPrev = []
iterationCounter = 0
while True:
    clusteringTable = []
    for y in range(len(vectors)):
        clusteringTable.append([])
        for x in range(len(vectors[0])):
            temp = []
            temp.append(vectors[y][x])
            for k in range(kVal):
                #distance from center point
                distance = 0
                for l in range(len(centerPoints[0])):
                    distance = distance + abs(centerPoints[k][l]-vectors[y][x][l])
                temp.append(distance)
            #assign cluster centroid with min distance
            temp.append(temp[1:].index(min(temp[1:])))
            clusteringTable[y].append(temp)
    
    #check if cluster values changed, exit otherwise
    test = []
    for k in range(kVal):
        test.append(0)
        for itemY in clusteringTable:
            for itemX in itemY:
                if itemX[-1] == k:
                    test[k] = test[k] + 1
    if testPrev == test:
        break
    testPrev = test
    
    #update centroids
    for k in range(kVal):
        n = 0
        vectorTemps = [0]*len(clusteringTable[0][0][0])
        for itemY in clusteringTable:
            for itemX in itemY:
                if itemX[-1] == k:
                    for valCounter in range(len(itemX[0])):
                        vectorTemps[valCounter] = vectorTemps[valCounter] + itemX[0][valCounter]
                    n = n + 1
        #check for 0 division
        for valCounter in range(len(vectorTemps)):
            if vectorTemps[valCounter] != 0:
                vectorTemps[valCounter] = vectorTemps[valCounter]/n
        centerPoints[k] = vectorTemps
    iterationCounter = iterationCounter + 1

#Build clustered array
clusteredVectors = []
for y in range(len(clusteringTable)):
    clusteredVectors.append([])
    for x in range(len(clusteringTable[0])):
        clusteredVectors[y].append(centerPoints[clusteringTable[y][x][-1]])

print(clusteredVectors)
end = time.time()

#Log info
with open('log.txt', 'a+') as out:
    out.write(f"""**K-MEANS RESULTS**\n""")
    out.write(f"""Array size: {len(vectors)}x{len(vectors[0])}x{len(vectors[0][0])}\n""")
    out.write(f"""Parameters: kVal: {kVal}\n""")
    out.write(f"""Centroid averages: {str(centerPoints)}\n""")
    out.write(f"""Time taken: {round(end - start)} seconds\n""")