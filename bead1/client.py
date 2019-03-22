#!/usr/bin/python
#beadando 1
import json
import subprocess
import sys


json_string1= """
{
	"date": "20190303",
	"system": "linux",
	"pings": [
				
			 ]
}
"""

data = json.loads(json_string1)

test = json.dumps(data)
#print(test)

with open(str(sys.argv[1]), 'r') as f:
	for line in f:
		line = line.rstrip('\n').split(',')[1]
		print(line)

		p = subprocess.Popen(["ping","-c",  "1", line], stdout= subprocess.PIPE)
		p.wait()

		data['pings'].append(({'target': line, 'output': p.communicate()[0]}))
		test = json.dumps(str(data))
		print(test)

with open ('ping.json', "w") as pings:
	pings.write(test)

print("ping.json DONE")
print("##############")

## tracert

json_string2= """
{
	"date": "20190303",
	"system": "linux",
	"tracers": [
				
			 ]
}
"""
data = json.loads(json_string2)
test = json.dumps(data)


with open(str(sys.argv[1]), 'r') as f:
	for line in f:
		line = line.rstrip('\n').split(',')[1]
		print(line)

		p = subprocess.Popen(["traceroute","-m",  "30", line], stdout= subprocess.PIPE)
		p.wait()

		data['tracers'].append(({'target': line, 'output': p.communicate()[0]}))
		test = json.dumps(str(data))
		print(test)

with open ('traceroute.json', "w") as pings:
	pings.write(test)

print("traceroute.json DONE")
