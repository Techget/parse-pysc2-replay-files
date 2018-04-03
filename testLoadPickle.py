import pickle
import pprint
import numpy

pp = pprint.PrettyPrinter(indent=4)
temp = pickle.load(open("data/da7d591b3776bec9597955dae31f10aae3ecd09f01b8b5b13a117e6591b931ee.p", "rb"))

print(temp.keys())

print(temp['info'])
print(len(temp['state']))
print(temp['state'][3])
temp2 = numpy.array(temp['state'][1]['minimap'][0])
print(temp2.shape)

print(len(temp['state'][1]['screen']))
temp3 = numpy.array(temp['state'][1]['minimap'][0])
print(temp3.shape)
