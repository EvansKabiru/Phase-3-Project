from __future__ import with_statement
import sys
import os
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool
from alembic import context

# Import your models' MetaData here
from lib.db.models import Base  # Replace with the correct import path for your Base
from lib.db import engine  # Ensure this points to where your engine is defined (if needed)

# This is the Alembic Config object, which provides access to
# the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Add your model's MetaData object here for 'autogenerate' support
target_metadata = Base.metadata  # Assuming `Base` is the base class that all your models inherit from.

# Other Alembic settings (for example, connecting to your database)
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Running the migration (offline or online)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
