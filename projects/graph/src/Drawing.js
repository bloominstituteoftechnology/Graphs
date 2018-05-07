// Sample code for creating randomized circle drawing

/*

const roundColor = () => {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
};

for (let i = 0; i < 1000; i++) {
  ctx.moveTo(
    Math.floor(Math.random() * canvas.width) / 3,
    Math.floor(Math.random() * canvas.height) / 3
  );
  ctx.beginPath();
  ctx.fillStyle = roundColor();
  ctx.arc(
    i % 2 === 0
      ? canvas.width / 2 + i * Math.random()
      : canvas.width / 2 - i * Math.random(),
    i % 2 === 0
      ? canvas.height / 2 + i * Math.random()
      : canvas.height / 2 - i * Math.random(),
    Math.floor(Math.random() * 25),
    0,
    Math.PI * 2,
    false
  ); // Outer circle
  ctx.stroke();
}

*/