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
    // ctx.moveTo(80,80);
    for (var i = 0; i < 100; i++) {
      for (var j = 0; j < 100; j++) {
        for (var p = 0; p < 100; p++) {
        ctx.fillStyle = `rgb(${Math.floor(255 - 10.5 * i)}, ${Math.floor(255 - 10.5 * j)}, ${Math.floor(255 - 10.5 * p)})`;
        ctx.fillRect(j * 25, i * 25, 25, 25);
        }
      }
    }
    for (var i = 0; i < 20; i++) {
      if (ctx.lineWidth > 10) {
        ctx.lineWidth = 1;
      } else {
        ctx.lineWidth = 1 + i;
      }
      ctx.beginPath();
      ctx.moveTo(1 + i + 20, i + 1);
      ctx.lineTo(1 + i * 80, 500);
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
