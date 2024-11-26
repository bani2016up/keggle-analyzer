from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import httpx


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://auth-service:8000/user/{token}')
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return response.json()
