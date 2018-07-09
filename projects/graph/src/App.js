import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 700;
const canvasHeight = 850;

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
    // grey canvas
    ctx.fillStyle = "#aaacb5";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // red line

    let gradient0 = ctx.createLinearGradient(345, 582, 700, 50);
    gradient0.addColorStop(0, "#cc2037"); // darker
    gradient0.addColorStop(0.20, "#f2485f"); // lighter
    ctx.fillStyle = gradient0;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(700, 50); // top right
    ctx.lineTo(300, 550); // middle
    ctx.lineTo(345, 582); // middle again
    ctx.lineTo(700, 100); // top right: end
    ctx.closePath();
    ctx.fill();
    
    let gradient1 = ctx.createLinearGradient(0, 850, 300, 549);
    gradient1.addColorStop(0.80, "#f2485f"); // lighter
    gradient1.addColorStop(1, "#cc2037"); // darker
    ctx.fillStyle = gradient1;
    ctx.beginPath();
    ctx.lineTo(301, 549); // middle
    ctx.lineTo(0, 660); // lower left
    ctx.lineTo(0, 850); // bottom left: canvas edge
    ctx.lineTo(100, 850); // bottom right
    ctx.lineTo(346, 581); // middle again
    ctx.closePath();
    ctx.fill();
    // ctx.stroke();

    // cyan line
    ctx.fillStyle = "#2cb786";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(700, 100); // top right
    ctx.lineTo(345, 582); // middle
    ctx.lineTo(100, 850); // bottom left
    ctx.lineTo(350, 850); // bottom right
    ctx.lineTo(392, 613); // middle again
    ctx.lineTo(700, 155); // top right: end
    ctx.closePath();
    ctx.fill();
    // ctx.stroke();

    // yellow line
    ctx.fillStyle = "#f9bb34";
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.moveTo(700, 155); // top right
    ctx.lineTo(392, 613); // middle
    ctx.lineTo(350, 850); // bottom left
    // ctx.lineTo(700, 850); // bottom right: canvas edge
    ctx.lineTo(525, 850); // bottom right
    ctx.lineTo(445, 640); // middle again
    ctx.lineTo(700, 220); // top right: end
    ctx.closePath();
    ctx.fill();
    // ctx.stroke();

    // guide line
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, 343);
    ctx.lineTo(700, 828);
    // ctx.stroke();

    // text
    ctx.fillStyle = "black";
    ctx.font = "158px helvetica";
    ctx.fillText("2018.", 50, 150);

    ctx.font = "58px helvetica";
    ctx.fillText("Fall.", 50, 215);

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
