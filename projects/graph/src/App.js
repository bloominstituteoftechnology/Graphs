import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;

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
    let ctx = canvas.getContext("2d");
    ctx.font = "11px serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    // Clear it
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    const vertexes = this.props.graph.vertexes;
    const vertexRadius = 10;
    // compute connected components
    // draw edges
    vertexes.forEach(vertex => {
      let x = vertex.pos.x;
      let y = vertex.pos.y;
      if (vertex.edges.length > 0) {
        for (let i = 0; i < vertex.edges.length; i++) {
          let edge = vertex.edges[i]; // other node to connect to
          let edgeX = edge.destination.pos.x;
          let edgeY = edge.destination.pos.y;
          // draw a line to each edge destination
          ctx.beginPath();
          ctx.fillStyle = "black";
          ctx.moveTo(x, y);
          ctx.lineTo(edgeX, edgeY);
          ctx.stroke();
          ctx.closePath();
        }
      }
    });
    // draw verts
    vertexes.forEach(vertex => {
      let x = vertex.pos.x;
      let y = vertex.pos.y;
      ctx.beginPath();
      ctx.fillStyle = "teal";
      ctx.arc(x, y, vertexRadius, 0, Math.PI * 2);
      ctx.fill();
      // draw vert values (labels)
      ctx.fillStyle = "black";
      ctx.fillText(`${vertex.value}`, x, y);
      ctx.closePath();
    });
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

    // use the graph randomize() method
    const g = this.state.graph;
    g.randomize(5, 4, 150, 0.6);
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
