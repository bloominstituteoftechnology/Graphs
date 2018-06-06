import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

const circleSize = 15;

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
    ctx.fillStyle = 'tan';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    this.props.graph.getConnectedComponents();

    for (let vertex of this.props.graph.vertexes) {
      const posX = vertex.pos.x;
      const posY = vertex.pos.y;

      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(posX, posY);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.strokeStyle = vertex.color;
        ctx.stroke();
      }
    }

    for (let vertex of this.props.graph.vertexes) {
      const posX = vertex.pos.x;
      const posY = vertex.pos.y;

      ctx.beginPath();
      ctx.arc(posX, posY, circleSize, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fillStyle = vertex.color;
      ctx.fill();

      ctx.fillStyle = 'white';
      ctx.font = '16px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(vertex.value, posX, posY);
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
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
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
