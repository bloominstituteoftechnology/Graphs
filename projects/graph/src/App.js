import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 400;
const canvasHeight = 300;

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
    //ctx.fillStyle = '#0FFFFF';
    //ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    var grd = ctx.createLinearGradient(0, 500, 0, 0);
    grd.addColorStop(0, '#000000');
    grd.addColorStop(1, '#028187');

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let i = 0; i < 50; i++) {
      ctx.beginPath();
      ctx.arc(
        Math.random() * (20 * i),
        Math.random() * (20 * i),
        10,
        0,
        2 * Math.PI,
      );
      ctx.strokeStyle = '#FFFFFF';
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
