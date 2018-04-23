import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 640;
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
    ctx.fillStyle = 'lightblue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // graph paper - vertical lines
    // for (let x = 20; x < canvasWidth; x += 20) {
    // ctx.moveTo(x, 0);
    // ctx.lineTo(x, canvasHeight);
    // ctx.stroke();
    // }

    // graph paper - horizontal lines
    // for (let y = 20; y < canvasHeight; y += 20) {
    //   ctx.moveTo(0, y);
    //   ctx.lineTo(canvasWidth, y);
    //   ctx.stroke();
    // }
    
    ctx.fillStyle = '#000000';
    // head
    ctx.beginPath();
    ctx.arc(canvasWidth / 2, canvasHeight / 2, 100, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    // left ear
    ctx.beginPath();
    ctx.arc(canvasWidth / 2 - 100, canvasHeight / 2 - 110, 60, .43 * Math.PI, .1 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // right ear
    ctx.beginPath();
    ctx.arc(canvasWidth / 2 + 100, canvasHeight / 2 - 110, 60, .9 * Math.PI, .57 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // chin
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(canvasWidth / 2, canvasHeight / 2 + 70, 50, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // left cheek
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 - 50, canvasHeight / 2 + 60, 65, 30, 1.20 * Math.PI, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // right cheek
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 + 50, canvasHeight / 2 + 60, 65, 30, .8 * Math.PI, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(canvasWidth / 2, canvasHeight / 2 + 20, 50, 0, 2 * Math.PI);
    ctx.fill();
    // chin
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(canvasWidth / 2, canvasHeight / 2 + 70, 49, 0, 2 * Math.PI);
    // ctx.stroke();
    ctx.fill();
    // left eye background
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 - 27, canvasHeight / 2, 50, 85, 1.97 * Math.PI, 0, 2 * Math.PI);
    // ctx.stroke();
    ctx.fill();
    // right eye background
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 + 27, canvasHeight / 2, 50, 85, .03 * Math.PI, 0, 2 * Math.PI);
    // ctx.stroke();
    ctx.fill();
    // left eye white
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 - 16, canvasHeight / 2 - 20, 10, 30, 1.98 * Math.PI, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // right eye white
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 + 16, canvasHeight / 2 - 20, 10, 30, .02 * Math.PI, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // left eye black
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 - 13, canvasHeight / 2 - 4, 7, 14, 0, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // right eye black
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 + 15, canvasHeight / 2 - 4, 7, 14, 0, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // above-nose arch
    ctx.beginPath();
    ctx.arc(canvasWidth / 2, canvasHeight / 2 + 58, 50, 1.36 * Math.PI, 1.64 * Math.PI);
    ctx.stroke();
    // lower mouth
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2, canvasHeight / 2 + 50, 40, 55, 0, .15 * Math.PI, .85 * Math.PI);
    ctx.fill();
    // mouth
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2, canvasHeight / 2 + 20, 85, 60, 0, 0.1 * Math.PI, 0.9 * Math.PI);
    ctx.stroke();
    ctx.fill();
    // nose
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2, canvasHeight / 2 + 30, 25, 12, 0, 0, 2 * Math.PI);
    ctx.fill();
    // left cheek arch
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 - 76, canvasHeight / 2 + 42, 12, 5, 0, 1.1 * Math.PI, 1.6 * Math.PI);
    ctx.stroke();
    // right cheek arch
    ctx.beginPath();
    ctx.ellipse(canvasWidth / 2 + 76, canvasHeight / 2 + 42, 12, 5, 0, 1.4 * Math.PI, 1.9 * Math.PI);
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
