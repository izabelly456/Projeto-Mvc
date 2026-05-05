#1. Hash  verificação de senhas com bcrypt
#2. geração de tokens JWT 
# 3. leitura e vaçlidação de token vindo do cookie

from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Request, HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# cryptcontext - configura o bcrypt como o algoritmo de hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# funcoes de senha
def hash_password(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)

# funcoes de token - JWT
def criar_token(data: dict):
    payload = data.copy()

    #define quando o token expira
    espira = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": espira})

    #criar o token JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decodificar_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

