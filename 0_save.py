import sys
from ast import literal_eval
from PIL import Image

#Convert input to array and read outputName parameter
vectors = literal_eval(sys.stdin.read())
outputName = sys.argv[1]
modelLen = len(vectors[0][0])

#Check supported model and initialize image
if modelLen == 3:
    image = Image.new('RGB', (len(vectors[0]),len(vectors)))
elif modelLen == 4:
    image = Image.new('RGBA', (len(vectors[0]),len(vectors)))
else:
    print("Unsupported model")
    sys.exit(1)

#Map array values to image and save
pix = image.load()
for y in range(len(vectors)):
    for x in range(len(vectors[0])):
        r = int(round(vectors[y][x][0]))
        g = int(round(vectors[y][x][1]))
        b = int(round(vectors[y][x][2]))
        if modelLen == 3:
            pix[x,y] = (r,g,b)
        elif modelLen == 4:
            a = int(round(vectors[y][x][3]))
            pix[x,y] = (r,g,b,a)

image.save(outputName)

#Log
with open('log.txt', 'a+') as out:
    out.write(f"""**SAVING TO IMAGE {outputName}**\n\n""")