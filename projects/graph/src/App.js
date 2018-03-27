import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
// Styling the Vertices
const xpadding = 8;
const ypadding = 4;
// Sizing the Graph
const xsize = 5;
const ysize = 4;
const jitter = 150;

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

  getRandomColor() {
    return "#" + ((1 << 24) * Math.random() | 0).toString(16);
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // --- GraphView is getting 'graph' as a prop from App.
    // --- accessible through 'this.props.graph'

    const connectedComponents = this.props.graph.getConnectedComponents();
    console.log('Connected Components:', connectedComponents);

    // draw edges
    // For each vertex inside the connected components array
    connectedComponents.forEach(vertex => {
      vertex.edges.forEach(edge => {
        ctx.beginPath(); // Begin Drawing Line
        ctx.moveTo(vertex.pos.x, vertex.pos.y); // Move to Origin Vertex
        ctx.strokeStyle = 'black';
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y)
        ctx.stroke(); // Stroke the line out
        ctx.closePath() // Reset the Cursor Back to Initial Vertex
      });
    })
    // draw verts
    this.props.graph.vertexes.forEach(vertex => {
      ctx.beginPath();
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.strokeStyle = 'black';
      ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, 2 * Math.PI, true);
      ctx.stroke();
      ctx.closePath();
      // Fill them In White
      ctx.fillStyle = 'white';
      ctx.beginPath();
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, 2 * Math.PI, true);
      ctx.fill();
      // Change the Color of the Connected Ones
      let connected = this.props.graph.bfs(vertex);
      ctx.fillStyle = this.getRandomColor();
      connected.forEach(connectedVertex => {
        ctx.beginPath();
        ctx.moveTo(connectedVertex.pos.x, connectedVertex.pos.y);
        ctx.arc(connectedVertex.pos.x, connectedVertex.pos.y, 20, 0, 2 * Math.PI, true);
        ctx.fill();
      });
    })
    this.props.graph.vertexes.forEach(vertex => {
      // Write each Vertex Values
      ctx.strokeStyle = 'black';
      ctx.font = '14px serif';
      ctx.beginPath();
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.strokeText(vertex.value, vertex.pos.x - xpadding, vertex.pos.y + ypadding)
    })
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
    this.state.graph.randomize(xsize, ysize, jitter);
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
