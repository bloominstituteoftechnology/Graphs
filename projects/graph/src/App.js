import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const vr = 10;

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
    ctx.fillStyle = '#ffffe6';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    
    for (let vertex of this.props.graph.vertexes) {
      const px = vertex.pos.x;
      const py = vertex.pos.y;

      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let vertex of this.props.graph.vertexes) {
      const px = vertex.pos.x;
      const py = vertex.pos.y;

      ctx.beginPath();
      ctx.arc(px, py, vr, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fillStyle = 'black';
      ctx.fill();

      ctx.fillStyle = 'white';
      ctx.font = '11px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(vertex.value, px, py);
    }
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
    this.state.graph.randomize(5, 4, 150, 0.6);
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
