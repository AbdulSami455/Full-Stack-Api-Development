from jose import JWTError, jwt
from datetime import datetime,timedelta

#secret key
# Algorithm
#EXpiration time


SECRET_KEY="SDFSDFSDJFDSIFJDSIJFIDSmodg9dsjfisduf8d8fdsuf7ds7f7ds774738838383"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

def create_access_token(data:dict):
  to_encode=data.copy()

  expire= datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp":expire})

  encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


def verify_access_token(token:str,credentials_exception):
