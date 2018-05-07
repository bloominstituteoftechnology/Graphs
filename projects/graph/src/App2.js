import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

function recur(num) {
  function fibonacci(num, memo) {
    memo = memo || {};

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

    for (let i = 0; i < 100; i++) {
      ctx.strokeStyle = 'white';
      let x = recur(i);
      ctx.lineWidth = 1;
      ctx.moveTo(x, x);
      ctx.bezierCurveTo(i, i, x * i, x / i, x * x, x * Math.PI);
      ctx.lineTo(x + i, x + i);
      ctx.lineTo(x * i, x * i);
      ctx.lineTo(x - i, x - i);
      ctx.lineTo(x / i, x / i);
      ctx.stroke();
      ctx.bezierCurveTo(x, x, x, x, x, x * Math.PI);
      ctx.moveTo(i + 200, i + 200);
      ctx.stroke();
      ctx.bezierCurveTo(x, x, x, x, x, x * Math.PI);
      ctx.moveTo(i + 300, i + 300);
      ctx.stroke();
      ctx.bezierCurveTo(x, x, x, x, x, x * Math.PI);
      ctx.moveTo(i + 400, i + 400);
      ctx.stroke();
      ctx.bezierCurveTo(x, x, x, x, x, x * Math.PI);
      ctx.stroke();
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
