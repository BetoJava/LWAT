from fastapi import APIRouter, HTTPException
from tinydb import TinyDB
from app.db.base import users_table: TinyDB.table
from app.schemas.user import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut, status_code=201)
def create_user(user_in: UserCreate):
    data = user_in.dict()
    user_id = users_table.insert(data)
    return UserOut(id=user_id, **data)

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int):
    record = users_table.get(doc_id=user_id)
    if not record:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut(id=user_id, **record)

@router.get("/", response_model=list[UserOut])
def list_users():
    return [UserOut(id=rec.doc_id, **rec) for rec in users_table.all()]

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    removed = users_table.remove(doc_ids=[user_id])
    if not removed:
        raise HTTPException(status_code=404, detail="User not found")
    return
