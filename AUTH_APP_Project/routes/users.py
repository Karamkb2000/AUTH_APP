from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from dependencies import dependencies
users_router = APIRouter()

@users_router.get("/me", response_model=schemas.UserResponse)
def read_users_me(current_user: schemas.UserResponse = Depends(dependencies.get_current_user)):
    return current_user

@users_router.get("/admin", response_model=schemas.UserResponse)
def read_admin_data(current_user: schemas.UserResponse = Depends(dependencies.get_current_admin_user)):
    return {"admin_data": "This is sensitive admin data"}