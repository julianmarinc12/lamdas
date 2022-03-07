
#python
from typing import Optional
from enum import Enum
#pydantic
from pydantic import BaseModel 
from pydantic import EmailStr
from pydantic import Field
#fastapi
from fastapi import UploadFile
from fastapi import Path
from fastapi import Header
from fastapi import Form
from fastapi import File
from fastapi import FastAPI
from fastapi import Cookie   
from fastapi import HTTPException
from fastapi import status
from fastapi import Query
from fastapi import Body

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

class PersonBase(BaseModel):
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

class Person (PersonBase):  
    password : str = Field(
        ...,
        min_length= 8,
        example = "julianmarinc"
    )

class PersonOut(PersonBase):
    pass

class LoginOut(BaseModel):
    username: str = Field(
        ...,
        min_lengt= 1,
        max_length= 20,
        example= "julian"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length= 20,
        example= "julianmarinc"
        
    )

@app.get(
    path="/",
     status_code=status.HTTP_200_OK,
    tags=["Inicio"]
    )
def home():
    return{"Hello":"word"}

#request and response body

@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"]
    )
def create_person(person: Person = Body(...)):
    """
    - create person

    - this path operation creates a person in the app y save the information in la dababase

    - parameterr:
      - Request body person:
        - **person : Person** -> a person model whit first name,last name, age, hair color and marital status
    - return a person model whit first name, last name, age , hair color and marital status

    """
    return person

#validation query parameters

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
  
    )
def show_person(
    name: Optional[str]=Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        example="julian"
        ),
    age: int =Query(
        ...,
        title="Person Age",
        description=" This is the person age. It's requered",
        example=26
        )
):
    return{name: age}

#validaciones: path Parameters

persons = [1,2,3,4]

@app.get(
    "/person/detail/{person_id}",
    tags=["Persons"]
    )
def show_person(
    person_id: int = Path(
        ...,
         gt=0,
         title="Person id",
         description="this is the person id. It's requered",
         example= 123
        
         )
):
    if person_id not in persons:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "!this person doesno't exist"
        )
    return {person_id:"it exists!"}

#validations :  request body
@app.put(
    "/person/{person_id}",
    tags=["Persons"]
    )
def update_person(
    person_id: int =Path(
        ...,
        title="person ID",
        description=" this is the person ID",
        gt =0,
        example= 123
    ),
    person: Person = Body(...),
    location:Location= Body(...)

):
    resultd = person.dict()
    resultd.update(location.dict())
    return resultd

#form   
@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
    )
def login(username: str=Form(...),password: str=Form(...)):
    
    return LoginOut(username=username,password=password)
   

#Cookies and headers parameters

@app.post(
    path = "/contact",
    status_code=status.HTTP_200_OK,
    tags=["contact"]
    
)
def contact(
    first_name: str = Form(
        ...,
        min_length=1,
        max_length=20,
        example = "julian"
    ),
    last_name: str = Form(
        ...,
        min_length=1,
        max_length=20,
        example= "marin"
    ),
    email: EmailStr = Form(
        ...,
        example="julian@email.com"
        ),
    message: str = Form(
        ...,
        min_length=20,
        example= "hola que mas pues vengo aqui buscandote"
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):

    return user_agent

#files
@app.post(
    path = "/post-image",
    tags=["image"]


)
def post_image(
    image: UploadFile = File(...)
):
    return{
        "filename": image.filename,
        "format":image.content_type,
        "size(kb)":round(len(image.file.read())/1024, ndigits=3)
    }