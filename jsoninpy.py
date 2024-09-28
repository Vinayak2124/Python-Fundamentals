# JSON -> Javascript Object Notation -> it is text
# It is mainly used for storing and transferring the data between the browser and server
# it is used in API . API uses json format 

# It supports 6 datatype : str,number,bool,null,obj,arr

import json

d = {
    'name' : 'vinayak',
    'language' : 'Python'
}
f = json.dumps(d)

print(f)
print(type(f))

# convert json to Python object

dic = '{"cname":"Python", "fees":2233, "Duration":"1 month"}'

x = json.loads(dic)
print(x)
print(type(x))

# read and write in JSON file :


file = open("file.json","r")
r = file.read()
data = json.loads(r)

print(data)
