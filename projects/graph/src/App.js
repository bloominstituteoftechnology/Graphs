import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

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

    const g = this.props.graph;
    g.dump();

    g.randomize(5, 4, 150, 0.6);

    for (let v of g.vertexes) {
      if (v.pos) {
        ctx.beginPath();
        ctx.fillStyle = "indigo";
        ctx.arc(v.pos.x, v.pos.y, 18, 0, Math.PI * 2, true);
        ctx.fill();
        for (let e of v.edges) {
          ctx.beginPath();
          ctx.strokeStyle = "goldenrod";
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
          ctx.closePath();
          ctx.stroke();
        }
        ctx.font = "14px helvetica";
        ctx.fillStyle = "white";
        ctx.fillText(`${v.value}`, v.pos.x - 7, v.pos.y);
      }
    }
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
