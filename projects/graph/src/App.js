import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;

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
    ctx.fillStyle = 'lightblue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    ctx.beginPath();
    ctx.arc(95, 50, 40, 0, 2 * Math.PI);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(700, 50, 40, 0, 2 * Math.PI);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(700, 400, 40, 0, 2 * Math.PI);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(95, 400, 40, 0, 2 * Math.PI);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(135, 50);
    ctx.lineTo(660, 50);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(95, 90);
    ctx.lineTo(95, 360);
    ctx.stroke();    

    ctx.beginPath();
    ctx.moveTo(95, 90);
    ctx.lineTo(95, 360);
    ctx.stroke();  

    ctx.beginPath();
    ctx.moveTo(135, 400);
    ctx.lineTo(660, 400);
    ctx.stroke();  

    ctx.beginPath();
    ctx.moveTo(700, 360);
    ctx.lineTo(700, 90);
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
