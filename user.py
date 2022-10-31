from fastapi import APIRouter
from config.db import conn
from model.index import users
from schema.index import User

user = APIRouter

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(user.c.id==id)).fetchall()

@user.post("/")
async def write_data(users:User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        passward=user.passward
    ))

@user.get("{id}")
async def update_data(id: int, users:User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        passward=user.passward
    ).where(users.c.id==id)

    return conn.execute(users.select()).fetchall()

@user.get("/")
async def delete_data():
    conn.execute(users.delete())
    return conn.execute(users.select()).fetchall()