from fastapi import FastAPI,APIRouter,status,HTTPException,Response
from pydantic import BaseModel
import psycopg2
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

router=APIRouter()

@router.post('/login')
def login():




