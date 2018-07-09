import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 500;
 const canvasHeight = 300;

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
    ctx.fillStyle = 'teal';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges

    ctx.fillStyle = 'yellow';
    ctx.beginPath();
    ctx.moveTo(25, 25);
    ctx.lineTo(105, 25);
    ctx.lineTo(25, 105);
    ctx.fill();

    // Stroked triangle
    ctx.beginPath();
    ctx.moveTo(125, 125);
    ctx.lineTo(125, 45);
    ctx.lineTo(45, 125);
    ctx.closePath();
    ctx.stroke();

    ctx.font = "70px Arial";
    ctx.fillText("Hey CS9", 120, 190);
    

    ctx.fillStyle = 'black';
    ctx.beginPath();
    ctx.arc(395, 60, 40, 0, 2 * Math.PI);
    ctx.fill();

    ctx.fillStyle = 'white';
    ctx.beginPath();
    ctx.arc(298, 10, 50, 0, 2 * Math.PI);
    ctx.fill();


    ctx.fillStyle = 'white';
    ctx.beginPath();
    ctx.arc(213, 60, 23, 0, 2 * Math.PI);
    ctx.fill();

    ctx.fillStyle = 'white';
    ctx.beginPath();
    ctx.arc(213, 240, 23, 0, 2 * Math.PI);
    ctx.fill();


    ctx.fillStyle = 'white';
    ctx.beginPath();
    ctx.arc(298, 300, 50, 0, 2 * Math.PI);
    ctx.fill();
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
