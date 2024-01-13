from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from services import user as UserService

from dto import user as UserDto

router = APIRouter()


@router.post('/', tags=["user"])
async def create(data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{id}', tags=["user"])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)


@router.delete('/{id}', tags=["user"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.delete_user_by_id(id, db)

@router.put('/{id}', tags=["user"])
async def update(id: int = None, data:UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.update_user_by_id(id, data, db)