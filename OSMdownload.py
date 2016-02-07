print "-- OSM download py --"

import os
import math
import urllib

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return xtile, ytile

def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  return (lat_deg, lon_deg)


def createDir(tilezoom,xtile):
  directory = str(tilezoom) + "/" + str(xtile)
  if not os.path.exists(directory):
    os.makedirs(directory)
    print "dir " + directory + " created"


def downloadTiles(x,y,tilezoom):

  tile = deg2num(x,y,tilezoom)
  maptype = "mapbox.streets/" # or: mapbox.satellite/ mapbox.streets-satellite ... (mapbox doc)
  xtile = tile[0]
  ytile = tile[1]

  if tilezoom < 10:
    for x in range(xtile-2,xtile+4):
      #print x
      createDir(tilezoom,x)
      for y in range(ytile-1,ytile+2):
        #print y
        tilenr = str(tilezoom) + "/" + str(x) + "/" + str(y)
        pngurl = "https://api.tiles.mapbox.com/v4/" + maptype + tilenr +".png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw"
        urllib.urlretrieve(pngurl, tilenr+".png")
        print 'tile ' + tilenr + " downloaded"
  else:
    for x in range(xtile-tilezoom,xtile+tilezoom):
      #print x
      createDir(tilezoom,x)
      for y in range(ytile-tilezoom,ytile+tilezoom):
        #print y
        tilenr = str(tilezoom) + "/" + str(x) + "/" + str(y)
        pngurl = "https://api.tiles.mapbox.com/v4/" + maptype + tilenr +".png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw"
        urllib.urlretrieve(pngurl, tilenr+".png")
        print 'tile ' + tilenr + " downloaded"

'''
if tilezoom < 10:
  ...
elif tilezoom < 15:
  ...
else:
  ...
  
'''

#downloadTiles(6)

# warsaw shore
for num in range(6,19):
  x = 52.23
  y = 21.01
  print "-- downloading tiles for (" + str(x) + ", " + str(y) +") ..."
  print "tilezoom: " + str(num)
  downloadTiles(x,y,num)

''' 
eventually add other cracow x = 50.06 y = 19.94 whitestock x = 53.13 y = 23.15 meeting place  x = 52.41 y = 16.93 wroclove x = 51.11 y = 17.03
'''

