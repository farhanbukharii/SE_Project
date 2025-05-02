from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, crud, schemas, auth, models
from typing import List

router = APIRouter()

@router.post("/searches/", response_model=schemas.RecentSearch)
def save_search(query: schemas.RecentSearchCreate, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_recent_search(db, user=current_user, query=query.query)

@router.get("/searches/", response_model=List[schemas.RecentSearch])
def list_searches(db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(auth.get_current_user)):
    return crud.get_recent_searches(db, user=current_user)

@router.delete("/searches/{search_id}")
def delete_search(search_id: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(auth.get_current_user)):
    deleted = crud.delete_recent_search(db, user=current_user, search_id=search_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Search not found")
    return {"msg": "Search deleted"}
