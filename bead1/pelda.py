import json

json_string= """
{
	"researcher": {
		"name": "Ford Prefect",
		"species": "Betelgeusian",
		"relatives": [
			{
				"name": "Zaphod Beeblebrox",
				"species": "Betelgeusian"
			}
		]
	}
}
"""
data = json.loads(json_string)

#data["researcher"]["second"]["user"] = "Bela"
#iter(data).next()['f'] = "alma"
#data["researcher"].append({'b':'2'})

#for rel in data["researcher"]["relatives"]:
#	print('Name: %s (%s)' % ( rel["name"], rel["species"] ) )

test = json.dumps(data)
print(test)

data['researcher']['relatives'].append(({'a': 'aaaa', 'b': 'aaaa', 'c': 'aaaa'}))
test = json.dumps(data)
print(test)