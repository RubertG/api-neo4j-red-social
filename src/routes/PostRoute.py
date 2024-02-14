from fastapi import APIRouter
from src.schemas.PostSchema import SchemaPost
from src.services.PostService import (
    obtener,
    crear,
    obtenerPorID,
    eliminarPorID,
    actualizar,
    obtenerPorUsuario
)

Route = APIRouter()

@Route.get("/")
def obtenerTodos():
    return obtener()

@Route.get("/usuario/{id}")
def obtenerTodosPorUsuario(id: str):
    return obtenerPorUsuario(id)

@Route.get("/{id}")
def obtenerPost(id: str):
    return obtenerPorID(id)
    
@Route.post("/")
def crearPost(post: SchemaPost):
    return crear(post)

@Route.delete("/{id}")
def eliminarPost(id: str):
    return eliminarPorID(id)

@Route.put("/actualizar/{id}")
def actualizarPost(id: str, post: SchemaPost):
    return actualizar(id, post)