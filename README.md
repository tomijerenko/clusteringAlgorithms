# Files
   0_read.py - reads image and outputs its pixel values as vector array
   
   0_kmeans.py - reads vector array, performs k-means and outputs vector array
   
   0_dbscan.py - reads vector array, performs dbscan and outputs vector array
   
   0_save.py - reads vector array and generates an image
   
   log.txt - contains clustering information for pictures

# Dependencies
   All packages/libraries should be included in Python 3.6.8

# Limitations
   Image generation with 0_save.py works only for 3 or 4 channel models i.e. RGB (.jpg) or RGBA (.png)

# Format
   k-means and dbscan use following format string (string of 3 dimensional array of size [x,y,n]):
   
    [[[n0,n1,n2,...],[n0,n1,n2,...]],[[n0,n1,n2,...],[n0,n1,n2,...]],...]

# Usage
## k-means
    python3 0_read.py <inputImageName> | python3 0_kmeans.py <k-value> | python3 0_save.py <outputImageName>
   
## dbscan
   Parameter "distanceFunction" uses only "e" for euclidean distance or "m" for maximum distance
   
    python3 0_read.py <inputImageName> | python3 0_dbscan.py <eps> <minPts> <distanceFunction> | python3 0_save.py <outputImageName>

# Examples
## k-means
    python3 0_read.py 1_butterfly.jpg | python3 0_kmeans.py 2 | python3 0_save.py 2_butterfly2means.jpg
    python3 0_read.py 1_butterfly.jpg | python3 0_kmeans.py 5 | python3 0_save.py 2_butterfly5means.jpg

    python3 0_read.py 1_pug.jpg | python3 0_kmeans.py 2 | python3 0_save.py 2_pug2means.jpg
    python3 0_read.py 1_pug.jpg | python3 0_kmeans.py 5 | python3 0_save.py 2_pug5means.jpg

    python3 0_read.py 1_cat.jpg | python3 0_kmeans.py 2 | python3 0_save.py 2_cat2means.jpg
    python3 0_read.py 1_cat.jpg | python3 0_kmeans.py 5 | python3 0_save.py 2_cat5means.jpg

## dbscan
    python3 0_read.py 1_butterflySmaller.jpg | python3 0_dbscan.py 100 100 e | python3 0_save.py 2_butterfly_dbscan_100_100_e.jpg
    python3 0_read.py 1_butterflySmaller.jpg | python3 0_dbscan.py 100 100 m | python3 0_save.py 2_butterfly_dbscan_100_100_m.jpg

    python3 0_read.py 1_pugSmaller.jpg | python3 0_dbscan.py 100 100 e | python3 0_save.py 2_pugSmaller_dbscan_100_100_e.jpg
    python3 0_read.py 1_pugSmaller.jpg | python3 0_dbscan.py 100 100 m | python3 0_save.py 2_pugSmaller_dbscan_100_100_m.jpg

    python3 0_read.py 1_catSmaller.jpg | python3 0_dbscan.py 100 100 e | python3 0_save.py 2_catSmaller_dbscan_100_100_e.jpg
    python3 0_read.py 1_catSmaller.jpg | python3 0_dbscan.py 100 100 m | python3 0_save.py 2_catSmaller_dbscan_100_100_m.jpg

# Copyright
   All the images were taken from internet and therefore belong to their respective owners.
   
   Algorithms were not invented by me, I merely just implemented them.
