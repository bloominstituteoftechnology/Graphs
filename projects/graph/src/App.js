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
        - lineTo(): Adds a new point and creates a line to that point from the last specified point in the canvas | use to have multiple lines/edges
        - stroke(): Actually draws the path you have defined
    */
    ctx.fillStyle = 'blue';
    ctx.fillRect(200, 20, 200, 180);
    ctx.beginPath();
    ctx.moveTo(50,40);
    ctx.lineTo(10,10);
    ctx.lineTo(350,10);
    ctx.lineTo(450,430);
    ctx.stroke();  

    /*
      Verts/Nodes (circles) 
        - void ctx.arc(x, y, radius, startAngle, endAngle [, anticlockwise]);
          * x coord of arc's center
          * y coord of arc's center
          * arc's radius
          * startAngle = angle which arc starts measured clockwise from positive x axis and expressed in radians
          * endAngle = angle which arc starts measured clockwise from positive x axis and expressed in radians
    */

    ctx.fillStyle = 'purple';
    ctx.fillRect(400, 350, 100, 100);
    ctx.beginPath();
    ctx.arc(450, 400, 100, 0, 2 * Math.PI);
    ctx.stroke();

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
