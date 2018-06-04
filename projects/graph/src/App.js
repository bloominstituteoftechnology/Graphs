import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 900;
const canvasHeight = 700;

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
    let centerOfx = ctx.canvas.width / 3;
    let centerOfy = ctx.canvas.height / 4;

    let color = ctx.createRadialGradient(900, 700, 300, 300, 700, 900);
    color.addColorStop(0, 'gray');
    color.addColorStop(1, 'pink');
    
    // Clear it
    ctx.fillStyle = color;
    ctx.fillRect(10, 10, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    ctx.beginPath();
    for (let i = 0; i < 1500; i++) {
      let a = 2;
      let b = 2;
      const angle = 0.1 * i;
      let x = centerOfx + (a + b * angle) * Math.cos(angle);
      let y = centerOfy + (a + b * angle) * Math.sin(angle);

      ctx.lineTo(x, y);
    }
    ctx.strokeStyle = 'pink';
    ctx.stroke();

    ctx.beginPath();
    ctx.strokeStyle = 'black';
    ctx.moveTo(10, 10);
    ctx.lineTo(375, 745);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(900, 10);
    ctx.lineTo(375, 745);
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
