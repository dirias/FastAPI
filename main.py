#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

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
    name: Optional[str] = Query(None, min_lenght=1, mac_length=50),
    age: Optional[str] = Query(...)):
    return {name: age}
