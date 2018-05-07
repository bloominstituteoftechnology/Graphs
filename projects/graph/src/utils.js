/**
 * Generate a random hex color.
 * Source: https://stackoverflow.com/questions/1484506/random-color-generator
 * @returns {string}
 */
export function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
