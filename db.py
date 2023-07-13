"""Declare the database engine and session.""" ""
import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Model(DeclarativeBase):
    """Define the base model.

    All others will inherit from this.
    """

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


load_dotenv()


engine = create_engine(os.environ["DATABASE_URL"])
Session = sessionmaker(bind=engine)
