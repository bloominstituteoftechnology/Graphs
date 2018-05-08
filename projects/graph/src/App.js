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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.save();

    let x = 100;
    let y = 300;
    let newStart = 10;
    let color = '';
    const colors = [
      'rgba(255, 0, 0, .5)',
      'rgba(0,255,0,.5)',
      'rgba(0,0,255,.5)',
      'rgba(255,0,255,.5)',
    ];
    let count = 0;
    for (let i = 0; i < 100; i++) {
      for (let j = 0; j < 10; j++) {
        // if (j % 2 === 0) x = x + 30;
        color = colors[count];
        if (count === 4) count = 0;
        count++;
        ctx.strokeStyle = color;
        ctx.strokeRect(x, y, 75, 75);

        ctx.rotate(10 * Math.random() / 3);

        x = x * 0.4567;
      }
      if (newStart % 2 === 0) {
        newStart = newStart * 5;
        x = x * 3000;
        y = y * 0.3;
      } else {

        x = newStart * 100;
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
