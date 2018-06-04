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
    var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
    grd.addColorStop(0, 'black');
    grd.addColorStop(1, 'white');
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let i = 0; i <= canvasWidth; i = i + 50) {
      ctx.moveTo(i, 0);
      ctx.lineTo(canvasWidth - i, canvasHeight);
    }
    for (let i = 50; i < canvasHeight; i = i + 50) {
      ctx.moveTo(0, i);
      ctx.lineTo(canvasWidth, canvasHeight - i);
    }

    for (let i = 0; i < 0.5; i = i + (0.6 - i) * 0.15) {}

    ctx.stroke();
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
