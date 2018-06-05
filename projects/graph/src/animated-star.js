// Animated Star

const centerX = canvas.width / 2;
const centerY = canvas.height / 2;
const gap = 1;
const steps = 100;
const increment = (90 * Math.PI) / steps;
let start = null;

function update(timeStamp) {
  if (!start) {
    start = timeStamp;
  }
  const progress = Math.min((timeStamp - start) / 10000, 1);
  let theta = increment;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.moveTo(centerX, centerY);
  while (theta < progress * 200 * Math.PI) {
    const newX = centerX + theta * Math.cos(theta) * gap;
    const newY = centerY + theta * Math.sin(theta) * gap;
    ctx.lineTo(newX, newY);
    theta = theta + increment;
  }
  ctx.stroke();
  if (progress < 0.12) {
    requestAnimationFrame(update);
    ctx.strokeStyle = '#FF0000';
  } else if (progress < 0.24) {
    requestAnimationFrame(update);
    ctx.strokeStyle = '#FF6600';
  } else if (progress < 0.36) {
    requestAnimationFrame(update);
    ctx.strokeStyle = '#FFFF00';
  } else if (progress < 0.48) {
    requestAnimationFrame(update);
    ctx.strokeStyle = '#00FF00';
  } else if (progress < 0.6) {
    requestAnimationFrame(update);
    ctx.strokeStyle = '#00FFFF';
  } else if (progress < 0.72) {
    requestAnimationFrame(update);
    ctx.strokeStyle = '#9D00FF';
  } else if (progress < 0.84) {
    requestAnimationFrame(update);
    ctx.strokeStyle = '#FF00FF';
  } else {
    requestAnimationFrame(update);
    ctx.strokeStyle = 'white';
  }
}
requestAnimationFrame(update);
