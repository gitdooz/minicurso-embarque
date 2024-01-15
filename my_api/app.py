from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
database = []


class Events(BaseModel):
    nome: str
    dono: str
    desc: str
    data: str
    quant_ingressos: int
    foi_vendid: bool
    data_validade: str


@app.get('/')
async def hello_world() -> str:
    return 'Hello World!\nSou linde'


@app.post('/event', response_model=Events)
async def criar_evento(event: Events):
    database.append(event)

    return event


@app.get('/event')
async def ler_todos_os_eventos() -> List:
    return database
