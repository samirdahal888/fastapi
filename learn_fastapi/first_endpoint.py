# Lets cerate faskapi simple app
from fastapi import FastAPI

#we have to make the instance of FastApi class to use its functionality, only then we can define the routes

app = FastAPI()

#this bellow line is the line we are making the API
@app.get('/') # we are using our instace to define the endpoint / we have to do like this to define the end points ( use as a decorator)
def hello(): # this is the backend logic ( so here we are making api and backend at the same time)
    return 'hii'


# to run this we have to do 
# uvicon filename:objectname --reload (reload helps to automaticaly reload the server when something is changes)