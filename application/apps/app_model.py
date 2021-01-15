from sqlalchemy import Column, Integer, String
from flask import url_for, jsonify
from application import db


# {
#     'name': "Webcrawler",
#     'quick_description': "Un crawler pour parser / scrap du contenu en ligne",
#     'miniature': url_for('static', filename='img/miniature/webcrawler_miniature.png'),
#     'url': url_for('webcrawler_bp.webcrawler_page')
# },
class Apps(db.Model):
    __tablename__ = "Apps"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String(64), index=True, unique=True)
    quick_description = Column(String(128))
    miniature_path = Column(String(128))
    url = Column(String(128))

    def __init__(self, name: str, quick_description: str, url: str):
        self.name = name
        self.quick_description = quick_description
        self.url = url

    def __repr__(self):
        return '<Id:{}\n' \
               'Nom projet: {}\n' \
               'Description rapide:{}\n' \
               'Miniature:{}\n' \
               'Url:{}>\n'.format(self.id,
                                  self.name,
                                  self.quick_description,
                                  url_for('static', filename=self.miniature_path),
                                  url_for(self.url))

    def to_dict(self):
        return jsonify({"Id": self.id,
                        'name': self.name,
                        'quick_description': self.quick_description,
                        'miniature': url_for('static', filename=self.miniature_path),
                        'url': url_for(self.url)})
