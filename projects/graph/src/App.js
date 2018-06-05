import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
const canvasHeight = 400;

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
    // ctx.globalCompositeOperation = 'source-in';

    // Clear it
    ctx.fillStyle = 'pink';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // console.log('in updateCanvas', this.props);

    ctx.textBaseline = 'middle';
    ctx.textAlign = 'center';
    ctx.font = '16px Arial';

    const vertexSize = 15;

    for (let vertex of this.props.graph.vertexes) {
      // ctx.beginPath();

      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }

      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexSize, 0, 2 * Math.PI);

      ctx.fillStyle = 'white';
      ctx.fill();

      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);

      ctx.stroke();
    }

    // for (let vertex of this.props.graph.vertexes) {
    //   ctx.beginPath();
    //   ctx.arc(vertex.pos.x, vertex.pos.y, vertexSize, 0, 2 * Math.PI);

    //   ctx.fillStyle = 'white';
    //   ctx.fill();

    //   ctx.fillStyle = 'black';
    //   ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);

    //   ctx.stroke();
    // }

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
    // this.state.graph.randomize(600, 600, 300, 0.06);

    this.state.graph.debugCreateTestData();
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
