from pydantic import BaseModel, Field
from typing import Optional
import uuid

class SchemaUsuario(BaseModel):
    id: Optional[str] = Field(default=uuid.uuid4().hex)  # Se especifica el tipo como int y se agrega un ejemplo
    nombre: str = Field(example="Ana")
    email: str = Field(example="ana@ejemplo.com")
