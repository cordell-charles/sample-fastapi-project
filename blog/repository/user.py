from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import HTTPException, status
from ..hashing import Hash


def create(request: schema.User, db: Session):

    new_user = models.User(
        first_name= request.first_name,
        last_name = request.last_name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def show_user(id: int, db: Session):
    
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not available')
    

    return user