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
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Set up the gradient
    let grd = ctx.createLinearGradient(400, 50, 50, 90, 60, 100);
    grd.addColorStop(0, '#932fa3');
    grd.addColorStop(1, '#259ec6');

    // Fill with gradient
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Create circles in a loop
    ctx.strokeStyle = '#dce5e8';
    for (let i = 0; i < canvas.width; i += 18) {
      for (let j = 0; j < canvas.height; j += 10) {
        ctx.beginPath();
        ctx.arc(i, j, 40, 0, 2 * Math.PI);
        ctx.stroke();
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
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
