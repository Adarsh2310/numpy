import json

'''with open('sample2.json') as json_file:
    data = json.load(json_file)
    print(data)
    json_object = json.dumps(data, indent = 4)
    print(json_object)
    print(type(json_object))
    print(data.keys())
f=open('learn.json')
data=json.load(f)
print(data)'''

with open('learn.json') as json_file:
    '''data = json.load(json_file)
    print(data)
    print(type(data))
    json_object = json.dumps(data)
    print(json_object)
    print(json_object["name"])'''
    data=json.load(json_file)
    print(data)
    for i in data:
        print(i['name'])



