
import csv
import requests
from json import dumps

import time
timestamp = time.strftime("%d-%m-%y -- %H-%M-%S")

cell_ID_data_file_read = open('PATH Of Cell ID FILE','rb') #Enter the path of the file containing Cell IDs and LAC
cell_ID_data_file_reader = csv.reader(cell_ID_data_file_read)
cell_ID_data_file_headers = cell_ID_data_file_reader.next()

cell_ID_loc_file_write = open('PATH For OUTPUT FILE '+timestamp+'.csv','wb') #Enter the path where outpt file would be generated
cell_ID_loc_file_writer = csv.writer(cell_ID_loc_file_write)
cell_ID_loc_file_writer.writerow(["Cell ID", "LAC", "Latitude-LAPI","Longitude-LAPI","Latitude-CPT","Longitude-CPT"])

request_url_LAPI = 'http://unwiredlabs.com/v2/process.php'
request_url_CPT = 'http://cellphonetrackers.org/gsm/gsm-tracker.php'

for rows in cell_ID_data_file_reader:
	parameters_LAPI = {
		'token': TOKEN, #API Token from Location API
		'mcc': MCC, #Enter the value of MCC
		'mnc': MNC, #Enter the value of MNC
		'cells': [{'cid': rows[0], 'lac': rows[1]}]}
	parameters_CPT = {
		'mcc': MCC, #Enter the value of MCC
		'mnc': MNC, #Enter the value of MNC
		'cid': rows[0], 
		'lac': rows[1]}

	url_response_LAPI = requests.post(request_url_LAPI, data=dumps(parameters_LAPI), headers={'content-type': 'application/json'})
	url_output_LAPI_json = url_response_LAPI.json()

	url_response_CPT = requests.post(request_url_CPT, data=parameters_CPT)

	if url_output_LAPI_json.get('status') == 'ok':
		latitude_LAPI = '{lat}'.format(**url_output_LAPI_json)
		longitude_LAPI = '{lon}'.format(**url_output_LAPI_json)
#		print latitude_LAPI, longitude_LAPI
	else:
		latitude_LAPI = '0'
		longitude_LAPI = '0'

	if url_response_CPT.content.find('Lat=') != -1: 
		latitude_CPT = url_response_CPT.content[url_response_CPT.content.find('Lat=')+4:url_response_CPT.content.find(' ', url_response_CPT.content.find('Lat='))]
		longitude_CPT = url_response_CPT.content[url_response_CPT.content.find('Lon=')+4:url_response_CPT.content.find('<', url_response_CPT.content.find('Lon='))]
#		print latitude_CPT, longitude_CPT
	else:
		latitude_CPT = '0'
		longitude_CPT = '0'

	print rows[0], rows[1], latitude_LAPI, longitude_LAPI, latitude_CPT, longitude_CPT	
	cell_ID_loc_file_writer.writerow([rows[0], rows[1], latitude_LAPI, longitude_LAPI, latitude_CPT, longitude_CPT])

cell_ID_data_file_read.close()
cell_ID_loc_file_write.close()

