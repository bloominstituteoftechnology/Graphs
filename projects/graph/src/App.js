import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 16 * 50;
const canvasHeight = 9 * 50;

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
    ctx.save();

    let x = 100;
    let y = 500;
    let newStart = 10;

    for (let i = 0; i < 60; i++) {

      for (let j = 0; j < 10; j++) {
        // if (j % 2 === 0) x = x + 30;
        ctx.strokeStyle = 0x02031;
        ctx.strokeRect(x, y, 50, 50)
        ctx.rotate(((100 * Math.random()) / 2));
        x = x*.3;
        y = y *1;
      }
      if(newStart % 2 === 0) {
        newStart = newStart * 5;
        x = ~x * 1000;
        y = ~y;

      }
      else { 
        newStart = newStart;
        x = newStart;
      }
      // y = y*i-50;
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
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph(),
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
