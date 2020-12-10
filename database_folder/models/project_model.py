from application import db
from sqlalchemy import Column, Integer, String
from flask import url_for


class Project(db.Model):
    __tablename__ = "Projects"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String(64), index=True, unique=True)
    outils = Column(String(128))
    quick_description = Column(String(128))
    miniature_path = Column(String(128))
    url = Column(String(128))

    def __init__(self, name: str, outils: str, quick_description: str, miniature_path: str, url: str):
        self.name = name
        self.outils = outils
        self.quick_description = quick_description
        self.miniature_path = miniature_path
        self.url = url

    def __repr__(self):
        return '<Id:{}\n' \
               'Nom projet: {}\n' \
               'Outils:{}\n' \
               'Description rapide:{}\n' \
               'Miniature_path:{}\n' \
               'Url:{}>'.format(self.id,
                                self.name,
                                self.outils,
                                self.quick_description,
                                url_for('static', filename=self.miniature_path),
                                url_for(self.url))

    def to_dict(self):
        data = {
            'name': self.name,
            'outils': self.outils,
            'quick_description': self.quick_description,
            'miniature_path': url_for('static', filename=self.miniature_path),
            'url': url_for(self.url),
        }
        return data
