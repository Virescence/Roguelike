
var socket = io.connect('http://' + document.domain + ':' + location.port);




function connect(){
    //connect to the socket server.
    socket.on('connect', function() {
        //socket.emit('connect', {data: 'I\'m connected!'});
    });
};
connect();


socket.on('server_connect', function(msg) {
    console.log("received server_connect");
    //alert(msg.message);
    //document.getElementById('sample').textContent=msg.message;
});


socket.on('init_player', function(msg) {
    console.log("received init_player");
    createCharacter(msg.sessionId, msg.x_position, msg.y_position, msg.hp);
    console.log(msg.x_position + ", " + msg.y_position);
});


socket.on('remove_player', function(msg) {
    console.log("received remove_player");
    delete characterDict[msg.sessionId]
    console.log("deleted " + msg.sessionId);
});


socket.on('position_update', function(msg) {
    console.log('received position_update');
    var character = characterDict[msg.sessionId];
    character.x_position = msg.x_position;
    character.y_position = msg.y_position;
    //console.log(msg.x_position, + ", " + msg.y_position)
    //console.log(character.x_position)
    //console.log(character.y_position)
});

socket.on('room_update', function(msg) {
    console.log('received room_update');
    roomWidth = msg.width;
    roomHeight = msg.height;
});


var messages_received = [];
socket.on('server_update', function(msg) {
    console.log(msg.update);

    //if (messages_received.length >= 10){
    //messages_received.shift()}
    //messages_received.push(servermsg.update);
    //message_string = '';
    //for (var i = 0; i < messages_received.length; i++){
        //message_string = message_string + '<p>' + messages_received[i].toString() + '</p>';
    //}
    //document.getElementById('messages').innerHTML=message_string;
});
