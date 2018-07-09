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

    // Clear it
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    const vertexes = this.props.graph.vertexes;
    const vertexRadius = 10;

    vertexes.forEach(vertex => {
      let x = vertex.pos.x;
      let y = vertex.pos.y;
      ctx.beginPath();
      ctx.arc(x, y, vertexRadius, 0, Math.PI * 2);
      ctx.fillStyle = "teal";
      ctx.fill();
      ctx.closePath();
    });
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
