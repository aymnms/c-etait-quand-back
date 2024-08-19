from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, default=0)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    session_id = db.Column(db.String(36), unique=True, nullable=True)
    answers = db.relationship('Answer', backref='player', lazy=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(200), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid.uuid4()))
    players = db.relationship('Player', backref='room', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    solution = db.Column(db.String(200), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    players = db.relationship('Player', backref='character', lazy=True)
