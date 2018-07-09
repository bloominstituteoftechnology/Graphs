import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1800;
const canvasHeight = 1350;
const maxWeight = 200;

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
    const drawn = [];

    // Clear it
    ctx.fillStyle = 'yellow';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // console.log('updateCanvas', this.props);
    // !!! IMPLEMENT ME
    // compute connected components
    // let debugVertex = this.props.graph.vertexes[0];

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';

    const { vertexes } = this.props.graph;

    vertexes.forEach(vert => {
      // console.log(vert);
      const { edges } = vert;
      edges.forEach(edge => {
        const weightX =
          (Math.max(vert.pos.x, edge.destination.pos.x) +
            Math.min(vert.pos.x, edge.destination.pos.x)) /
          2;
        const weightY =
          (Math.max(vert.pos.y, edge.destination.pos.y) +
            Math.min(vert.pos.y, edge.destination.pos.y)) /
          2;
        if (!drawn.includes(weightX)) {
          ctx.fillStyle = 'black';
          ctx.fillText(edge.weight, weightX, weightY);
        }
        drawn.push(weightX);

        const vertNum = Number(vert.value.slice(1));
        const destNum = Number(edge.destination.value.slice(1));
        // console.log('values', vertNum, destNum);
        if (vertNum < destNum) {
          ctx.beginPath();
          // console.log(edge, 'edge');
          ctx.moveTo(vert.pos.x, vert.pos.y);
          const { x, y } = edge.destination.pos;
          ctx.strokeStyle = edge.destination.color;
          ctx.lineTo(x, y);
        }
        ctx.stroke();
      });

      ctx.beginPath();
      ctx.arc(vert.pos.x, vert.pos.y, 15, 0, Math.PI * 2);
      ctx.strokeStyle = vert.color;
      ctx.fillStyle = vert.color; // TODO: make variable
      ctx.fill();

      ctx.fillStyle = 'black';
      ctx.fillText(vert.value, vert.pos.x, vert.pos.y);

      ctx.stroke();
    });
    // console.log(this.props.graph);
    // draw edges
    // draw verts
    // draw vert values (labels)
  }

  /**
   * Render
   */
  render() {
    return (
      <canvas
        ref="canvas"
        width={canvasWidth}
        height={canvasHeight}
        style={{ marginTop: 20 }}
      />
    );
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
    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(12, 9, 150, 0.5);
    this.state.graph.getConnectedComponents();
    console.log(this.state.graph, 'graph');
  }

  render() {
    return (
      <div className="App">
        <div>
          <GraphView graph={this.state.graph} />
        </div>
        <div>
          <button className="button" onClick={this.randomizeGraph}>
            Randomize Graph
          </button>
        </div>
      </div>
    );
  }

  randomizeGraph = () => {
    // console.log('in randomizex');
    // console.log(this.state.graph)
    const graph = new Graph();
    graph.randomize(12, 9, 150, 0.5);
    graph.getConnectedComponents();
    this.setState({ graph });
    console.log(graph);

    // this.state.graph.randomize(5, 4, 150, 0.5);
    // console.log(this.state.graph);
  };
}

export default App;
