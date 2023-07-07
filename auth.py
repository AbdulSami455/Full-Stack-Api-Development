from fastapi import FastAPI,APIRouter,status,HTTPException,Response,Depends
from pydantic import BaseModel
import psycopg2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from psycopg2.extras import  RealDictCursor
import utilis,Oauth
import random
from typing import Optional
def UserLogin(BaseModel):
    email : str
    password: str


try:
    conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='abdullah@1234',cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("Database Connection was Successful")
except Exception as error:
    print("Failed")
    print("Error:",error)

class user(BaseModel):
    email: str
    password: str

class token(BaseModel):
    access_token:str
    type:str

class Tokendata(BaseModel):
    id:Optional[str]=None

auth=FastAPI()



@auth.post('/createuser')
def createuser(newuser:user):
    hashpass=utilis.hashing(newuser.password)
    num = random.randrange(4, 90000)
    cursor.execute("""insert into users(id,email,password)values(%s,%s,%s)""", (num, newuser.email, hashpass))
    conn.commit()
    return {"message":"User Created"}

@auth.post('/loginnow')
def login(newuser:user):

    # Retrieve the password from the database based on the provided email
    cursor.execute("SELECT password FROM users WHERE email = %s", (newuser.email,))
    result = cursor.fetchone()

    if result is None:
        return {"message": "User not found"}

    stored_password = result[0]
    provided_password = newuser.password

    # Compare the provided password with the stored password
    if utilis.verify(provided_password, stored_password):
        return {"message": "LoORDER BY id ASC gin successful"}
    else:
        return {"message": "Incorrect password"}
@auth.post('/token')
def tokengenerate(user:OAuth2PasswordRequestForm=Depends()):

  access_token=Oauth.create_access_token(data={"username":user.username})
  return {"access_token":access_token,"type":"bearer"}




