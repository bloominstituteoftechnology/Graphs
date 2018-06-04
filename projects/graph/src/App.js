import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;

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
    // ctx.fillStyle = 'mistyrose';
    // ctx.fillRect(200, 200, canvasWidth, canvasHeight);
    // ctx.fillStyle = 'red';
    // ctx.fillRect(50, 50, 50, 50);
    // ctx.fillStyle = 'blue';
    // ctx.fillRect(250, 250, 25, 25);

    // ctx.moveTo(50, 20);
    // ctx.lineTo(500, 900);
    // ctx.stroke();
    // ctx.strokeStyle = '#FF0000';

    // ctx.lineTo(50, 200);
    // ctx.lineTo(500, 20);
    // ctx.lineTo(75, 100);
    // ctx.stroke();

    // ctx.beginPath();
    // ctx.moveTo(135, 50);
    // ctx.arc(95, 50, 40, 0, 2 * Math.PI);
    // ctx.moveTo(200, 250);
    // ctx.arc(200, 250, 40, 0, 1 * Math.PI);
    // ctx.moveTo(300, 50);
    // ctx.arc(300, 50, 40, 0, 2 * Math.PI);
    // ctx.stroke();

    // ctx.strokeStyle = 'blue';
    // for (let i = 0; i < 150; i++) {
    //   ctx.beginPath();
    //   ctx.moveTo(0, 0);
    //   ctx.lineTo(i * 10, 600);
    //   ctx.stroke();
    // }

    // ctx.strokeStyle = 'chartreuse';
    // for (let i = 0; i < 150; i++) {
    //   ctx.beginPath();
    //   ctx.moveTo(Math.cos(i) * 100, Math.sin(i) * 100);
    //   ctx.lineTo(Math.sin(i) * 600, Math.cos(i) * 600);
    //   ctx.stroke();
    // }

    // set up the gradient
    let grd = ctx.createLinearGradient(500, 50, 50, 90, 60, 100);
    grd.addColorStop(0, '#333F48');
    grd.addColorStop(1, '#B9975B');

    // Fill with gradient
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // ctx.beginPath();
    // ctx.arc(400, 300, 40, 0, 2 * Math.PI);
    // ctx.stroke();
    // ctx.strokeStyle = '#C8102E';
    // ctx.fillStyle = '#333F48';
    // ctx.fill();

    // // ctx.strokeStyle = '#C8102E';
    // // for (let i = 0; i < 50; i++) {
    // //   ctx.beginPath();
    // //   ctx.moveTo(0, 0);
    // //   ctx.lineTo(i * 10, 600);
    // //   ctx.stroke();
    // // }

    // ctx.strokeStyle = '#C8102E';
    // for (let i = 0; i < 150; i++) {
    //   ctx.beginPath();
    //   ctx.moveTo(Math.cos(i) * 100, Math.sin(i) * 100);
    //   ctx.lineTo(Math.sin(i) * 600, Math.cos(i) * 600);
    //   ctx.stroke();
    // }

    // ctx.font = '50px Arial';
    // ctx.fillStyle = '#C8102E';
    // ctx.fillText('Vegas Golden Knights', 150, 60);

    // create circles in a loop
    ctx.strokeStyle = '#B9975B';
    for (let i = 0; i < canvas.width; i += 15) {
      for (let j = 0; j < canvas.height; j += 15) {
        // ctx.fillRect(x, y, 20, 20);
        ctx.beginPath();
        ctx.arc(i, j, 40, 0, 2 * Math.PI);
        ctx.stroke();
        // ctx.strokeStyle = '#B9975B';
      }
    }

    // ctx.moveTo(100, 100);
    // ctx.lineTo(300, 100);
    // ctx.strokeStyle = '#C8102E';
    // ctx.stroke();

    // ctx.moveTo(100, 100);
    // ctx.lineTo(100, 300);
    // ctx.strokeStyle = '#C8102E';
    // ctx.stroke();

    // ctx.moveTo(300, 100);
    // ctx.lineTo(300, 300);
    // ctx.strokeStyle = '#C8102E';
    // ctx.stroke();

    // ctx.moveTo(100, 300);
    // ctx.lineTo(200, 400);
    // ctx.strokeStyle = '#C8102E';
    // ctx.stroke();

    // ctx.moveTo(300, 300);
    // ctx.lineTo(200, 400);
    // ctx.strokeStyle = '#C8102E';
    // ctx.stroke();

    // ctx.beginPath();
    // ctx.arc(150, 150, 0, 10, 10);
    // ctx.strokeStyle = '#C8102E';
    // ctx.stroke();

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
