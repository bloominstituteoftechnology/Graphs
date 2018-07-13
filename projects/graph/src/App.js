import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
let canvasWidth = 750;
let canvasHeight = 600;
const circleRadius = 15;

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
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext("2d");

    ctx.fillStyle = "grey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = "13px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    // set of all connected components
    const components = this.props.graph.getConnectedComponents();
    // loop pass each to drawV
    components.forEach((component) => {
      this.drawVertexes(ctx, component, this.generateRandomColor());
    });
  }

  drawVertexes(ctx, vertexes, color) {

    ctx.strokeStyle = color;

    for (let vertex of vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    // circles
    for (let v of vertexes) {
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    }
  }

  generateRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
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

  randomize = () => {
    const state = {
      graph: new Graph()
    };

    state.graph.randomize(5, 4, 150, 0.6);
    this.setState(state);
  };

  render() {
    return (
      <div className="App">
        <button onClick={this.randomize}> Randomize </button>
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
