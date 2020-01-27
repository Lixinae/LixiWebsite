from application import db


class Project(db.Model):
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Nom projet {}\nLangages:>'.format(self.name, self.langages)

    # class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')
#
#     # Très utile pour debug : exemple
#     # >>> from app.models import User
#     # >>> u = User(username='susan', email='susan@example.com')
#     # >>> u
#     # < User susan >
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
