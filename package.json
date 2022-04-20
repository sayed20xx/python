import json
dictionary ={}
while True :
  name = input("Name: ")
  value = input("Value: ")
  dictionary[name] ={"name":name,"value":value}
  con =input("continue: ")
  if con.lower() == "y":
    continue
  else:
    break
s=json.dumps(dictionary)
with open("Agent.json","w")as f:
  f.write(s)
