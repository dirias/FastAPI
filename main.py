#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return {"Hello": "Word"}

#Request and response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return Person
#Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_lenght=1,
        mac_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 to 50 characters"
        ),
    age: str = Query(
        ...,
        title="Person age",
        description= "This is the person name. It's requried"
        )
    ):
    return {name: age}

#Validaciones: Path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="This is the person ID. IT's requried"
        )
    ):
    return {person_id: "created"}
