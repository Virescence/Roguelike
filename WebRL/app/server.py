import threading

from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, leave_room


import time
import game


app = Flask(__name__)
app.config['SECRET_KEY'] = 'idkfa'
app.debug = False
socket = SocketIO(app)
client_list = []
client_dict = {}


@app.route("/")
def index():
    return render_template("main.html", test="lolol")


@app.route("/rl")
def test():
    return render_template("rl.html")


@app.route("/lighting")
def lightingTest():
    return render_template('draft0.html')

#
#
# Socket Stuff
#
#


@socket.on('browsermsg')
def handle_event(json):
    print("message recv: " + str(json))
    # socket.emit('newnumber', {'number': 'yo'}, broadcast=True)
    # socket.emit('newnumber', {'number': game.main()}, broadcast=True)
    socket.emit('servermsg', {'message': client_dict[request.sid] + ": " + json['data']})


@socket.on('connect')
def connected():
    print("connected")
    if request.sid not in client_list:
        client_list.append(request.sid)
    socket.emit('server_connect', {'message': request.sid})
    # tell the new player about the room
    socket.emit('init_room', {'room_width': game.room.width,
                              'room_height': game.room.height}, room=request.sid)
    newChar = game.Player(request.sid)

    # tell everyone about the new player
    socket.emit('init_player', {'sessionId': newChar.sessionId,
                                'x_position': newChar.x_position,
                                'y_position': newChar.y_position})

    # tell the new player about everyone else
    for key, value in game.playerDict.items():
        if value != newChar:
            socket.emit('init_player', {'sessionId': key,
                                    'x_position': value.x_position,
                                    'y_position': value.y_position,
                                    'hp': newChar.hp}, room=request.sid)

    # https://gist.github.com/ericremoreynolds/dbea9361a97179379f3b


@socket.on('disconnect')
def disconnect():
    session_id = request.sid
    client_list.remove(session_id)
    del game.playerDict[session_id]
    print(request.sid + " disconnected")
    socket.emit('remove_player', {'sessionId': session_id})


@socket.on('move')
def keypress(json):
    command = json['data']
    caseDict = {
        'w': 'forward',
        'a': 'left',
        's': 'backward',
        'd': 'right'}
    response = (caseDict.get(command, 'invalid'))
    if response == 'invalid':
        socket.emit('server_update', {'update': request.sid + ": " + 'sent a broadcast!'})
    else:
        character = game.playerDict[request.sid]
        character.move(response)
        # socket.emit('server_update', {'update': request.sid + ": " + response}, room=request.sid)
        socket.emit('position_update', {'sessionId': request.sid,
                                       'x_position': character.x_position,
                                       'y_position': character.y_position})


@socket.on('login')
def login(json):
    client_dict[request.sid] = json["data"]
    for key, value in client_dict.items():
        print(key, value)
    socket.emit('servermsg', {'message': json["data"] + " has joined the server!"})


def run_socket():
    socket.run(app)


def run_app():
    app.run(host="0.0.0.0", threaded=True)


def broadcast(message):
    print(message)
    socket.emit('newnumber', {'number': message}, broadcast=True)


def start_server():
    socket.run(app, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    serverThread = threading.Thread(target=start_server)
    serverThread.start()

    staminaUpdateThread = threading.Thread(target=game.stamina_update)
    staminaUpdateThread.start()
