import pickle
import pprint
pp = pprint.PrettyPrinter(indent=4)
temp = pickle.load(open("data/016fec95a4114371c51e098bdc8f5b3b59ac391afc1b174d948883b74740379c.p", "rb"))

print(temp.keys())

print(temp['info'])
print(temp['state'])
