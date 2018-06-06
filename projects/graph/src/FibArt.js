import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 1000;

function recur(num) {
  function fibonacci(num, memo = {}) {
    if (memo[num]) return memo[num];
    if (num <= 1) return 1;

    return (memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo));
  }
  let x = fibonacci(num);
  return x;
}
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

    var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
    grd.addColorStop(0, 'black');

    grd.addColorStop(0.99, 'red');

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

      // for (let i = 0; i < 100; i++) {
      //   ctx.strokeStyle = 'white';
      //   let x = recur(i);
      //   ctx.lineWidth = 1;
      //   ctx.moveTo(100 + i, i);
      //   ctx.bezierCurveTo(i, i, x, x, x, x * Math.PI);
      //   ctx.lineTo(x * i, x * i);
      //   ctx.stroke();
      //   ctx.strokeStyle = 'blue';
      //   ctx.bezierCurveTo(i, i, -x, x, x, x * Math.PI);
      //   ctx.stroke();
      // }
      for (let i = 0; i < 100; i++) {
        let x = recur(i);
        ctx.beginPath();
        ctx.moveTo(i * x, i * x);
        ctx.arc(x, x, i, 0, 2 * Math.PI, false);
        ctx.fillStyle = 'yellow';
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.lineTo(x + x, i * x);
        ctx.strokeStyle = 'black';
        ctx.stroke();
        ctx.closePath();
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
class App2 extends Component {
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

export default App2;
