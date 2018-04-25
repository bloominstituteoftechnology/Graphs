import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 752;
const canvasHeight = 650;

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

  randomizeColor(hex = "") {

    if (hex.length === 6) return "#" + hex;

    const hexRandom = ((Math.random() * 240) | 0).toString(16);
    hex += hexRandom.length === 1 ? "0" + hexRandom : hexRandom;

    return this.randomizeColor(hex);
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");

    // Clear it
    ctx.fillStyle = "#d1fff4";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const vertexes = this.props.graph.vertexes;
    const radius = 15;

    // draw all the edges first
    for (let vertex of vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.strokeStyle = this.randomizeColor();
        ctx.stroke();
      }
    }

    // draw all the vertexes second to hide edge overlap on vertexes
    for (let vertex of vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2 * Math.PI);
      ctx.fillStyle = this.randomizeColor();
      ctx.fill();
      ctx.stroke();

      ctx.font = "12px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillStyle = "white";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
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

    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.bfs(0);
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
