from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from application import db


class TravailDuCuirInstaParent(db.Model):
    __tablename__ = "tdc_insta_parent"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String(64), index=True, unique=True)
    path_to_file = Column(String(128))
    childrens = relationship("TravailDuCuirInstaEnfant")

    def __init__(self, name: str, path: str):
        self.name = name
        self.path_to_file = path

    def __repr__(self):
        return ""

    def to_json(self):
        return {
            'name': self.name,
            'path_to_file': self.path_to_file,
            'childrens': self.childrens
        }


class TravailDuCuirInstaEnfant(db.Model):
    __tablename__ = "tdc_insta_enfant"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String(64), index=True, unique=True)
    path_to_file = Column(String(128))
    parent_id = Column(Integer, ForeignKey("tdc_insta_parent.id"))

    def __init__(self, name: str, path: str):
        self.name = name
        self.path_to_file = path

    def __repr__(self):
        return ""

    def to_json(self):
        return {
            'name': self.name,
            'path_to_file': self.path_to_file,
            'parent_id': self.parent_id
        }
