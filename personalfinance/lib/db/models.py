from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# User Table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # One-to-Many Relationship: One user can have multiple incomes
    incomes = relationship("Income", back_populates="user")
    
    # One-to-Many Relationship: One user can have multiple financial goals
    financial_goals = relationship("FinancialGoal", back_populates="user")
    
    # Many-to-Many Relationship: A user can have multiple financial institutions
    financial_institutions = relationship("FinancialInstitution", secondary="user_institution", back_populates="users")


# Income Table
class Income(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    source = Column(String)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    # One-to-Many Relationship: Income can have multiple expenses
    expenses = relationship("Expense", back_populates="income")
    
    user = relationship("User", back_populates="incomes")


# Expense Table
class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    date = Column(Date)
    category_id = Column(Integer, ForeignKey('categories.id'))
    income_id = Column(Integer, ForeignKey('incomes.id'))

    # One-to-Many Relationship: Expense belongs to a single category
    category = relationship("Category", back_populates="expenses")
    
    # One-to-Many Relationship: Expense belongs to a single income
    income = relationship("Income", back_populates="expenses")


# Financial Goal Table
class FinancialGoal(Base):
    __tablename__ = 'financial_goals'

    id = Column(Integer, primary_key=True, index=True)
    target_amount = Column(Float)
    target_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    # One-to-Many Relationship: Goal is tied to a user
    user = relationship("User", back_populates="financial_goals")


# Category Table
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    # One-to-Many Relationship: Category can have many expenses
    expenses = relationship("Expense", back_populates="category")


# Financial Institution Table
class FinancialInstitution(Base):
    __tablename__ = 'financial_institutions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    account_type = Column(String)

    # Many-to-Many Relationship: A financial institution can serve multiple users
    users = relationship("User", secondary="user_institution", back_populates="financial_institutions")


# Many-to-Many Relationship Table: User and FinancialInstitution association
class UserInstitution(Base):
    __tablename__ = 'user_institution'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    institution_id = Column(Integer, ForeignKey('financial_institutions.id'), primary_key=True)
