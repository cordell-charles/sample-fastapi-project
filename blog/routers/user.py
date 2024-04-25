from fastapi import APIRouter, Depends
from .. import schema, database, oauth2
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['Users']
)


## get requests ### 

@router.get('/{id}', response_model=schema.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return user.show_user(id, db)




## post requests ### 

@router.post('/', response_model=schema.ShowUser)
def create_user(request: schema.User, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return user.create(request, db)


## update requests ### 

## delete requests ### 