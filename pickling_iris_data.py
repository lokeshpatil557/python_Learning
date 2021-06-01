import pickle
import requests

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
res = requests.get(url)
res_text = res.text
data = res_text.splitlines()
red = [[i] for i in data]
fileobj = open('irisdata.pkl', 'wb')
pickle.dump(red, fileobj)
fileobj.close()

fileobj1 = open('irisdata.pkl', 'rb')
data = pickle.load(fileobj1)
print(data)
