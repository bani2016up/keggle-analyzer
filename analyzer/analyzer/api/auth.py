from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session
from database import get_db
import httpx

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="http://localhost:8000/login",
    tokenUrl="http://localhost:8000/auth"
)

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/user/{token}")
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return response.json()
