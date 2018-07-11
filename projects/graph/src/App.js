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
    // canvas constants
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");
    ctx.font = "11px serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    // clear canvas upon updating
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // find vertexes
    const vertexes = this.props.graph.vertexes;
    const vertexRadius = 10;
    // find the connected components
    const connectedComponents = this.props.graph.getConnectedComponents();
    // draw and color edges of connected components
    connectedComponents.forEach(component => {
      for (let v of component) {
        let x = v.pos.x;
        let y = v.pos.y;
        // draw each edge with the color of its component
        for (let edge of v.edges) {
          let edgeX = edge.destination.pos.x;
          let edgeY = edge.destination.pos.y;
          // draw a line to each connected component
          ctx.beginPath();
          ctx.strokeStyle = v.color; // color of component
          ctx.moveTo(x, y);
          ctx.lineTo(edgeX, edgeY);
          ctx.fill();
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
      ctx.strokeStyle = "black";
      ctx.arc(x, y, vertexRadius, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
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
