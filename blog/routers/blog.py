from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schema, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session
from fastapi_utils.tasks import repeat_every
from ..repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

## get requests ### 

@router.get('/', response_model=List[schema.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.show_all(id, db)




### post requests ###

@repeat_every(seconds=60 * 60)
@router.post('/', status_code=status.HTTP_201_CREATED) # 201 code for created
def create(request: schema.Blog, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)



### update requests ### 

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Blog, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)



### delete requests ###

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)