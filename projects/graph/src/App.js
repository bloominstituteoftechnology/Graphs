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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    const g = new Graph();
    g.randomize(100, 100, 300, 23);
    g.dump();

    ctx.fillStyle = 'green';
  

    // step to drawing a simple line from one coordinate to the nexts
    ctx.beginPath();
    ctx.moveTo(100, 100);
    ctx.lineTo(400, 400);
    ctx.closePath();
    ctx.stroke();

    // x, y, radius, start angle, end angle, anticlockwise(defaults to clockwise)
    ctx.arc(50, 100, 10, 0, 360);
    ctx.stroke();
    ctx.fillRect(100, 100, 100, 100);
    ctx.fillRect(400, 400, 50, 50);
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
    this.state.graph.randomize(canvasWidth, canvasHeight, 23);
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
