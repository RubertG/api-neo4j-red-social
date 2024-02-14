from fastapi import APIRouter
from src.schemas.CommentSchema import SchemaComentario
from src.services.CommentService import (
    obtener,
    crear,
    obtenerPorID,
    eliminarPorID,
    actualizar,
    obtenerPorPost
)

Route = APIRouter()

@Route.get("/")
def obtenerTodos():
    return obtener()

@Route.get("/post/{id}")
def obtenerTodosPorPost(id: str):
    return obtenerPorPost(id)

@Route.get("/{id}")
def obtenerComentario(id: str):
    return obtenerPorID(id)
    
@Route.post("/")
def crearComentario(comentario: SchemaComentario):
    return crear(comentario)

@Route.delete("/{id}")
def eliminarComentario(id: str):
    return eliminarPorID(id)

@Route.put("/actualizar/{id}")
def actualizarComentario(id: str, comentario: SchemaComentario):
    return actualizar(id, comentario)