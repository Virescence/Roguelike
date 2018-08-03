var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var width = window.innerWidth;
var height = window.innerHeight;
var x = window.innerWidth/2;
var y = window.innerHeight/2;
resize();

function drawBall() {
  ctx.beginPath();
  ctx.arc(x,y,40,0,2*Math.PI);
  ctx.fillStyle = '#9e356a';
  ctx.fill();
}

function loop() {
  ctx.clearRect(0, 0, width, height);
  drawBall();
  requestAnimationFrame(loop);
}

loop();

function touch(e) {
  x = e.originalEvent.touches[0].pageX;
  y = e.originalEvent.touches[0].pageY;
}

function mousemove(e) {
  x = e.pageX;
  y = e.pageY;
}

function resize() {
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
}

window.addEventListener('resize', resize);
window.addEventListener('touchstart', touch);
window.addEventListener('touchmove', touch);
window.addEventListener('mousemove', mousemove);