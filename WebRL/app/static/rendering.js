//game specific
document.addEventListener("DOMContentLoaded", gameLoop);
var position = {
    x:0,
    y:0
};

var canvas;
var ctx;

var roomWidth = 3;
var roomHeight = 2;

function gameLoop(){
    // DRAWING
    canvas = document.getElementById("gamewindow");
    ctx = canvas.getContext("2d");
    function draw(){

        ctx.save();

        // Clear canvas
        ctx.clearRect(0,0,canvas.width,canvas.height);

        // Draw segments
        ctx.strokeStyle = "#999";
        for(var i=0;i<segments.length;i++){
            var seg = segments[i];
            ctx.beginPath();
            ctx.moveTo(seg.a.x,seg.a.y);
            ctx.lineTo(seg.b.x,seg.b.y);
            ctx.stroke();
        }

        //ctx.strokeStyle = "#555";
        //for (var row in height):
            //for (var col in width);
                //So... you need to get these from the server upon load, and store them, not too hard.

        //ctx.drawImage(img, 0, 0);


        // Draw red dot
        ctx.fillStyle = "#dd3838";
        for (var key in characterDict) {
            ctx.beginPath();
            ctx.arc(characterDict[key].x_position, characterDict[key].y_position, 4, 0, 2*Math.PI, false);
            ctx.fill();
        }
        ctx.restore();
    };


    // LINE SEGMENTS
    var segments = [
        //example of expected format
        //{a:{x:0,y:0}, b:{x:720,y:0}},
        ];

function generateGrid(width, height, size) {
  console.log("generateGrid() called!");
  //vertical lines
  for (var x_axis = 0; x_axis < width + 1; x_axis++) {
    segments.push({a:{x:x_axis * size, y:0}, b:{x:x_axis * size, y:height * size}});
  }

  //horizontal lines
  for (var y_axis = 0; y_axis < height + 1; y_axis++) {
    segments.push({a:{x:0, y:y_axis * size}, b:{x:width * size, y:y_axis * size}});
  }
};

socket.on('init_room', function(msg) {
    //timing issue
    console.log("init_room called");
    generateGrid(msg.room_width, msg.room_height, 36)
});


    // DRAW LOOP
    window.requestAnimationFrame = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.msRequestAnimationFrame;
    var updateCanvas = true;
    function drawLoop(){
        requestAnimationFrame(drawLoop);
        //if(updateCanvas){
            draw();
            //updateCanvas = false;
        //}
    }
    window.onload = function(){
        drawLoop();
    };

    // MOUSE
    var Mouse = {
        x: canvas.width/2,
        y: canvas.height/2
    };
    canvas.onmousemove = function(event){
        var rect = canvas.getBoundingClientRect();
        Mouse.x = event.clientX - rect.left;
        Mouse.y = event.clientY - rect.top;
        updateCanvas = true;
    };
};

//Example for building grid

/*
var seg = [];
var width = 2;
var height = 3;
for (w = 0; w < width; w++) {
  for (h = 0; h < height; h++){
    seg.push({a:{b:w,  c:h}})
  }
}

console.log(seg);


for (i in seg){
  console.log(seg[i]);
  console.log(seg[i].a.c);
}
*/
