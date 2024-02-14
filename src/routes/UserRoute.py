from fastapi import APIRouter
from src.schemas.UserSchema import SchemaUsuario
from src.services.UserService import (
    obtener,
    crear,
    obtenerUsuario,
    eliminarPorID,
    actualizar
)

Route = APIRouter()

@Route.get("/")
def obtenerTodos():
    return obtener()

@Route.get("/{id}")
def obteneUser(id: str):
    return obtenerUsuario(id)
    
@Route.post("/")
def creaUser(user: SchemaUsuario):
    return crear(user)

@Route.delete("/{id}")
def eliminaUser(id: str):
    return eliminarPorID(id)

@Route.put("/actualizar/{id}")
def actualizaUser(id: str, user: SchemaUsuario):
    return actualizar(id, user)