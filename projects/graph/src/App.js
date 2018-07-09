import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
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
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //========================================//
    ctx.fillStyle = 'yellow';
    ctx.fillRect(175, 200, 125, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(325, 200, 100, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(200, 175, 200, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(225, 150, 150, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(175, 225, 225, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(150, 250, 175, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(150, 275, 150, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(150, 300, 175, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(175, 325, 225, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(175, 350, 250, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(200, 375, 200, 25);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(225, 400, 150, 25);
    

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
