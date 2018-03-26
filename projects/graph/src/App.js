import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

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
    const getRndColor = () => {
      return '#' + Math.floor(Math.random() * 16777215).toString(16);
    } 
    // Clear it
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    for(let i = 0; i < 1000; i++)
    {    
      ctx.moveTo(Math.floor( Math.random() * canvas.width ) / 3, Math.floor( Math.random() * canvas.height ) / 3);
      ctx.beginPath();
      ctx.fillStyle = getRndColor();
      ctx.arc( (i % 2 === 0) ? canvas.width/2 + i * Math.random() : canvas.width/2 - i* Math.random(), (i % 2 === 0) ? canvas.height/2 + i * Math.random(): canvas.height/2 - i* Math.random(), Math.floor(Math.random() * 25), 0, Math.PI * 2, false); // Outer circle
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
