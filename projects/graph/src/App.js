import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 400;
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
    ctx.fillStyle = 'lightgreen';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    ctx.fillStyle = 'lightblue';
    ctx.fillRect(30, 30, 90, 90);

    ctx.lineTo(100, 300);
    ctx.lineTo(40,50);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(300, 50, 10, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.moveTo(200, 200);

    ctx.strokeStyle = 'blue';

    for(let i = 0; i < 200; i++) {
      ctx.beginPath();
      ctx.moveTo(0,Math.cos(i) * 600);
      ctx.arc(350, 150, 40, 0, 2 * Math.PI);
      ctx.stroke();
    }
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
