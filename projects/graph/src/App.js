import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 400;
const canvasHeight = 300;
const vertexRadius = 10;

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
    let grd = ctx.createLinearGradient(canvasWidth / 2, 0, canvasWidth / 2, canvasHeight);
    grd.addColorStop(0, "lightyellow");
    grd.addColorStop(1, "lightblue");
    
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log('In update canvas, vertex data is: ', this.props.graph);

    for (let vertex of this.props.graph.vertexes) {
      console.log('vertex names: ', vertex.value);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2*Math.PI);
      ctx.fillStyle = 'green';
      ctx.fill();
      ctx.strokeStyle= 'black'; // TODO: Optimize this code. Many calls for stroke and fill
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.font = "10px Arial";
      ctx.textAlign = "center";
      ctx.textBaseLine = "middle";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
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
    this.state.graph.debugCreateTestData();
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
