import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
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

    ctx.fillStyle = 'pink';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.textBaseline = 'middle';
    ctx.textAlign = 'center';
    ctx.font = '16px Arial';

    const vertexSize = 15;

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.strokeStyle = vertex.color;
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexSize, 0, 2 * Math.PI);

      ctx.fillStyle = vertex.color;
      ctx.strokeStyle = vertex.color;
      ctx.fill();

      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);

      ctx.stroke();
    }

    // !!! IMPLEMENT ME
    // compute connected components
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.5);
    // const test = this.state.graph.generateTwoColorScheme(20);
    // console.log('test', test);
    // this.state.graph.debugCreateTestData();
    // this.state.graph.bfs(this.state.graph.vertexes[0]);
    this.state.graph.dump();
    this.state.graph.getConnectedComponents();
  }

  refreshPage() {
    window.location.reload();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <button onClick={this.refreshPage}>Generate New Graph!</button>
      </div>
    );
  }
}

export default App;
