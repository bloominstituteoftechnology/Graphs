import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

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
    ctx.fillStyle = 'teal';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    let grd = ctx.createRadialGradient(75,50,15,100,50,100);
    grd.addColorStop(0,"blue");
    grd.addColorStop(1,"white");


    ctx.fillStyle = grd;
    ctx.fillRect(10,10,350,350);

    let grd2 = ctx.createRadialGradient(75,50,15,100,50,100);
    grd2.addColorStop(0,"green");
    grd2.addColorStop(1,"white");

    ctx.fillStyle = grd2;
    ctx.fillRect(5,5,100,100);


    
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
