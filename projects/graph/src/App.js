import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
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
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // ------------- Happy Accident ---------------
    // for(let x = 0; x < canvasWidth; x++) {
    //   for(let y = 0; y < canvasHeight; y++) {
    //       const r = (Math.sqrt(y * (x/20))) % 255;
    //       const g = (Math.cos(x*y + Math.sin(y)) * 100) % 255;
    //       const b = (r*(y/(Math.PI*r)) + g) % 255;
          // ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
          // ctx.fillRect(x, y, 1, 1);
    //   }
    // }
    // -------------------------------------------

    ctx.beginPath();
    for(let x = 0; x < canvasWidth; x++) {
      for(let y = 0; y < canvasHeight; y++) {
        const r = Math.cos((Math.sqrt(y)*Math.tan(x)*-x)) % 255;
        const b = Math.tan((Math.sqrt(y)*Math.tan(x)*x)) % 255;
        const g = (b + (r + (Math.PI/2))) % 255;

        ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
        ctx.fillRect(x, y, 1, 1);
      }
    }

    ctx.globalAlpha = 0.01;
    ctx.lineWidth=0.5;
    // for(let i = 0; i < 50; i++) {
    //   // ctx.beginPath();
    //   // ctx.fillStyle = 'black';
    //   ctx.strokeStyle = 'rgb(200, 50, 100)';
    //   ctx.arc((Math.cos(i)*canvasWidth), (i)*10, Math.sqrt(i), 0, Math.PI * 2);
    //   // ctx.fill();
    //   ctx.stroke();
    //   ctx.closePath();
    // }
    ctx.beginPath();
    for(let i = 0; i < 50; i++) {
      // ctx.fillStyle = 'black';
      ctx.strokeStyle = 'rgb(200, 50, 100)';
      ctx.arc((i*i)/2, i*10, Math.sqrt(i), 0, Math.PI * 2);
      // ctx.fill();
      ctx.stroke();
      ctx.closePath();
    }
    ctx.beginPath();
    for(let i = 0; i < 50; i++) {
      // ctx.fillStyle = 'black';
      ctx.strokeStyle = 'rgb(200, 50, 100)';
      ctx.arc(Math.cos(i)*canvasWidth, i*10, Math.sqrt(i), 0, Math.PI * 2);
      // ctx.fill();
      ctx.stroke();
      ctx.closePath();
    }

    ctx.beginPath();
    ctx.fillStyle = 'white';
    ctx.strokeStyle = 'black';
    ctx.arc(canvasWidth/2, canvasHeight/2, 10, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();

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
