from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import  RealDictCursor
app=FastAPI()


try:
    conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='abdullah@1234',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("Database Connection was Successful")
except Exception as error:
    print("Failed")
    print("Error:",error)

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
    cursor.execute("select * from posts")
    posts=cursor.fetchall()
    print(posts)
    return {"Post":posts}


@app.post("/posts")

def create_posts(new_post: Post):
    #cursor.execute("""insert into posts(title,content,published)values(%s,%s,%s)returning *""",(new_post.title,new_post.content,new_post.publication))
    #dbpost=cursor.fetchone()

    return {"Message": "start one"}

def find_post(id):
    for p in my_post:
        if p["id"]==id:
            return p
@app.get("/posts/{id}")

def get_posts(id:int):
  print(id)
  cursor.execute("""SELECT * from posts WHERE id = %s""",(str(id)))
  postst=cursor.fetchone()
  #print(postst)
  #post1=find_post(id)
  if not postst:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not Found")
  return  {"post detail":postst}




@app.delete("/posts/{id}")

def delete_posts(id: int):
     cursor.execute("""delete from posts where id = %s returning *""",(str(id)))
