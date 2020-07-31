# from application import db
#
# from flask import url_for
#
#
# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     outils = db.Column(db.String(128))
#     quick_description = db.Column(db.String(128))
#     miniature = db.Column(db.String(128))
#     url = db.Column(db.String(128))
#
#     def __repr__(self):
#         return '<Id:{}\nNom projet: {}\nOutils:{}\nDescription rapide:{}\nMiniature:{}\nUrl:{}>'.format(self.id, self.name, self.outils,
#                                                                                                         self.quick_description,
#                                                                                                         self.miniature,
#                                                                                                         self.url)
#
#     def to_dict(self):
#         data = {
#             'name': self.name,
#             'outils': self.outils,
#             'quick_description': self.quick_description,
#             'miniature': url_for('static', filename=self.miniature),
#             'url': url_for(self.url),
#         }
#         return data
