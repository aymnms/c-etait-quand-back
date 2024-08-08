import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from models import db, Player, Answer, Room, Question, Character
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cetaitquand.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    session_id = request.sid
    player = Player.query.filter_by(session_id=session_id).first()
    if player:
        room_uuid = player.room.uuid
        leave_room(room_uuid)
        emit('player_left', {'msg': f'Player {player.pseudo} has left the room'}, room=room_uuid)
        player.session_id = None
        db.session.commit()
    print("Client disconnected")

@socketio.on('login')
def handle_login(data):
    pseudo = data.get('pseudo')
    character_id = data.get('character_id')
    room_uuid = data.get('room_uuid', None)  # Optional

    if not pseudo or not character_id:
        emit('error', {"error": "Pseudo and character_id are required"})
        return

    # Check if the character exists
    character = Character.query.get(character_id) # query.get -> session.get
    if not character:
        emit('error', {"error": "Character not found"})
        return

    # Find or create the room
    if room_uuid:
        room = Room.query.filter_by(uuid=room_uuid).first()
        if not room:
            emit('error', {"error": "Room not found"})
            return
    else:
        room = Room(uuid=str(uuid.uuid4()))
        db.session.add(room)
        db.session.commit()

    # Create the player
    player = Player(pseudo=pseudo, character_id=character_id, room_id=room.id, session_id=request.sid)
    db.session.add(player)
    db.session.commit()

    join_room(room.uuid)

    emit('login_success', {
        "player_id": player.id,
        "room_id": room.id,
        "room_uuid": room.uuid
    }, room=room.uuid)

if __name__ == '__main__':
    # Check if the database file exists
    if not os.path.exists('cetaitquand.db'):
        with app.app_context():
            db.create_all()
            print("Database created.")
    else:
        print("Database already exists.")
    
    socketio.run(app, debug=True)