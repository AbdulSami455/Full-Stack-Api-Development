import random

from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import  RealDictCursor
#from .routers import posts,users
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
from fastapi.middleware.cors import CORSMiddleware

#from .import model
#from sqlalchemy.orm import Session
#from .database import SessionLocal,engine

#model.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins = [
    "http://www.google.com",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()"""



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

class user(BaseModel):
    email: str
    password: str


my_post=[{"title":"Post1","content":"this is Post Number 1","id":1},{"title":"Post2","content":"this is second post","id":2}]
@app.get("/")
def root():
    return {"message":"Hello1234567"}




#@app.get("/sqlalchemy")
#def tests_posts(db: Session= Depends(get_db)):
 #  return {"status":"Return"}

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


@app.post("/user")

def create_users(newuser: user):


    # Hashing Password
    hashedpass=pwd_context.hash(newuser.password)
    newuser.password=hashedpass
    num=random.randrange(4,90000)
    cursor.execute("""insert into users(id,email,password)values(%s,%s,%s)""",(num,newuser.email,newuser.password))
    conn.commit()

    return {"message":"done"}

@app.get("/user")
def get_user():
    cursor.execute("""select * from users""")
    db00=cursor.fetchall()
    conn.commit()
    return {"messgae":db00}
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
     conn.commit()