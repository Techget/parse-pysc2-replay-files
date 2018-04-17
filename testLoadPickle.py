import pickle
import pprint
import numpy

pp = pprint.PrettyPrinter(indent=4)

filename = "fce8134bc5edf4fff731fefccd6e78dcc11006c035def9d0ae9ecd63f9fe7267.p"
temp = pickle.load(open("data_64/"+filename, "rb"))

print(temp.keys())

print(temp['info'])
#print('#####')
#for pi in temp['info'].player_info:
#	print('###',pi)



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
while i < len(temp['state']):
	if temp['state'][i]['actions'] != []:
		print((numpy.array(temp['state'][i]['minimap'])).shape)

		print(temp['state'][i]['actions'])
#		break
	i+=1


