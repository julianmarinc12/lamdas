
#python

from typing import Optional
#pydantic
from pydantic import BaseModel

#fastapi
from fastapi import FastAPI
from fastapi import Body

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