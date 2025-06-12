from fastapi import FastAPI,HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open("patient.json",'r')as f:
        data = json.load(f)

    return data


@app.get('/patient') # for query parametr we dont have to  write it in api
def patients(filer_by = Query(description= 'filter by name',example='samir')): # directly we access here 
    name_query = filer_by.lower()
    data = load_data()
    # Filter entries where the name contains the query
    filtered = {
        pid: details for pid, details in data.items()
        if name_query in details["name"].lower()
    }
    return filtered




