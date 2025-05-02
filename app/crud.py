from sqlalchemy.orm import Session
from . import models, schemas, auth
from . import models, schemas

def create_recent_search(db: Session, user: models.User, query: str):
    search = models.RecentSearch(query=query, owner=user)
    db.add(search)
    db.commit()
    db.refresh(search)
    return search

def get_recent_searches(db: Session, user: models.User):
    return db.query(models.RecentSearch).filter(models.RecentSearch.owner == user).order_by(models.RecentSearch.timestamp.desc()).all()

def delete_recent_search(db: Session, user: models.User, search_id: int):
    search = db.query(models.RecentSearch).filter(models.RecentSearch.id == search_id, models.RecentSearch.owner == user).first()
    if search:
        db.delete(search)
        db.commit()
    return search

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
