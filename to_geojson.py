import csv 
import json

geojson = {
	'type': 'FeatureCollection',
}
features = []
csvfile = open('BL_Current_Active.csv', 'rb')
reader = csv.DictReader(csvfile)
for row in reader:
	f = {
		'type': 'feature',
		'properties': row,
		'geometry': {
			'type': 'Point',
			'coordinates': [ row['Longitude'], row['Latitude'] ]
		}
	}
	features.append(f)


geojson['features'] = features
print json.dumps(geojson)
