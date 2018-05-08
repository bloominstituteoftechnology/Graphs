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

    // Clear it
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME

    // // grad
    // let grd = ctx.createLinearGradient(0, 200, 200, 20);
    // grd.addColorStop(0, "gold");
    // grd.addColorStop(1, "silver");

    // ctx.fillStyle = grd;
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // // e

    // // c1
    // ctx.beginPath();
    // ctx.globalAlpha = 0.4;
    // ctx.arc(200, 175, 40, 0, 2 * Math.PI);
    // ctx.fillStyle = "red";
    // ctx.fill();
    // // ec1

    // // c2
    // ctx.beginPath();
    // ctx.arc(180, 210, 40, 0, 2 * Math.PI);
    // ctx.fillStyle = "green";
    // ctx.fill();
    // // ec2

    // // c3
    // ctx.beginPath();
    // ctx.arc(220, 210, 40, 0, 2 * Math.PI);
    // ctx.fillStyle = "blue";
    // ctx.fill();
    // // ec3

    // graph

    let nodeSize = 20;

    for (let vertex of this.props.graph.vertexes) {
      if (vertex.edges.length) {
        for (let i = 0; i < vertex.edges.length; i++) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(
            vertex.edges[i].destination.pos.x,
            vertex.edges[i].destination.pos.y,
          );
          ctx.strokeStyle = "red";
          ctx.stroke();
        }
      }
      let r, g, b;
      for (let vertex of this.props.graph.vertexes) {
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, nodeSize, 0, Math.PI * 2);
        r = Math.floor(Math.random() * 155) + 100;
        g = Math.floor(Math.random() * 155) + 50;
        b = Math.floor(Math.random() * 155) + 100;
        ctx.fillStyle = "rgb(" + r + ", " + g + ", " + b + ")";
        ctx.fill();

        ctx.strokeStyle = "blue";
        ctx.stroke();

        ctx.fillStyle = "black";
        ctx.font = "10px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      }
    }
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
      graph: new Graph(),
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 5, 150, 0.6);
    // this.state.graph.debugger();
  }

  render() {
    this.state.graph.dump();

    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
