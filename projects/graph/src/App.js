import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 1200;
const canvasHeight = 900;
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
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");
    this.props.graph.randomize(8, 6, 150, 0.3);

    console.log("this.props.graph: ", this.props.graph);

    // Clear it
    ctx.fillStyle = "lightgrey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw the lines
    let connected = [];
    connected = this.props.graph.bfs();
    this.props.graph.vertexes.forEach(i => {
      i.edges.forEach(j => {
        ctx.fillStyle = j.color;
        ctx.moveTo(i.pos.x, i.pos.y);
        ctx.lineTo(j.destination.pos.x, j.destination.pos.y);
        ctx.stroke();
      });
    });

    // draw our vertexes
    this.props.graph.vertexes.forEach(v => {
      ctx.beginPath();
      ctx.fillStyle = v.color;
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      // fill in the text
      ctx.beginPath();
      ctx.font = "13px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });
  }

  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />
        <br />
        <button onClick={e => this.props.callback()}> Generate Graph </button>
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
  }

  generateNewGraph = () => {
    this.setState({ graph: new Graph() });
  };

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} callback={this.generateNewGraph} />
      </div>
    );
  }
}

export default App;
