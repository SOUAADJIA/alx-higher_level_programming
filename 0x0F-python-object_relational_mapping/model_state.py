#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class representing the 'states' table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
