import click
from sqlalchemy.orm import Session
from lib.db import models, session_local
from lib.helpers import create_user, get_user, update_user, delete_user, create_income, get_incomes

@click.group()
def cli():
    """CLI to interact with the Personal Finance Dashboard"""
    pass

@click.command()
@click.argument('username')
@click.argument('email')
@click.argument('password')
def create(username, email, password):
    """Create a new user"""
    with Session(session_local) as session:
        create_user(session, username, email, password)

@click.command()
@click.argument('user_id')
def get(user_id):
    """Get user details by ID"""
    with Session(session_local) as session:
        get_user(session, user_id)

@click.command()
@click.argument('user_id')
@click.argument('username')
@click.argument('email')
@click.argument('password')
def update(user_id, username, email, password):
    """Update user details"""
    with Session(session_local) as session:
        update_user(session, user_id, username, email, password)

@click.command()
@click.argument('user_id')
def delete(user_id):
    """Delete a user by ID"""
    with Session(session_local) as session:
        delete_user(session, user_id)

@click.command()
def incomes():
    """View all incomes"""
    with Session(session_local) as session:
        get_incomes(session)

cli.add_command(create)
cli.add_command(get)
cli.add_command(update)
cli.add_command(delete)
cli.add_command(incomes)

if __name__ == '__main__':
    cli()
