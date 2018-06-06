import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleSize = 15;

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

    console.log("In update canvas", this.props);
    // let bubbles = this.generateBubbles(1000);
    // // Clear it
    // setInterval(() => {
    ctx.fillStyle = "darkblue";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fill();

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        // ctx.fillStyle = "black";
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let vertex of this.props.graph.vertexes) {
      console.log("VERTEXES: ", vertex);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = vertex.color;
      ctx.fill();
      ctx.stroke();

      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.font = "16px Arial";
      ctx.fillStyle = "black";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
  }

  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />
      </div>
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
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    this.state.graph.randomize(5, 4, 150, 0.6);
    // use the graph randomize() method
  }

  render() {
    this.state.graph.getConnectedComponents();
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <button
          onClick={() => {
            this.state.graph.vertexes = [];
            this.state.graph.randomize(5, 4, 150, 0.6);
            this.setState({ graph: this.state.graph }); // Lazy way? Is there a better way to force a re-render?
          }}
        >
          RELOAD
        </button>
      </div>
    );
  }
}

export default App;
