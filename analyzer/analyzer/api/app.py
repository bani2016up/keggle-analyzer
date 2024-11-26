from fastapi import FastAPI
from database import engine
import models
from routers import chains

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chains.router, prefix="/api/v1", tags=["chains"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
