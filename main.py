# Library / Dep imports
from fastapi import FastAPI
from typing import Optional
import uvicorn

# Model imports
from models import Blog

app = FastAPI()

# Generally use get or post


## Get operations
@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # Only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


    return {'data': {'name' : 'cordell'}}


# FastAPI reads endpoints in order, so its possible to have issues where endpoints have similar paths
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id

    return {'data': {'1', '2'}}


## Post operations


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}


# Changing port for debugging purpose

# if __name__ == "__main":
#     uvicorn.run(app, host="127.0.0.1", port='9000')

# Run command python main.py 