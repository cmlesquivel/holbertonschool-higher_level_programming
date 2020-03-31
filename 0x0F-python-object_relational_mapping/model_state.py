#!/usr/bin/python3
"""Module that define the table states
"""

from sqlalchemy import (create_engine, Column, Date, Integer,
                        ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Define the table states """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
