from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app=FastAPI()


class Post(BaseModel):
    title : str
    content : str
    publication : bool=True


my_post=[{"title":"Post1","content":"this is Post Number 1","id":1},{"title":"Post2","content":"this is second post","id":2}]
@app.get("/")
def root():
    return {"message":"Hello1234567"}

@app.get("/posts")

def get_posts():
    return {"Post":my_post}


@app.post("/posts")

def create_posts(new_post: Post):
    print(new_post.dict())
    post_dict=new_post.dict()
    post_dict['id']=randrange(0,100000000)
    my_post.append(post_dict)
    return {"Message": my_post}

def find_post(id):
    for p in my_post:
        if p["id"]==id:
            return p
@app.get("/posts/{id}")

def get_posts(id:int):
  print(id)
  post1=find_post(id)
  if not post1:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not Found")
  return  {"post detail":post1}




#@app.delete("/posts/{id}")

#def delete_posts(id:int):
