from fastapi import FastAPI
from ml_hub.app.routers import index
from ml_hub.__init__ import __version__

app = FastAPI(
    version=__version__
)

app.include_router(
    index.router, 
    prefix=""
)