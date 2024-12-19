from faker import Faker
from sqlalchemy.orm import Session
from lib.db.models import User, Income, Expense, FinancialGoal, Category, FinancialInstitution
from lib.db import models

fake = Faker()

# Generate fake data for users, incomes, expenses, goals, categories, and financial institutions
def create_fake_data(session: Session):
    # Create some fake users
    for _ in range(5):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password()
        )
        session.add(user)
    session.commit()

    # Create some fake financial institutions
    for _ in range(3):
        institution = FinancialInstitution(
            name=fake.company(),
            account_type=fake.random_element(["Checking", "Savings"])
        )
        session.add(institution)
    session.commit()

    # Assign financial institutions to users
    users = session.query(User).all()
    institutions = session.query(FinancialInstitution).all()
    for user in users:
        user.financial_institutions.append(fake.random_element(institutions))
    session.commit()

    # Create categories
    categories = ['Food', 'Rent', 'Entertainment', 'Utilities']
    for category_name in categories:
        category = Category(name=category_name)
        session.add(category)
    session.commit()

    # Create fake incomes and expenses
    for user in users:
        income = Income(
            amount=fake.random_number(digits=4),
            source=fake.random_element(["Salary", "Freelance", "Investment"]),
            date=fake.date_this_year(),
            user_id=user.id
        )
        session.add(income)
        session.commit()

        # Generate some fake expenses
        for _ in range(3):
            expense = Expense(
                amount=fake.random_number(digits=2),
                date=fake.date_this_year(),
                income_id=income.id,
                category_id=fake.random_element([cat.id for cat in session.query(Category).all()])
            )
            session.add(expense)
        session.commit()

        # Generate fake financial goals
        goal = FinancialGoal(
            target_amount=fake.random_number(digits=3),
            target_date=fake.date_this_year(),
            user_id=user.id
        )
        session.add(goal)
    session.commit()
