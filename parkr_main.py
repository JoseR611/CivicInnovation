import pandas as pd
import json
import numpy as np
from pprint import pprint
import itertools as it
from math import hypot

def dist(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return hypot(x2-x1,y2-y1)

def swap(a):
    x,y=a
    
    b=float(y),float(x)
    return (b)
 
#loading sampled files into python.
parking= json.load(open('parkingSummon.json'))
park=[]

#extracting only METER-OVERTIME and NO-PARKING violation from the set. 
for i in range(0, len(parking)):
    if(parking[i][3]=="NO PARKING" or parking[i][3]=="METER OVERTIME"):    
        park.append(parking[i])        

#getting the coardinates for the violations.
for i in range(0, len(park)):
        park[i][10]=float(park[i][10])
        park[i][11]=float(park[i][11])

lat=[]
long=[]
for i in range(0,len(park)):
    lat.append(park[i][10])
    long.append(park[i][11])
violation=(list (zip(lat,long)))

#getting meter's coordinates and converting into lats and longtitudes.
meter=[]
meters=json.load(open('meterOut.json'))
for i in range(0,len(meters)):
    coords = meters[i][17].replace('POINT (', '').replace(')','')
    meter.append(swap(coords.split(' ')))

#need more info for the streets like where can we park on the streets since not all locations on the streets can be used for parking. 
streets=json.load(open('streetInfo.json'))

#finding the nearest parking meter and distance from your "non-feasible" parking location. 
def find_nearest_meter(gps_pos):
    closest_meter=[]
#for i in range(0,len(violation)): 
    d=[]
    for j in range (0,len(meter)):
        d.append(dist(gps_pos,meter[j]))
    [m,i]=[min(d),d.index(min(d))]
    closest_meter=([m,meter[i]])
    return closest_meter

#gps location tracking and notifying in real time about the positions 
#actual gps location will be taken in the app.
gps_pos=[]
gps_pos=input("please enter you location in geocodes lat,long:")
gps_pos=gps_pos.split(',')

pos=(float(gps_pos[0]),float(gps_pos[1]))
if (pos in violation):
    print ("You are at a place where you have the highest chance of getting a ticket")
option=input("Suggestive Parking: 0 or 1")
if (option=='1' ):
    x=find_nearest_meter(pos)
    print ("here is a parking meter at ",x[1]," distance ",x[0],"m.")
    take=input("do you want to use it?")
    if (take=='1'):
        meter.remove(x[1]) #for 2 hours in the map. since each meter runs for 2hours.
        print ("okay marking you down for 2hours")
    





