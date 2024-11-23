

from fastapi import FastAPI
from pydantic import BaseModel
import os



app = FastAPI()


@app.put("/test/")
async def update_item() -> str:
    return "Gooooood :)))"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
