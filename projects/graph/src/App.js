import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1250;
const canvasHeight = 300;

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
    
    ctx.fillStyle = 'tan' 
    ctx.fillRect(0, 0, 480, 450)
    ctx.fillStyle = 'grey'
    ctx.fillRect(10, 10, 460, 275)

    const X = 85, W = 60, G = 30
    ctx.lineWidth = 10
    const colors = ['blue', 'black', 'red', 'yellow', 'green']
    const args = [
        [X,X,W],
        [X+W+W+G,X,W],
        [X+W+W+G+W+W+G,X,W],
        [X+W+G/2,X+W,W],
        [X+W+G/2+W+W+G,X+W,W]]

    while (colors.length > 0) {
        ctx.strokeStyle = colors.shift()
        ctx.beginPath()
        ctx.arc.apply(ctx, args.shift().concat([0,Math.PI*2,true]))
        ctx.stroke()
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
