import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
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
    
    // Clear it    
    ctx.fillStyle = '#E91E63';
    ctx.fillRect(50, 50, canvasWidth, canvasHeight);
    ctx.fillStyle = 'blue';
    ctx.fillRect(150, 150, canvasWidth, canvasHeight);
    ctx.fillStyle = 'red';
    ctx.fillRect(300, 100, canvasWidth, canvasHeight);

    // ctx.moveTo(50, 20);
    // ctx.lineTo(200,100);
    // ctx.stroke();
    // ctx.strokeStyle="blue";
    // ctx.beginPath();
    // ctx.arc(295,100,28,0,2*Math.PI);
    // ctx.moveTo(300,0);
    // ctx.lineTo(300,100);
    // ctx.stroke();

    ctx.strokeStyle="#00B294";
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(0,100);
      ctx.lineTo(i * 8, 600);
      ctx.stroke();
    }
    
    ctx.strokeStyle="purple";
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(600,0);
      ctx.lineTo(i * 8, 600);
      ctx.stroke();
    }

    ctx.strokeStyle = 'orange';
    for (let i =0; i < 150; i++) {
      ctx.beginPath();
      ctx.moveTo(Math.cos(i) * 10, Math.sin(1) * 10);
      ctx.lineTo(Math.sin(i) * 200, Math.cos(i) * 200);
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
