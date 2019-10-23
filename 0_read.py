import sys
from PIL import Image

#Open and read img
imageName = sys.argv[1]
im = Image.open(imageName)
pix = im.load()
xVal,yVal = im.size
pointsArray = []

#Map pixel values to array
for y in range(yVal):
    pointsArray.append([])
    for x in range(xVal):
        pointsArray[y].append(list(pix[x,y]))

print(pointsArray)

#Log
with open('log.txt', 'a+') as out:
    out.write(f"""**READING IMAGE {imageName}**\n""")