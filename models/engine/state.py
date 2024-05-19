#!/usr/bin/python3
"""
this State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
   this  State class / table model
    """
    __tablename__ = 'states'
    
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')
    else:
        name = ''
    
    @property
    def cities(self):
        """
        Returns the list of City instances with state_id
        """
        from models import storage
        return [city for city in storage.all(City).values() if city.state_id == self.id]
