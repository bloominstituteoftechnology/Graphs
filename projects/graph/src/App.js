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

    

    /*
    // sky
    ctx.fillStyle = 'blue';
    var gradient = ctx.createLinearGradient(0, 120, 0, 400);
    gradient.addColorStop(0, "cyan");
    gradient.addColorStop(1, "blue");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // beach
    ctx.fillStyle = "yellow";
    ctx.fillRect(0, 400, 500, 100);

    // sun
    ctx.beginPath();
    ctx.arc(20, 20, 90, 0, 2*Math.PI);
    ctx.fillStyle = "orange";
    ctx.fill();

    // sun rays
    ctx.strokeStyle = "orange";
    ctx.moveTo(140, 15);
    ctx.lineTo(210, 17);
    ctx.moveTo(130, 70);
    ctx.lineTo(190, 100);
    ctx.moveTo(80, 110);
    ctx.lineTo(130, 180);
    ctx.moveTo(30, 135);
    ctx.lineTo(45, 200);
    ctx.stroke();
    
    // sand (don't tell Anakin)
    for(var i = 0; i < 300; i++) {
      ctx.strokeStyle = 'salmon';
      ctx.moveTo(4 * i, 400);
      ctx.lineTo(5.75 * i, 500);
      ctx.stroke();
    }

    // seafoam
    ctx.strokeStyle = 'rgba(255, 255, 255, .5)';
    for (var j = 0; j < 400; j++) {
      ctx.moveTo(500, 390);
      ctx.lineTo(4 * j, 400);
    }
    ctx.stroke();
    */


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
