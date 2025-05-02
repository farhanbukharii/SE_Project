from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models, database
from .routers import users, searches, media

# Ensure DB tables are created
models.Base.metadata.create_all(bind=database.engine)

# Create FastAPI instance
app = FastAPI()

# Mount static HTML (frontend)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Include API routers
app.include_router(users.router)
app.include_router(searches.router)
app.include_router(media.router)
