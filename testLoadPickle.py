import pickle
import pprint
import numpy

pp = pprint.PrettyPrinter(indent=4)
temp = pickle.load(open("data/fcd6aab6918535c794ca42a08c3bfaa465e04b07bd2511866f68e14dc5c95b65.p", "rb"))

print(temp.keys())

print(temp['info'])
print(len(temp['state']))
#print(temp['state'][100])
#temp2 = numpy.array(temp['state'][1]['minimap'][0])
#print(temp2.shape)
#temp2 = numpy.array(temp['state'][1]['minimap'][4])
#print(temp2.shape)

#print(len(temp['state'][1]['screen']))
#temp3 = numpy.array(temp['state'][1]['minimap'][0])
#print(temp3.shape)

temp2 = numpy.array(temp['state'][1]['screen'][0])
print(temp2.shape)


i = 0
while i < len(temp['state']):
	if temp['state'][i]['actions'] != []:
		print(temp['state'][i])
		break
	i+=1


