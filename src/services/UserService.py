from src.config.db import conexionDB
from src.schemas.UserSchema import SchemaUsuario
import uuid
from fastapi import HTTPException

def obtener():
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Usuario) RETURN n"
        results = session.run(query)
        return results.value()
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def crear(usuario: SchemaUsuario):
    try:
        usuario.id = uuid.uuid4().hex
        driver = conexionDB()
        session = driver.session()
        query = "CREATE (n: Usuario { id: $id, nombre: $nombre, email: $email })"
        validarEmail(usuario.email)
        session.run(query, id=usuario.id, nombre=usuario.nombre, email=usuario.email)
        return { "message": "Usuario creado", "body": usuario }
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerUsuario(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (u:Usuario {id: $id}) RETURN u"
        results = session.run(query, id=id)
        data = results.value()
        if (data == []):
            raise HTTPException(status_code=404, detail=f"El usuario con id '{id}' no existe")
        return data
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def obtenerUsuario(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (u:Usuario {id: $id}) RETURN u"
        results = session.run(query, id=id)
        data = results.value()
        if (data == []):
            raise HTTPException(status_code=404, detail=f"El usuario con id '{id}' no existe")
        return data
    finally:
        driver.close()

def eliminarPorID(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (u:Usuario {id: $id}) DETACH DELETE u"
        obtenerUsuario(id)  # Verificar existencia antes de eliminar
        session.run(query, id=id)
        return { "message": "Usuario eliminado" }
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()

def validarEmail(email: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (u:Usuario {email: $email}) RETURN u"
        results = session.run(query, email=email)
        data = results.value()
        if (data != []):
            raise HTTPException(status_code=404, detail=f"El usuario con email '{email}' ya existe, usa un email unico")
        return None
    finally:
        driver.close()

def actualizar(id: str, usuario: SchemaUsuario):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (u:Usuario {id: $id}) SET u.nombre = $nombre, u.email = $email RETURN u"
        obtenerUsuario(id)  # Verificar existencia antes de actualizar
        validarEmail(usuario.email)  # Verificar email unico antes de actualizar
        results = session.run(query, id=id, nombre=usuario.nombre, email=usuario.email)
        return results.value()
    except Exception as e:
        print(e)
        return {"message": str(e)}
    finally:
        driver.close()
