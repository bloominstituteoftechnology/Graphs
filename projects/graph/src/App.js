import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 800;
const canvasHeight = 600;

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
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    function getRandomColor() {
      return Math.floor(Math.random() * (255 - 0 + 1)) + 0;
    }

    ctx.lineWidth = 3;
    ctx.shadowColor = 'black';
    ctx.shadowOffsetX = 6;
    ctx.shadowBlur = 10;

    // ctx.beginPath();
    // for (let i = 0; i < canvasHeight; i++) {
    //   ctx.lineTo(i, Math.floor(Math.random() * canvasHeight) * i);
    //   ctx.lineTo(Math.floor(Math.random() * canvasWidth) * i, i);
    //   ctx.stroke();
    //   ctx.strokeStyle = `rgb(${getRandomColor()}, ${getRandomColor()}, ${getRandomColor()})`;
    // }

    //const intervalID = window.setInterval(cb, 1);

    // ctx.beginPath();
    // for (let i = 0; i < canvasWidth; i++) {
    //   ctx.strokeStyle = `rgb(${getRandomColor()}, ${getRandomColor()}, ${getRandomColor()})`;
    //   ctx.arc(Math.floor(Math.random() * canvasHeight) * i, Math.floor(Math.random() * canvasHeight) / i, Math.floor(Math.random() * canvasHeight), Math.floor(Math.random() * canvasHeight), Math.floor(Math.random() * canvasHeight), false);
    //   ctx.stroke();
    // }

    let i = 0;

    // function cb() {
    //   ctx.fillStyle = 'white';
    //   ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    //   ctx.fillStyle = 'black';
    //   ctx.fillRect(70,0,100,30);
    //   ctx.rotate(45 * Math.PI / i++);
    // }

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
