from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    """Schéma pour la création (input) – on ne met pas d’ID ici."""
    pass

class UserOut(UserBase):
    """Schéma pour la sortie (output), avec l’ID."""
    id: int

    class Config:
        orm_mode = True
