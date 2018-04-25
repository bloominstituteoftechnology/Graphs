import React, { Component } from 'react';
import { Graph } from './graph';
import ReloadButton from './components/reload';
import './App.css';

const width = 8;
const height = 5;
const jitter = 150;
const vertexRadius = 14;
const font = 'Courier';
const prob = 0.55;
const backgroundColor = 'white';

const canvasWidth = width * jitter;
const canvasHeight = height * jitter;

const colors = {
  0: '#000000',
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
  15: '#df25d5',
};

const getRandomColor = _ => {
  const letters = '0123456789ABCDEF';
  let color = '#';

  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }

  return color;
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
    if (this.props.graph.vertexes.length === 0)
      this.props.graph.randomize(width, height, jitter, prob);

    this.updateCanvas();
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = backgroundColor;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const connectedComponents = this.props.graph.getConnectedComponents();

    for (let i = 0; i < connectedComponents.length; i++) {
      const cluster = connectedComponents[i];
      const color = colors[i] || getRandomColor();

      for (let vertex of cluster) {
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.strokeStyle = color;
          ctx.stroke();

          const averagePosX = (vertex.pos.x + edge.destination.pos.x) / 2;
          const averagePosY = (vertex.pos.y + edge.destination.pos.y) / 2;

          const weightWidth = vertexRadius * 1.2;
          const weightHeight = vertexRadius * 1.2;
          ctx.fillStyle = backgroundColor;
          ctx.fillRect(
            averagePosX - weightWidth / 2,
            averagePosY - weightHeight / 2,
            weightWidth,
            weightHeight,
          );

          ctx.fillStyle = 'black';
          ctx.font = `${vertexRadius}px ${font}`;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(edge.weight, averagePosX, averagePosY);
        }
      }

      for (let vertex of cluster) {
        const posX = vertex.pos.x;
        const posY = vertex.pos.y;

        ctx.beginPath();
        ctx.arc(posX, posY, vertexRadius, 0, 2 * Math.PI);
        ctx.strokeStyle = color;
        ctx.stroke();
        ctx.fillStyle = color;
        ctx.fill();

        ctx.fillStyle = backgroundColor;
        ctx.font = `${vertexRadius}px ${font}`;
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

    this.state.graph.randomize(width, height, jitter, prob);
  }

  reloadButtonClicked = _ => {
    this.setState({ graph: new Graph() });
  };

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />

        <ReloadButton reloadButtonClicked={this.reloadButtonClicked} />
      </div>
    );
  }
}

export default App;
