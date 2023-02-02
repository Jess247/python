import json

data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
# info returns a list
info = json.loads(data)
print(info[1]['name'])

data2 = '''{
"name":"Jess",
"phone":{
"type":"intl",
"number":"+1 345 654 7693"
},
"email":{
"hide":"yes"
}
}'''

# info returns a dictionary
info = json.loads(data2)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
