import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows


@app.get("/superheroesMarvel")
def get_superheroes_marvel():
    rows = ["Spider-Man", "Iron Man", "Thor", "Hulk", "Black Widow", "Doctor Strange", "Black Panther", "Captain America"]
    return rows


app.get("/cursosPlazit")
def get_cursos_plazit():
    rows = ["Python", "JavaScript", "Java", "C#", "Ruby", "Go", "Swift", "Kotlin"]
    return rows