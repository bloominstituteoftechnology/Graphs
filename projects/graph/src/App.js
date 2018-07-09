import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 250; 

const canvasHeight = 250; 

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
    // compute connected components
    // draw edges
    // ctx.beginPath();
    // ctx.moveTo(0, 0);
    // // ctx.lineTo(300, 150);
    // ctx.stroke();
    
    // draw verts
    // draw vert values (labels)
    ctx.fillStyle = 'black';
    ctx.beginPath();
    ctx.arc(100, 100, 50, 0, 2 * Math.PI);
    // ctx.stroke();
    ctx.fill();


    ctx.fillStyle = 'white';
    ctx.beginPath();
    ctx.arc(100, 100, 30, 0, 2 * Math.PI);
    ctx.fill();

    ctx.fillStyle = 'black';
    ctx.beginPath();
    ctx.arc(200, 100, 50, 0, 2 * Math.PI);
    // ctx.stroke();
    ctx.fill();


    ctx.fillStyle = 'white';
    ctx.beginPath();
    ctx.arc(200, 100, 30, 0, 2 * Math.PI);
    ctx.fill();


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
