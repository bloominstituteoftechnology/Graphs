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
    let radius = 50;

    // Clear it
    ctx.fillStyle = 'green';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    ctx.fillStyle = '#3BB9FF';
    ctx.fillRect(0, 0, 500, 200);

    // const grd = ctx.createLinearGradient(0, 0, 500, 0)
    // grd.addColorStop(0, "purple");
    // grd.addColorStop(1, "pink");

    ctx.fillStyle = 'yellow';
    ctx.arc(800 / 2, 150 / 2, radius, 0, 2 * Math.PI, false); 
    ctx.fill();


    ctx.fillStyle = 'ivory';
    ctx.fillRect(80, 150, 200, 200);
    
    ctx.fillStyle = 'brown';
    ctx.fillRect(100, 170, 50, 50);
    
    ctx.fillStyle = 'brown';
    ctx.fillRect(210, 170, 50, 50);

    ctx.fillStyle = 'gray';
    ctx.fillRect(153, 250, 50, 100);
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
