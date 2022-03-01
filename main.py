
#python

from typing import Optional
#pydantic
from pydantic import BaseModel

#fastapi
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

#models

class Person (BaseModel):
    firt_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return{"Hello":"word"}

#request and response body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

#validation query parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str]=Query(None,min_length=1,max_length=50),
    age: int =Query(...)
):
    return{name: age}

