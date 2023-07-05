import random
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import  RealDictCursor

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
router=APIRouter()
@router.post("/user")

def create_users(newuser: user):


    # Hashing Password
    hashedpass=pwd_context.hash(newuser.password)
    newuser.password=hashedpass
    num=random.randrange(4,90000)
    cursor.execute("""insert into users(id,email,password)values(%s,%s,%s)""",(num,newuser.email,newuser.password))
    conn.commit()

    return {"message":"done"}

@router.get("/user")
def get_user():
    cursor.execute("""select * from users""")
    db00=cursor.fetchall()
    conn.commit()
    return {"messgae":db00}