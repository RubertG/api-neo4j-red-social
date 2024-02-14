from pydantic import BaseModel, Field
from typing import Optional
import uuid

class SchemaPost(BaseModel):
    id: Optional[str] = Field(default=uuid.uuid4().hex)  # Se especifica el tipo como int y se agrega un ejemplo
    contenido: str = Field(example="¡Hola a todos!")
    usuario_id: str = Field(example=1)  # Se especifica el tipo como int y se agrega un ejemplo