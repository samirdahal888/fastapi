from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description='Id of the patient',examples=['P001'])]
    name:Annotated[str,Field(...,description='Name of the patient')]
    city:Annotated[str,Field(...,description='City of the patient')]
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender:Annotated[Literal['male','femal','Others'],Field(...,description='Gender of the patient')]
    height:Annotated[float,Field(...,gt= 0,description='Height of the patient')]
    weight:Annotated[float,Field(...,gt=0,description='weight of patient')]


    @computed_field(return_type=float)
    @property
    def bmi(self):
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field(return_type=str)
    @property
    def verdict(self):
        if self.bmi <18.5:
            return 'Underweight'
        elif self.bmi <25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return'obis'
        

    




def load_data():
    with open('patient.json','r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patient.json','w') as f:
        json.dump(data,f)

@app.get('/view')
def view_patients():
    data = load_data()
    return data

@app.get('/patient/{id}')
def get_patient_by_id(id:str):


    data = load_data()

    return data[id]

@app.post('/create')
def create_patient(patient:Patient):
    #load data
    data = load_data()


    # check if the patient already exist
    if patient.id in data:
        raise HTTPException(status_code=400,detail='patient already exist')

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save to the json file
    save_data(data)

    return JSONResponse(status_code=201,content={'message':'patient created successfully'})







 


