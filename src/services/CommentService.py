from src.config.db import conexionDB
from src.services.UserService import obtenerUsuario
from src.services.PostService import obtenerPost
from src.schemas.CommentSchema import SchemaComentario
import uuid
from fastapi import HTTPException

def obtener():
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Comentario) RETURN n"
        results = session.run(query)
        return results.value()
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def crear(comentario: SchemaComentario):
    try:
        comentario.id = uuid.uuid4().hex
        driver = conexionDB()
        session = driver.session()
        query = """
        CREATE (c: Comentario { id: $id, contenido: $contenido, usuario_id: $usuario_id, post_id: $post_id })
        WITH c
        MATCH (p:Post {id: $post_id})
        CREATE (c)-[:EN_RESPUESTA_A]->(p)
        WITH c
        MATCH (u:Usuario {id: $usuario_id})
        CREATE (u)-[:COMENTA]->(c)
        """
        obtenerPost(comentario.post_id)
        obtenerUsuario(comentario.usuario_id)
        session.run(query, id=comentario.id, contenido=comentario.contenido, usuario_id=comentario.usuario_id, post_id=comentario.post_id)
        return { "message": "Comentario creado", "body": comentario }
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerPorID(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (c:Comentario {id: $id}) RETURN c"
        results = session.run(query, id=id)
        data = results.value()
        if (data == []):
            raise HTTPException(status_code=404, detail=f"El comentario con id '{id}' no existe")
        return data[0]
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerComment(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (c:Comentario {id: $id}) RETURN c"
        results = session.run(query, id=id)
        data = results.value()
        if (data == []):
            raise HTTPException(status_code=404, detail=f"El comentario con id '{id}' no existe")
        return data
    finally:
        driver.close()

def eliminarPorID(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (c:Comentario {id: $id}) DETACH DELETE c"
        obtenerComment(id)  # Verificar existencia antes de eliminar
        session.run(query, id=id)
        return { "message": "Comentario eliminado" }
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerPorPost(post_id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = """
        MATCH (p:Post {id: $post_id})<-[:EN_RESPUESTA_A]-(c:Comentario)
        RETURN c
        """
        obtenerPost(post_id)  # Verificar existencia del Post antes de buscar comentarios
        results = session.run(query, post_id=post_id)
        return results.value()
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()
        
def actualizar(id: str, comentario: SchemaComentario):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (c:Comentario {id: $id}) SET c.contenido = $contenido"
        obtenerComment(id)  # Verificar existencia antes de actualizar
        results = session.run(query, id=id, contenido=comentario.contenido)
        return results.value()
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
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()