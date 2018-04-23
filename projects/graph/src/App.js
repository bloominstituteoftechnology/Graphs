import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 640;
const canvasHeight = 480;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvas();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvas();
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const factor = 10;
    // let grid = {};
    const num_items = 10;
    // const delay = 5;

    const colors = {
      0: 'red',
      1: 'blue',
      2: 'green',
      3: '#b3e0f2',
      4: 'yellow',
    };

    const getRandomRGB = _ => {
      return colors[Math.floor(Math.random() * Object.keys(colors).length)];
      // console.log(`rgb(${num1}, ${num2}, ${num3}`);
      // return `rgb(${num1}, ${num2}, ${num3}`;
    };

    const getRandomPos = max => {
      return Math.floor(Math.random() * max);
    };

    const drawRandomCircle = _ => {
      const r = factor;

      ctx.beginPath();
      ctx.arc(
        getRandomPos(canvasWidth),
        getRandomPos(canvasHeight),
        r,
        0,
        2 * Math.PI,
      );
      ctx.stroke();
      ctx.fillStyle = getRandomRGB();
      ctx.fill();
    };

    const drawRandomRect = _ => {
      const w = factor * 2;
      const h = factor * 2;

      ctx.rect(getRandomPos(canvasWidth), getRandomPos(canvasHeight), w, h);
      ctx.stroke();
      ctx.fillStyle = getRandomRGB();
      ctx.fill();
    };

    const drawRandomTriangle = _ => {
      const b = factor * 2;
      const h = 3 ** 0.5 * factor;

      const x_pos = getRandomPos(canvasWidth);
      const y_pos = getRandomPos(canvasHeight);

      ctx.beginPath();
      ctx.fillStyle = getRandomRGB();
      ctx.fill();
      ctx.moveTo(x_pos, y_pos);
      ctx.moveTo(x_pos, y_pos + -h / 2);
      ctx.lineTo(x_pos + -b / 2, y_pos + h / 2);
      ctx.lineTo(x_pos + b / 2, y_pos + h / 2);
      ctx.lineTo(x_pos, y_pos - h / 2);
    };

    const getRandomInt = max => {
      return Math.floor(Math.random() * max);
    };

    // let count = 0;

    // var counter = setInterval(_ => {
    //   const num = getRandomInt(3);
    //   switch (num) {
    //     case 0:
    //       drawRandomCircle();
    //       break;
    //     case 1:
    //       drawRandomRect();
    //       break;
    //     case 2:
    //       drawRandomTriangle();
    //       break;

    //     default:
    //       console.log('default');
    //   }
    //   count++;
    // }, delay);

    // while (1) {
    //   if (count > num_items) {
    //     clearInterval(counter);
    //     break;
    //   }
    // }

    for (let i = 0; i < num_items; i++) {
      const num = getRandomInt(3);
      switch (num) {
        case 0:
          drawRandomCircle();
          break;
        case 1:
          drawRandomRect();
          break;
        case 2:
          drawRandomTriangle();
          break;

        default:
          console.log('default');
      }
    }

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph(),
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
