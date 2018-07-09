import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 550;

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
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'purple';
    ctx.fillRect(0, 25, canvasWidth, canvasHeight);

    ctx.fillStyle = 'pink';
    ctx.fillRect(10, 25, canvasWidth, 40);

    ctx.fillStyle = 'pink';
    ctx.fillRect(10, 75, canvasWidth, 30);

    ctx.fillStyle = 'pink';
    ctx.fillRect(10, 115, canvasWidth, 20);

    ctx.fillStyle = 'pink';
    ctx.fillRect(10, 147, canvasWidth, 18);

    ctx.fillStyle = 'pink';
    ctx.fillRect(10, 175, canvasWidth, 14);

    ctx.fillStyle = 'pink';
    ctx.fillRect(10, 198, canvasWidth, 5);

    ctx.fillStyle = 'teal';
    ctx.fillRect(0, 10, 200, 200)

    ctx.fillStyle = 'yellow';
    ctx.beginPath();
    ctx.moveTo(250, 250);
    ctx.lineTo(105, 25);
    ctx.lineTo(25, 105);
    ctx.fill();

    

    



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
