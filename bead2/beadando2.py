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
	# for point in endPoints:
	# 	for occupiedPoint in occupiedNetworkPoints:
	# 		if (point == occupiedPoint):
	# 			return False
	# return True
	tmpIdx = 0
	for pc in data["possible-circuits"]:									#searching the correct route id
		if((pc[0] == endPoints[0]) and (pc[len(pc)-1] == endPoints[1])):
			global routeID
			routeID = tmpIdx
			#print("LOG: isItAvailable: match: [" + str(pc[0]) + str(pc[len(pc)-1]) + "] with requested: [" + endPoints[0] + endPoints[1] + "]; tmpIdx: " + str(tmpIdx) + " routeID: " + str(routeID) )
			#get if route is occupied
			for onp in occupiedNetworkPoints:
				if (onp == routeID):
					print("LOG: isItAvailable: occupied points: " + str(occupiedNetworkPoints))
					print("LOG: isItAvailable: occupied:        " + str(routeID))
					return False		#route is occupied
				#for point in 	#search points inside the 
			print("LOG: isItAvailable: occupied points: " + str(occupiedNetworkPoints))
			print("LOG: isItAvailable: available:       " + str(routeID))
			return True					#route is unoccupied
		tmpIdx += 1


#set occupied route to occupiedNetworkPoints list
def demandLine(endPoints):
	#for point in endPoints:
	#	occupiedNetworkPoints.append(point)
	
	occupiedNetworkPoints.append(routeID)
	global routeID
	#print("LOG: demandline: routeID: " + str(routeID))
	#print("LOG: demandline: updated occupiedpointlist: " + str(occupiedNetworkPoints))



#refuse the occupied line
def refuseLine(endPoints):
	#for point in endPoints:
	#	occupiedNetworkPoints.remove(point)	
	tmpIdx = 0
	for pc in data["possible-circuits"]:									#searching the correct route id
		if((pc[0] == endPoints[0]) and (pc[len(pc)-1] == endPoints[1])):
			global routeID
			routeID = tmpIdx
			#get if route is occupied
			#print("LOG: refuseLine: updated occupiedpointlist: " + str(occupiedNetworkPoints))
			occupiedNetworkPoints.remove(routeID)
			#print("LOG: refuseLine: line refused!")
			return

			#return True
		tmpIdx += 1


idx = 0
for pc in data["possible-circuits"]:
 	print(idx)
 	print(pc)
 	print(len(pc))
 	print(pc[len(pc)-1])
 	idx += 1

idx = 0
for time in range(0,data["simulation"]["duration"]):
	for demand in data["simulation"]["demands"]:
		if (time == demand["start-time"]): 				#possible begining of demand
			if(isItAvailable(demand["end-points"])):	#deamand if available, refuse if it isn't
				demandLine(demand["end-points"])
				print (str(idx+1) + " igeny foglalas:  " + str(demand["end-points"][0]) + "<->" + str(demand["end-points"][1]) + " st:" + str(demand["start-time"]) + " - " + str(possibleValues[0]))					
				idx += 1
			else:
				print (str(idx+1) + " igeny foglalas:  " + str(demand["end-points"][0]) + "<->" + str(demand["end-points"][1]) + " st:" + str(demand["start-time"]) + " - " + str(possibleValues[1]))				
				idx += 1
		elif (time == demand["end-time"]): 				#possible end of demand
			print (str(idx+1) + " igeny felszabaditas:  " + str(demand["end-points"][0]) + "<->" + str(demand["end-points"][1]) + " st:" + str(demand["start-time"]))
			refuseLine(demand["end-points"])
			idx += 1
	print("\n")

import os
os.system('spd-say "your program has finished"')


