import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 900;
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
    ctx.fillStyle = '#c0dfe8';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    console.log(ctx);
    

    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(10, 10, 880, 780);

    ctx.fillStyle = '#bf9ebe';

    ctx.beginPath();
    ctx.arc(110, 180, 90, 0, Math.PI)
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(290, 180, 90, 1, Math.PI, true)
    ctx.fill();

    ctx.beginPath();
    ctx.moveTo(300, 250);
    
    ctx.stroke();



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
