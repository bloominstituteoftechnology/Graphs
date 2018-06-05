import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
const canvasHeight = 400;

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
  // START FO MY CUSTOM FUNCTIONS

  draw(canvas, ctx) {
    ctx.fillStyle = 'lightblue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // // Create a gradient
    const rGrd = ctx.createRadialGradient(75, 50, 5, 90, 60, 100);
    rGrd.addColorStop(0, 'orange');
    rGrd.addColorStop(0.5, 'yellow');
    rGrd.addColorStop(1, 'lightblue');

    // // Fill with gradient
    ctx.fillStyle = rGrd;
    ctx.fillRect(0, 0, 200, 150);

    // Create gradient
    const lGrd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
    lGrd.addColorStop(0, 'blue');
    lGrd.addColorStop(0.5, 'yellow');
    lGrd.addColorStop(1, 'brown');

    // Fill with gradient
    ctx.fillStyle = lGrd;
    ctx.fillRect(0, 200, canvasWidth, canvasHeight);
  }

  // END OF MY CUSTOM FUNCTIONS
  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    this.draw(canvas, ctx);

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
