from pydantic import BaseModel, Field
from typing import Optional
import uuid

class SchemaComentario(BaseModel):
    id: Optional[str] = Field(default=uuid.uuid4().hex)  # Se especifica el tipo como int y se agrega un ejemplo
    contenido: str = Field(example="¡Me gusta este post!")
    usuario_id: str = Field(example=1)  # Se especifica el tipo como int y se agrega un ejemplo
    post_id: str = Field(example=1)  # Se especifica el tipo como int y se agrega un ejemplo
