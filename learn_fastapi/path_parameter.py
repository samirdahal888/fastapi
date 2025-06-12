from fastapi import FastAPI,Path,HTTPException
import json

app = FastAPI()
# just loading the data from patient.json
def load_data():
    with open("patient.json",'r') as f:
        data = json.load(f)
    return data

@app.get('/view/{Patient_id}') # here Patient_id is the path parameter we get it dynamically we can change it anytime
def view_particular_patient(Patient_id= Path(description="Patient id ",example=['P001'])) : # the value we got in our api can be directly accessible to the function like this
    # we acn use path parameter in the same place where we recive it in the function by doing =
    data = load_data()
    if Patient_id in data:
        return data[Patient_id] #since  our data is json and have patient id key , we can do this to get the particular patient
    raise HTTPException(status_code= 400,detail='patient not found') # like this we use http exception

