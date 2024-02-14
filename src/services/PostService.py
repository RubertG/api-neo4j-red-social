from src.config.db import conexionDB
from src.schemas.PostSchema import SchemaPost
from src.services.UserService import obtenerUsuario
import uuid
from fastapi import HTTPException

def obtener():
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Post) RETURN n"
        results = session.run(query)
        return results.value()
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def crear(post: SchemaPost):
    try:
        post.id = uuid.uuid4().hex
        driver = conexionDB()
        session = driver.session()
        query = """
        CREATE (n: Post { id: $id, contenido: $contenido, usuario_id: $usuario_id })
        WITH n
        MATCH (u:Usuario {id: $usuario_id})
        CREATE (u)-[:CREA]->(n)
        """
        obtenerUsuario(post.usuario_id)
        session.run(query, id=post.id, contenido=post.contenido, usuario_id=post.usuario_id)
        return { "message": "Post creado", "body": post }
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerPorID(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (p:Post {id: $id}) RETURN p"
        results = session.run(query, id=id)
        data = results.value()
        if (data == []):
            raise HTTPException(status_code=404, detail=f"El post con id '{id}' no existe")
        return data[0]
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerPost(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (p:Post {id: $id}) RETURN p"
        results = session.run(query, id=id)
        data = results.value()
        if (data == []):
            raise HTTPException(status_code=404, detail=f"El post con id '{id}' no existe")
        return data[0]
    finally:
        driver.close()

def eliminarPorID(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (p:Post {id: $id}) DETACH DELETE p"
        obtenerPost(id)  # Verificar existencia antes de eliminar
        session.run(query, id=id)
        return { "message": "Post eliminado" }
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerPorUsuario(usuario_id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = """
        MATCH (p:Post)<-[:CREA]-(u:Usuario {id: $usuario_id})
        RETURN p
        """
        obtenerUsuario(usuario_id) 
        results = session.run(query, usuario_id=usuario_id)
        return results.value()
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def actualizar(id: str, post: SchemaPost):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (p:Post {id: $id}) SET p.contenido = $contenido"
        obtenerPost(id)  # Verificar existencia antes de actualizar
        results = session.run(query, id=id, contenido=post.contenido)
        return results.value()
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()