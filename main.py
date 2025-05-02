from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import models, database
from app import users, searches, media
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
# Ensure DB tables are created
models.Base.metadata.create_all(bind=database.engine)

# Create FastAPI instance
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
class User(BaseModel):
    username: str
    password: str

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Here, you would validate the username and password and return a token
    # In this example, it just returns a placeholder token
    return {"access_token": "your_token", "token_type": "bearer"}


@app.get("/media/search")
async def search_media(q: str, type: str, token: str = Depends(oauth2_scheme)):
    # Handle the media search logic here
    return {"results": "list of media matching the query"}

# Mount static HTML (frontend)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Include API routers
app.include_router(users.router)
app.include_router(searches.router)
app.include_router(media.router)
