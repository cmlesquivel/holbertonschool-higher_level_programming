#!/usr/bin/python3
"""Module that define the table states
"""

from sqlalchemy import (create_engine, Column, Date, Integer,
                        ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """links to the MySQL table states
    Atributes:
       id: auto-generated, unique integer, required and is a primary key
       name:string required"""
    
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
