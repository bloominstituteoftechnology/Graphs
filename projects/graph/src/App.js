import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 700;

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
    ctx.fillStyle = 'orange';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Compute Connected Components
    
    /* 
      Edges (lines) 
        - beginPath(): Begins a path, or resets the current path
        - moveTo(): Moves the path to the specified point in the canvas, without creating a line
        - lineTo(): Adds a new point and creates a line to that point from the last specified point in the canvas
        - stroke(): Actually draws the path you have defined
    */
    ctx.fillStyle = 'blue';
    ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.lineTo(300,150);
    ctx.stroke();  


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
