from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app=FastAPI()

@app.get("/")
def root():
    return {"message":"Hello1234567"}

@app.get("/posts")

def get_posts():
    return {"Post":"Hello Everyone "}


@app.post("/createpost")

def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"Message": "new"}