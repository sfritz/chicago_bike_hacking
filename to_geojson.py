import csv
import json

geojson = {
	'type': 'FeatureCollection',
}
features = []
with open('BL_Current_Active.csv', 'rb') as csvfile:
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
with open('active_business_licenses.2015-04-28.geojson', 'w') as geojsonfile:
	geojsonfile.write(json.dumps(geojson))

