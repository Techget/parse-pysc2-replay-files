import pickle
import pprint
import numpy
from google.protobuf.json_format import MessageToJson
import json

pp = pprint.PrettyPrinter(indent=4)

#filename = "fce8134bc5edf4fff731fefccd6e78dcc11006c035def9d0ae9ecd63f9fe7267.p"
#filename = "fefa9e6630216c279f8a5a371bea283f091244452f77306376feadba7314b00f.p"
#filename = "2e3b9605f05053390d59ca132893b0210ece353b991c12d62cab9193dd4a9bed.p"
#filename = "7ab0c4728b61cb9fa800dd27691d2f8e673b49a94aa6f01261e5fc7c15cb3619.p"
filename = "ff0b0467698a1cf727e170ef1409737049cd7d666259811c45a9f58b2a06ab3a.p"
temp = pickle.load(open("data_full/"+filename, "rb"))

print(temp.keys())

loaded_replay_info_json = MessageToJson(temp['info'])
info_dict = json.loads(loaded_replay_info_json)
print(info_dict)

print(type(loaded_replay_info_json))
for pi in info_dict['playerInfo']:
	print(pi['playerResult']['result'])



#print(temp['info'])
#print('#####')
#for pi in temp['info'].player_info:
#	print('###',pi)

#for pi in temp['info'].player_info:
#	print(pi.player_result['Result'])

#print(len(temp['state']))
#print(temp['state'][100])

#temp2 = numpy.array(temp['state'][1]['minimap'][0])
#print(temp2.shape)
#temp2 = numpy.array(temp['state'][1]['minimap'][4])
#print(temp2.shape)

#print(len(temp['state'][1]['screen']))
#temp3 = numpy.array(temp['state'][1]['minimap'][0])
#print(temp3.shape)

#temp2 = numpy.array(temp['state'][1]['screen'])
#print(temp2.shape)

i = 0
counter = 0
while i < len(temp['state']):
	if temp['state'][i]['actions'] != []:
#		print((numpy.array(temp['state'][i]['minimap'])).shape)

		print(temp['state'][i])

#		for a in temp['state'][i]['actions']:
#			if a[1] == 'select_control_group':
#				print(a)
#				print(temp['state'][i])

		counter += len(temp['state'][i]['actions'])
#		print(temp['state'][i])
		break
	i+=1

print(counter)
