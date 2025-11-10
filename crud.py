from sqlalchemy.orm import Session
import models, auth

# Users
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user):
    hashed_pw = auth.hash_password(user.password)
    db_user = models.User(
        name=user.name, email=user.email, password=hashed_pw,
        phone_number=user.phone_number
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Todos
def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo, owner_id: int):
    db_todo = models.Todo(**todo.dict(), owner_id=owner_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_user_todos(db: Session, owner_id: int):
    return db.query(models.Todo).filter(models.Todo.owner_id == owner_id).all()

# Update Todo 
def update_todo(db: Session, todo: models.Todo, title=None, description=None, completed=None):
    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if completed is not None:
        todo.completed = completed
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

# Delete Todo 
def delete_todo(db: Session, todo: models.Todo):
    db.delete(todo)
    db.commit()
