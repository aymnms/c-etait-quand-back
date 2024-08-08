from flask import Flask, request, jsonify
from sqlalchemy.dialects.postgresql import UUID
from models import db, Player, Answer, Room, Question, Character
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cetaitquand.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
    app.run(debug=True)