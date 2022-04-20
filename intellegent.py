import json
with open("Agent.json","r")as f:
    content =json.loads(f.read())
    print (content["Temperature degree"])
    if (int(content["Temperature degree"]["value"]) == 710):

      print("درجة الحرارة مرتفعة الرجاء الهبوط في مدة لاتتجاوز 15 دقيقة")
      Extinguishing={
          "name ":"Extinguishing system ",
          "value" : 1
      }
      with open("Extinguishing.json", "w")as write_file:
          json.dump(Extinguishing,write_file)


    print(content["landing gear light"])
    if (str (content["landing gear light"]["value"]) == 'red'):
        print("لقد فشل انزال الاطارارات ")
        hydraulic = {
            "name ": "The hydraulic system ",
            "value": 1
        }
        with open("hydraulic.json", "w")as write_file:
            json.dump(hydraulic, write_file)
    print(content["the height"])
    if (int(content["the height"]["value"]) <= 4000):
        print("سيتم تذويد الطائرة بالاوكسجين من الجو")
        oxegen = {
            "name ": "Oxygen cylinder ",
            "value":"0%"
        }
        with open("oxegen.json", "w")as write_file:
            json.dump(oxegen, write_file)
    elif(int(content["the height"]["value"]) == 5000):
      print("سيتم تذويد الطائرة باوكسجين مخلوط")
      oxegen = {
            "name ": "Oxygen cylinder ",
            "value":"50%"
      }
      with open("oxegen.json", "w")as write_file:
           json.dump(oxegen, write_file)
    else :
      print("سيتم تذويد الطائرة باوكسجين صافي من الاسطوانة")
      oxegen = {
        "name ": "Oxygen cylinder ",
        "value": "100%"
      }
      with open("oxegen.json", "w")as write_file:
         json.dump(oxegen, write_file)
