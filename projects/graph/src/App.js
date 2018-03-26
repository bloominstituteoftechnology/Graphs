import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 700;
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
    ctx.fillStyle = '#FF0000';
    ctx.fillStyle = "lightgray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    // line 1
    ctx.moveTo(50, 50);
    ctx.lineTo(100, 100);
    ctx.stroke();

    // node 1
    ctx.beginPath();
    ctx.moveTo(60, 50);
    ctx.arc(50, 50, 10, 0, 2 * Math.PI, true);
    ctx.fill();
    ctx.stroke();

    // num 1
    ctx.beginPath();
    ctx.font = "10px Helvetica";
    ctx.strokeText("1", 48, 53);
    ctx.stroke();

    // node 2
    ctx.arc(100, 100, 10, 0, 2 * Math.PI, true);
    ctx.fill();
    ctx.stroke();

    // num 2
    ctx.font = "10px Helvetica";
    ctx.strokeStyle = "black";
    ctx.strokeText("2", 98, 102);
    ctx.stroke();

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
