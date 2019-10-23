import sys
import math
from ast import literal_eval
from PIL import Image
import time

#Distance functions
def EuclideanDistance(P,Q):
    intermediateValues = []
    for i in range(len(P[2])):
        intermediateValues.append(math.pow(Q[2][i]-P[2][i],2))
    return math.sqrt(sum(intermediateValues))

def MaximumDistance(P,Q):
    intermediateValues = []
    for i in range(len(P[2])):
        intermediateValues.append(abs(Q[2][i]-P[2][i]))
    return max(intermediateValues)

#Finds all neighbor points for a chosen point
def FindNeighbours(Point, Points, distanceFunction, eps):
    tempNeighbours = []
    for y in range(len(Points)):
        for x in range(len(Points[0])):
            if distanceFunction == "e":
                if EuclideanDistance(Point, Points[y][x]) <= eps:
                    tempNeighbours.append(Points[y][x])
            if distanceFunction == "m":
                if MaximumDistance(Point, Points[y][x]) <= eps:
                    tempNeighbours.append(Points[y][x])
    return tempNeighbours

start = time.time()
#Read parameters
vectors = literal_eval(sys.stdin.read())
eps = int(sys.argv[1])
minPts = int(sys.argv[2])
distFunc = sys.argv[3]

if distFunc != "e" and distFunc != "m":
    sys.exit(1)

#prepare array
pointsArray = []
for y in range(len(vectors)):
    pointsArray.append([])
    for x in range(len(vectors[0])):
        pointsArray[y].append([y,x,vectors[y][x],"Undefined"])

#DBSCAN
clusterCounter = 0
progress = 0
for y in range(len(vectors)):
    for x in range(len(vectors[0])):
        if pointsArray[y][x][-1] != "Undefined":
            continue

        Neighbours = FindNeighbours(pointsArray[y][x], pointsArray, distFunc, eps)
        if len(Neighbours) < minPts:
            pointsArray[y][x][-1] = "Noise"
            continue
        
        clusterCounter = clusterCounter + 1
        pointsArray[y][x][-1] = str(clusterCounter)
        if pointsArray[y][x] in Neighbours:
            Neighbours.remove(pointsArray[y][x])
        
        for innerPoint in Neighbours:
            if innerPoint[-1] == "Noise":
                pointsArray[innerPoint[0]][innerPoint[1]][-1] = str(clusterCounter)
            if innerPoint[-1] != "Undefined":
                continue
            pointsArray[innerPoint[0]][innerPoint[1]][-1] = str(clusterCounter)
            NeighboursInner = FindNeighbours(innerPoint, pointsArray, distFunc, eps)
            if len(NeighboursInner) >= minPts:
                Neighbours.append(NeighboursInner)

#Get distinct clusters
clusterNumbers = []
for y in range(len(vectors)):
    for x in range(len(vectors[0])):
        if pointsArray[y][x][-1] not in clusterNumbers:
            clusterNumbers.append(pointsArray[y][x][-1])

#Map cluster's averages
averagesForClusters = []
for item in clusterNumbers:
    n = 0
    vectorTemps = [0]*len(pointsArray[0][0][2])
    for y in range(len(vectors)):
        for x in range(len(vectors[0])):
            if pointsArray[y][x][-1] == item:
                for i in range(len(pointsArray[y][x][2])):
                    vectorTemps[i] = vectorTemps[i] + pointsArray[y][x][2][i]
                n = n + 1
    #Check 0 division
    for i in range(len(vectorTemps)):
        if vectorTemps[i] != 0:
            vectorTemps[i] = vectorTemps[i]/n
    averagesForClusters.append(vectorTemps)

#Build clustered array and change cluster averages with initial values
clusteredVectors = []
for y in range(len(pointsArray)):
    clusteredVectors.append([])
    for x in range(len(pointsArray[0])):
        clusteredVectors[y].append(averagesForClusters[clusterNumbers.index(pointsArray[y][x][-1])])

print(clusteredVectors)
end = time.time()

#Log info
with open('log.txt', 'a+') as out:
    out.write(f"""**DBSCAN RESULTS**\n""")
    out.write(f"""Array size: {len(vectors)}x{len(vectors[0])}x{len(vectors[0][0])}\n""")
    out.write(f"""Parameters: Eps: {eps}, minPts: {minPts}, distFunc: {distFunc}\n""")
    out.write(f"""Number of identified clusters: {len(clusterNumbers)}\n""")
    out.write(f"""Cluster averages: {str(averagesForClusters)}\n""")
    out.write(f"""Time taken: {round(end - start)} seconds\n""")
