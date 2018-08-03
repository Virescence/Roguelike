function keypressed(evt){
    evt = evt || window.evt;
    var charCode = evt.keyCode || evt.which;
    var charStr = String.fromCharCode(charCode);
    socket.emit('move', {data:charStr});
};

document.onkeypress = function(evt){
    keypressed(evt);
};

function roomUpdated(){


};