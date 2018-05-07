import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 400; 
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

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'red';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    // !!! IMPLEMENT ME
    
    // grad
    let grd = ctx.createLinearGradient(0, 200, 200, 20);
    grd.addColorStop(0, "gold");
    grd.addColorStop(1, "silver");
    
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // e
    
    // c1
    ctx.beginPath();
    ctx.globalAlpha = 0.4;
    ctx.arc(200, 175, 40, 0, 2 * Math.PI);
    ctx.fillStyle = "red";
    ctx.fill();
    // ec1
  
    // c2
    ctx.beginPath();
    ctx.arc(180, 210, 40, 0, 2 * Math.PI);
    ctx.fillStyle = "green";
    ctx.fill();
    // ec2

    // c3
    ctx.beginPath();
    ctx.arc(220, 210, 40, 0, 2 * Math.PI);
    ctx.fillStyle = "blue";
    ctx.fill();
    // ec3

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
