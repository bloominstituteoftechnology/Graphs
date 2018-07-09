import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';
import { randomFill } from 'crypto';

// !!! IMPLEMENT ME
const canvasWidth = 600;
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

    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');

    var grd = ctx.createLinearGradient(0,100,0,0);
    grd.addColorStop(0,"gold");
    grd.addColorStop(1,"white");
    
    
    // Clear it
    ctx.fillStyle = 'teal';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, 300, canvasHeight);

    ctx.fillStyle = 'green';
    ctx.beginPath();
    ctx.arc(105,150,40,0,2*Math.PI);
    ctx.stroke();

    ctx.fillStyle = 'green';
    ctx.moveTo(25,320);
    ctx.lineTo(280,500);
    ctx.stroke();

    // Create gradient

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
