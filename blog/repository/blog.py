from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import HTTPException, status



def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs



def create(request: schema.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id: int, request: schema.Blog, db: Session):

    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    blogs.update(request)
    db.commit()
    return 'Updated successfully'



def destroy(id: int, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return 'delete completed'



def show_all(id: int, db: Session):
    single_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not single_blog:

        # This is normal way of writing without httpexception # 
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    
    return single_blog