import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 600;
const canvasHeight = 700;

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
    ctx.fillStyle = "#F8C471";
    ctx.fillRect(80, 80, canvasWidth, canvasHeight);
    ctx.fillStyle = "#F7DC6F";
    ctx.fillRect(150, 150, canvasWidth, canvasHeight);
    ctx.fillStyle = "#ABEBC6";
    ctx.fillRect(200, 200, canvasWidth, canvasHeight);
    ctx.fillStyle = "#1ABC9C";
    ctx.fillRect(300, 300, canvasWidth, canvasHeight);

    ctx.moveTo(100, 50);
    ctx.lineTo(500, 200);
    ctx.lineTo(300, 150);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(100, 20, 30, 0, 2*Math.PI);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(100, 40, 20, 0, 2*Math.PI);
    ctx.stroke();



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
