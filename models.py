import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

database_name = "capstone"
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

# uncomment if you prefer not to use migrations , it will create for you the required entities
    # if os.environ['FLASK_ENV'].lower() == 'development':
    #     db.create_all()


class MoviesActors(db.Model):
    __tablename__ = 'movies_actors'

    movie_id = db.Column(
        db.Integer,
        db.ForeignKey('movie.id'),
        primary_key=True)
    actor_id = db.Column(
        db.Integer,
        db.ForeignKey('actor.id'),
        primary_key=True)

    actor = db.relationship("Actor", back_populates="movies")
    movie = db.relationship("Movie", back_populates="actors")


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.DateTime, default=datetime.utcnow)

    actors = db.relationship("MoviesActors", back_populates="movie")

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


class Actor(db.Model):
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    movies = db.relationship("MoviesActors", back_populates="actor")

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
