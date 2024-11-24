from fastapi import APIRouter

from api.kaggle.routes import router as downloads_router


version = "v1"

routes = APIRouter(prefix=f"/api/{version}", redirect_slashes=False)


routes.include_router(downloads_router, prefix="/kaggle", tags=["downloads"])
