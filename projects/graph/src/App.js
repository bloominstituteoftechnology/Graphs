import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

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
    grd.addColorStop(0, '#000000');
    grd.addColorStop(0.1, '#3c0045');
    grd.addColorStop(0.2, '#fe008d');
    grd.addColorStop(0.3, '#ff6a00');
    grd.addColorStop(0.4, '#fffc00');
    grd.addColorStop(0.5, '#70ff00');
    grd.addColorStop(0.6, '#00ff2e');
    grd.addColorStop(0.7, '#00b7ff');
    grd.addColorStop(0.8, '#9b0004');
    grd.addColorStop(0.9, '#cc7274');
    grd.addColorStop(1, '#ffffff');

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let i = 0; i < 25; i++) {
      ctx.beginPath();
      ctx.arc(25 + i * i, 15 + i * i, i / 1.5, 0, 2 * Math.PI, false);
      ctx.arc(25 + i * i - i - i, 15 + i * i, i / 1.5, 0, 2 * Math.PI, false);
      ctx.arc(25 + i * i + i + i, 15 + i * i, i / 1.5, 0, 2 * Math.PI, false);
      ctx.arc(25 + i * i - i * 3, 15 + i * i, i / 1.5, 0, 2 * Math.PI, false);
      ctx.arc(25 + i * i + i * 3, 15 + i * i, i / 1.5, 0, 2 * Math.PI, false);
      ctx.arc(25 + i * i - i * 5, 15 + i * i, i / 1.5, 0, 2 * Math.PI, false);
      ctx.arc(25 + i * i + i * 5, 15 + i * i, i / 1.5, 0, 2 * Math.PI, false);
      if (i < 10) ctx.fillStyle = 'green';
      else if (i >= 10 && i < 15) ctx.fillStyle = 'white';
      else if (i >= 15 && i < 20) ctx.fillStyle = 'red';
      else if (i >= 20 && i <= 25) ctx.fillStyle = 'black';
      ctx.fill();
      ctx.lineWidth = 2;
      if (i < 10) ctx.strokeStyle = 'pink';
      else if (i >= 10 && i < 15) ctx.strokeStyle = 'purple';
      else if (i >= 15 && i < 20) ctx.strokeStyle = 'black';
      else if (i >= 20 && i <= 25) ctx.strokeStyle = 'yellow';
      ctx.stroke();
      ctx.closePath();
    }

    for (let i = 0; i < 500; i++) {
      ctx.strokeStyle = '#0011aa';
      ctx.lineWidth = 1;
      ctx.globalAlpha = 0.01;
      ctx.moveTo(i * 3, i * i);
      ctx.bezierCurveTo(i + 5, i, i * i, i + i, i, i);
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
