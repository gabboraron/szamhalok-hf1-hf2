#!/usr/bin/python
#beadando 2
import json
import subprocess
import sys
from pprint import pprint


with open(str(sys.argv[1]), 'r') as f:
	data = json.load(f)

#print("#####")
#pprint(data)
#print("#####")

possibleValues = ["sikeres", "sikertelen"]
pvIdx = 0

#print(len(data["simulation"]["demands"]))

occupiedNetworkPoints = []

routeID = 0
#return True if line is available
def isItAvailable(endPoints):
	tmpIdx = 0
	for pc in data["possible-circuits"]:									#searching the correct route id
		if((pc[0] == endPoints[0]) and (pc[len(pc)-1] == endPoints[1])):
			global routeID
			routeID = tmpIdx
			#print("LOG: isItAvailable: match: [" + str(pc[0]) + str(pc[len(pc)-1]) + "] with requested: [" + endPoints[0] + endPoints[1] + "]; tmpIdx: " + str(tmpIdx) + " routeID: " + str(routeID) )
			#get if route is occupied
			for onp in occupiedNetworkPoints:
				if (onp[0] == routeID):
					#print("LOG: isItAvailable: occupied points: " + str(occupiedNetworkPoints))
					#print("LOG: isItAvailable: occupied:        " + str(routeID))
					return False		#route is occupied
				#for point in 	#search points inside the 
			#print("LOG: isItAvailable: occupied points: " + str(occupiedNetworkPoints))
			#print("LOG: isItAvailable: available:       " + str(routeID))
			if contains(tmpIdx):
				return False
			return True					#route is unoccupied
		tmpIdx += 1

#get if the possible circoute route contains network points what are in already demanded network points
#return True if contains, False if not
def contains(neededRouteId):
	for onp in occupiedNetworkPoints:
		for point in data["possible-circuits"][onp[0]]:
			tmpIdx = 0
			for requestedPoint in data["possible-circuits"][neededRouteId]:
				if ((tmpIdx != 0)and(tmpIdx != len(data["possible-circuits"][neededRouteId])-1)):
					if (point == requestedPoint):
						return True
				tmpIdx += 1
	return False

#set occupied route to occupiedNetworkPoints list
def demandLine(demandId):
	global routeID
	occupiedNetworkPoints.append([routeID,demandId])	# [routeID,demandId] = [data[possible-circuits id], demanded route id from data[simulation][demands]]
	#print(str(occupiedNetworkPoints))

#refuse the occupied line
def refuseLine(demandId):
	#print(str(occupiedNetworkPoints))
	#print("felszabadítandó: " + str(demandId))
	tmpidx = 0
	for onp in occupiedNetworkPoints:		#searching the correct route id
		if (onp[1] == demandId):
			#tmp = [routeID,demandId]
			#occupiedNetworkPoints.remove(tmp)
			occupiedNetworkPoints.pop(tmpidx)
			return True
		tmpidx += 1


# idx = 0
# for pc in data["possible-circuits"]:
#  	print(idx)
#  	print(pc)
#  	print(len(pc))
#  	print(pc[len(pc)-1])
#  	idx += 1

idx = 0
dIdx = 0
for time in range(0,data["simulation"]["duration"]):
	for demand in data["simulation"]["demands"]:
		if (time == demand["start-time"]): 				#possible begining of demand
			if(isItAvailable(demand["end-points"])):	#deamand if available, refuse if it isn't
				demandLine(dIdx)
				print (str(idx+1) + " igeny foglalas:  \t" + str(demand["end-points"][0]) + "<->" + str(demand["end-points"][1]) + " st:" + str(demand["start-time"]) + " - " + str(possibleValues[0]))					
				#idx += 1
			else:
				print (str(idx+1) + " igeny foglalas:  \t" + str(demand["end-points"][0]) + "<->" + str(demand["end-points"][1]) + " st:" + str(demand["start-time"]) + " - " + str(possibleValues[1]))				
			idx += 1
		elif (time == demand["end-time"]): 				#possible end of demand
			if (refuseLine(dIdx)):
				print (str(idx+1) + " igeny felszabaditas:  " + str(demand["end-points"][0]) + "<->" + str(demand["end-points"][1]) + " st:" + str(demand["end-time"]))
			
			idx += 1
		dIdx += 1
	dIdx = 0
	#print("\n")

import os
os.system('spd-say "your program has finished"')


