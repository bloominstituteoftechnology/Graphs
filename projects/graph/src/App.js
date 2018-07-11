import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 1000;

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

    // call dummy graph
    // console log confirms this.props.graph is being rendered
    // console.log("this.props.graph", this.props.graph);
    // console.log("createDummyGraph", this.props.graph.createDummyGraph);

    // Clear it
    ctx.fillStyle = "grey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw dummy vertex (hardcoded)
    // ctx.beginPath();
    // ctx.arc(10, 10, 10, 0, 2 * Math.PI); // x, y, radius, start angle, finish angle
    // ctx.stroke();
    // ctx.closePath();

    // ctx.beginPath();
    // ctx.arc(100, 100, 10, 0, 2 * Math.PI); // x, y, radius, start angle, finish angle
    // ctx.stroke();
    // ctx.closePath();

    // edges
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.closePath();
        ctx.stroke();
      }
    }

    // draw dummy verticies (dynamic)
    this.props.graph.vertexes.forEach(v => {
      console.log(v.color);
      // verts
      ctx.strokeStyle = "black";
      ctx.fillStyle = v.color;
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, 14, 0, 2 * Math.PI);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // vert values (labels)
      if (v.color === "black") {
        ctx.fillStyle = "white";
      } else {
        ctx.fillStyle = "black";
      }
      ctx.font = "11px arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });

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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    // this.state.graph.createDummyGraph();
    this.state.graph.randomize(3, 4, 150, 0.6);
    this.state.graph.bfs();
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
