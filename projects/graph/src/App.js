import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1024;
const canvasHeight = 768;

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
    // ctx.fillStyle = 'white';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    let bckgrnd = ctx.createRadialGradient(canvasWidth/2, canvasHeight, canvasWidth/Math.PI, canvasWidth, canvasHeight, canvasWidth);
    bckgrnd.addColorStop(0, "navy");
    bckgrnd.addColorStop(1,"black");

    ctx.fillStyle = bckgrnd;
    ctx.fillRect(10, 10, canvasWidth,canvasHeight);

    ctx.beginPath();
    ctx.arc(canvas.width/2, canvas.height/2, 75, 1.1*Math.PI, 1.9*Math.PI, false);
    ctx.lineWidth = 15;
    ctx.strokeStyle = "bckgrnd";
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
