import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 400; 
const canvasHeight = 400;

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

    ctx.beginPath();
    ctx.arc(200,200,190,0,2*Math.PI);
    ctx.fillStyle = '#f2f000';
    ctx.lineWidth = 10;
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(210,120,10,0,2*Math.PI);
    ctx.fillStyle = 'black';
    ctx.lineWidth = 10;
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(400, 400);
    ctx.lineTo(200, 200);
    ctx.lineTo(400, 20);
    ctx.fillStyle = 'white';
    ctx.lineWidth = 10;
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = 'white';
    ctx.fillRect(342, 0, 70, 100);

    ctx.fillStyle = 'white';
    ctx.fillRect(335, 320, 70, 100);


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
