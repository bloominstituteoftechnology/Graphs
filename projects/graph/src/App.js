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
    console.log("this.props.graph", this.props.graph);
    console.log("createDummyGraph", this.props.graph.createDummyGraph);
    this.props.graph.createDummyGraph();

    // Clear it
    ctx.fillStyle = "grey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw dummy vertex
    ctx.beginPath();
    ctx.arc(10, 10, 10, 0, 2 * Math.PI); // x, y, radius, start angle, finish angle
    ctx.stroke();
    ctx.closePath();

    ctx.beginPath();
    ctx.arc(100, 100, 10, 0, 2 * Math.PI); // x, y, radius, start angle, finish angle
    ctx.stroke();
    ctx.closePath();


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
