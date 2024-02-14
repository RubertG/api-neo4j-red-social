from fastapi import FastAPI
from src.routes.PostRoute import Route as PostRoute
from src.routes.UserRoute import Route as UserRoute
from src.routes.CommentRoute import Route as CommentRoute

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "endpoints":[
            { "usuarios": 
                {"GET":"http://localhost:8000/api/v1/usuarios",
                "GET2":"http://localhost:8000/api/v1/usuarios/{id}",
                 "POST":"http://localhost:8000/api/v1/usuarios",
                 "PUT":"http://localhost:8000/api/v1/usuarios/actualizar",
                 "DELETE":"http://localhost:8000/api/v1/usuarios/{id}"},
            },
            { "posts": 
                {"GET":"http://localhost:8000/api/v1/posts",
                "GET2":"http://localhost:8000/api/v1/posts/{id}",
                "GET3":"http://localhost:8000/api/v1/posts/usuario/{id}",
                 "POST":"http://localhost:8000/api/v1/posts",
                 "PUT":"http://localhost:8000/api/v1/posts/actualizar",
                 "DELETE":"http://localhost:8000/api/v1/posts/{id}"},
            },
            { "comentarios": 
                {"GET":"http://localhost:8000/api/v1/comentarios",
                "GET2":"http://localhost:8000/api/v1/comentarios/{id}",
                "GET3":"http://localhost:8000/api/v1/comentarios/post/{id}",
                 "POST":"http://localhost:8000/api/v1/comentarios",
                 "PUT":"http://localhost:8000/api/v1/comentarios/actualizar",
                 "DELETE":"http://localhost:8000/api/v1/comentarios/{id}"},
            }
        ]
    }
app.include_router(UserRoute, prefix="/api/v1/usuarios", tags=["Usuario"])
app.include_router(PostRoute, prefix="/api/v1/posts", tags=["Post"])
app.include_router(CommentRoute, prefix="/api/v1/comentarios", tags=["Comentario"])