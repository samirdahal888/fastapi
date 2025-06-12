import json
with open('/home/samir-dahal/fastapi/learn_fastapi/patient.json','r') as f:
    data = json.load(f)
    print(data['P001'])




