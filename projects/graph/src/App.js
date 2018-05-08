import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 750;
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
    ctx.fillStyle = 'lightpink';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Draw Edges
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let vertex = this.props.graph.vertexes[i];
      if (vertex.edges.length) {
        for (let j = 0; j < vertex.edges.length; j++) {
          let edge = vertex.edges[j].destination.position;
          ctx.beginPath();
          ctx.moveTo(vertex.position.x, vertex.position.y);
          ctx.lineTo(edge.x, edge.y);
          ctx.stroke();
        }
      }
    }

    // Draw Vertices
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let vertex = this.props.graph.vertexes[i];
      ctx.beginPath();
      ctx.arc(vertex.position.x, vertex.position.y, 10, 0, 2 * Math.PI);
      ctx.fillStyle = 'black';
      ctx.fill();
      ctx.stroke();
      ctx.strokeStyle = 'white';
      ctx.font = '10px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = 'white';
      ctx.fillText(vertex.value, vertex.position.x, vertex.position.y);
      ctx.stroke();
      ctx.closePath();
    }
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph(),
    };

    // this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5, 4, 150, 0.6);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
