import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 800;
 const canvasHeight = 400;
 let dx = Math.random() + 4 * 1.1;
 let x = Math.random() * 800;
 let y = Math.random() * 400;
 let dy = Math.random() + 4 * 1.1;
 const radius = 30;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    //this.updateCanvas();
    this.animateCircle();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    //this.updateCanvas();
    this.animateCircle();
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(10, 10, 200, 200);
   
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  }
  
  animateCircle = () => {
    
    let canvas = this.refs.canvas;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;
    let ctx = canvas.getContext('2d');


    requestAnimationFrame(this.animateCircle);
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2, false);
    ctx.strokeStyle = 'red';
    ctx.stroke();
    x += dx;
    y += dy;

    if(x + radius> canvasWidth || x - radius < 0){
      dx = -dx;
    }

    if(y + radius > canvasHeight || y - radius < 0){
      dy = -dy;
    }

    //setTimeout(this.animateCircle, 5000);
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
