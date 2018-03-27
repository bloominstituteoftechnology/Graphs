import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const xCount = 8;
const yCount = 8;
const boxSize = 150;

const canvasWidth = boxSize * xCount;
const canvasHeight = boxSize * yCount;
const vertexRadius = boxSize / 8;
/**
 * GraphView
 * @extends {Component<{graph: Graph}, State>}
 * 
 */
class GraphView extends Component {
  constructor() {
    super();
  }
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
    /** @type {CanvasRenderingContext2D} */
    let ctx = this.refs.canvas.getContext('2d');

    // initialize canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw edges of vertexes
    for (const parentVert of this.props.graph.vertexes) {
      for (const debugEdge of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(debugEdge.destination.pos.x, debugEdge.destination.pos.y);
        ctx.stroke();
      }
    }

    // draw vertexes 
    for (const vertex of this.props.graph.vertexes) {
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, Math.PI * 2);
      ctx.stroke();

      // add text to middle of node
      ctx.fillStyle = 'red';
      ctx.textAlign = 'center';
      ctx.font = '10px Arial';
      ctx.textBaseline = 'middle';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
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
  state = {
    graph: new Graph()
  };

  constructor(props) {
    super(props);

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(xCount, yCount, boxSize);
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
