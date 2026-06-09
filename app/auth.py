from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")
EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 30))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    # bcrypt max 72 bytes support করে
    safe_pw = password.encode("utf-8")[:72].decode("utf-8", errors="ignore")
    return pwd_context.hash(safe_pw)

def verify_password(plain: str, hashed: str):
    safe_pw = plain.encode("utf-8")[:72].decode("utf-8", errors="ignore")
    return pwd_context.verify(safe_pw, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
