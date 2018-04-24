import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 19;
const prob = 0.7;

const colors = {
  0: 'black',
  1: '#808080',
  2: '#a9a9a9',
  3: '#d3d3d3',
  4: '#00008b',
  5: '#0000ff',
  6: '#add8e6',
  7: '#008000',
  8: '#90ee90',
  9: '#adff2f',
  10: '#ff00ff',
  11: '#8b008b',
  12: '#ffc0cb',
  13: '#ff1493',
  14: '#ff69b4',
};

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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const connectedComponents = this.props.graph.getConnectedComponents();

    for (let i = 0; i < connectedComponents.length; i++) {
      const cluster = connectedComponents[i];
      const color = colors[i];

      for (let vertex of cluster) {
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.strokeStyle = color;
          ctx.stroke();
        }
      }

      for (let vertex of cluster) {
        const posX = vertex.pos.x;
        const posY = vertex.pos.y;

        ctx.beginPath();
        ctx.arc(posX, posY, vertexRadius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fillStyle = color;
        ctx.fill();

        ctx.fillStyle = 'white';
        ctx.font = `${vertexRadius}px Courier`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vertex.value, posX, posY);
      }
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

    this.state.graph.randomize(5, 4, 150, prob);
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
