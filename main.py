
#python

from typing import Optional
from enum import Enum
#pydantic
from pydantic import BaseModel, Field

#fastapi
from fastapi import FastAPI, Path
from fastapi import Body, Query

app = FastAPI()

#models
class HairColor(Enum):
    white = "white"
    browm = "browm"
    black ="black"
    blonde ="blonde"
    red = "red"

class Location(BaseModel):
    city: str =Field(
        min_length= 1,
        max_length= 50,
        example = "Medellin"
    )
    state:str = Field(
        min_length= 1,
        max_length= 50,
        example = "Antioquia"
    )
    country:str = Field(
        min_length= 1,
        max_length= 50,
        example = "Colombia"
    )



class Person (BaseModel):
    firt_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example ="julian")
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example = "marin")
    age: int = Field(
        ...,
        gt = 1,
        le= 115,
        example =25
    )
    hair_color: Optional[HairColor] = Field(default= None, example="black")
    is_married: Optional[bool] = Field(default=None, example = False)


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
    name: Optional[str]=Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
        ),
    age: int =Query(
        ...,
        title="Person Age",
        description=" This is the person age. It's requered"
        )
):
    return{name: age}

#validaciones: path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
         gt=0,
         title="Person id",
         description="this is the person id. It's requered"
         )
):
    return {person_id:"it exists!"}

#validations :  request body
@app.put("/person/{person_id}")
def update_person(
    person_id: int =Path(
        ...,
        title="person ID",
        description=" this is the person ID",
        gt =0
    ),
    person: Person = Body(...),
    location:Location= Body(...)

):
    resultd = person.dict()
    resultd.update(location.dict())
    return resultd
    
