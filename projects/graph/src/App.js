import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 700;
 const canvasHeight = 480;

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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth,  canvasHeight);
    ctx.fillStyle = 'blue';
    ctx.fillRect(10, 10, 20, 20);

    ctx.moveTo(25, 299);
    ctx.lineTo(400, 300);
    ctx.lineTo(452, 378);
    ctx.lineTo(35, 222);
    ctx.moveTo(0, 0);
    ctx.lineTo(255, 255);
    ctx.stroke();

    let grd = ctx.createLinearGradient(0, 0, canvasWidth, 0);
    grd.addColorStop(0, "blue");
    grd.addColorStop(1, "white");

    // Fill with gradient
    ctx.fillStyle = grd;
    ctx.fillText('Mark', canvasWidth / 2, canvasHeight /2);
    ctx.moveTo(45, 120);
    ctx.lineTo(255, 255);
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
