#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """State Model"""

    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name: Mapped[str] = Column(String(128), nullable=False)
        cities: Mapped["City"] = relationship("City", backref="state",
                                              cascade="delete")
    else:
        name = ''

        @property
        def cities(self):
            """Return the list of City instances with state_id
            equal to the current State.id"""
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
