
#python


from typing import Optional
#pydantic
from pydantic import BaseModel

#fastapi
from fastapi import FastAPI, Path
from fastapi import Body, Query

app = FastAPI()

#models
class Location(BaseModel):
    city: str
    state:str
    country:str



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



