#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from .base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from ..config import Config

class LucClass(BaseModel):
    """LucClass."""

    __tablename__ = 'classes'
    __table_args__ = dict(schema=Config.ACTIVITIES_SCHEMA)

    id = Column(Integer, primary_key=True)
    code = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    symbology = Column(Text, nullable=False)
    class_system_id = Column(Integer, ForeignKey('{}.class_systems.id'.format(Config.ACTIVITIES_SCHEMA),
                                                              ondelete='NO ACTION'), nullable=False)

    classification_system = relationship('LucClassificationSystem')