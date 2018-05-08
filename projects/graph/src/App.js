import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;

function drawLine(startx, starty, finx, finy, ctx) {
  ctx.strokeStyle = 'black';
  ctx.moveTo(startx, starty)
  ctx.lineTo(finx, finy);
}

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.props.graph.randomize(5, 5, 120, 0.6);
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
    ctx.fillStyle = 'white';
    ctx.fillRect(2, 2, canvasWidth-4, canvasHeight-4);
    for (let vertex of this.props.graph.vertexes) {
      console.log(vertex);
      ctx.beginPath();
      for (let edge of vertex.edges) {
        drawLine(vertex.pos.x, vertex.pos.y, edge.destination.pos.x, edge.destination.pos.y, ctx);
      }
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