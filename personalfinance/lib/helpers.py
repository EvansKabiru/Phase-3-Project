from sqlalchemy.orm import Session
from lib.db import models

# CRUD operations for Users
def create_user(session: Session, username: str, email: str, password: str):
    user = models.User(username=username, email=email, password=password)
    session.add(user)
    session.commit()

def get_user(session: Session, user_id: int):
    user = session.query(models.User).filter(models.User.id == user_id).first()
    if user:
        print(f'User: {user.username}, Email: {user.email}')
    else:
        print("User not found!")

def update_user(session: Session, user_id: int, username: str, email: str, password: str):
    user = session.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.username = username
        user.email = email
        user.password = password
        session.commit()
        print(f"Updated user: {user.username}")
    else:
        print("User not found!")

def delete_user(session: Session, user_id: int):
    user = session.query(models.User).filter(models.User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"Deleted user: {user.username}")
    else:
        print("User not found!")

# CRUD operations for Incomes
def create_income(session: Session, amount: float, source: str, date: str, user_id: int):
    income = models.Income(amount=amount, source=source, date=date, user_id=user_id)
    session.add(income)
    session.commit()

def get_incomes(session: Session):
    incomes = session.query(models.Income).all()
    for income in incomes:
        print(f"Income: {income.source}, Amount: {income.amount}, Date: {income.date}")
