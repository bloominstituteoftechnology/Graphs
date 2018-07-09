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
    let gradient_canvas = ctx.createLinearGradient(345, 582, 700, 50);
    gradient_canvas.addColorStop(0, "#c4beb0"); // darker
    gradient_canvas.addColorStop(0.25, "#dbd5c7"); // lighter
    ctx.fillStyle = gradient_canvas;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // red line

    let gradient0 = ctx.createLinearGradient(345, 582, 700, 50);
    gradient0.addColorStop(0, "#cc2037"); // darker
    gradient0.addColorStop(0.25, "#f2485f"); // lighter
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
    gradient1.addColorStop(0.75, "#f2485f"); // lighter
    gradient1.addColorStop(1, "#cc2037"); // darker
    ctx.fillStyle = gradient1;
    ctx.beginPath();
    ctx.moveTo(301, 549); // middle
    ctx.lineTo(0, 660); // lower left
    ctx.lineTo(0, 850); // bottom left: canvas edge
    ctx.lineTo(100, 850); // bottom right
    ctx.lineTo(346, 581); // middle again
    ctx.closePath();
    ctx.fill();

    // cyan line
    let gradient2 = ctx.createLinearGradient(345, 580, 700, 100);
    gradient2.addColorStop(0, "#2cb786"); // darker
    gradient2.addColorStop(0.30, "#49d8a6"); // lighter
    ctx.fillStyle = gradient2;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(700, 100); // top right
    ctx.lineTo(345, 582); // middle
    ctx.lineTo(392, 613); // middle again
    ctx.lineTo(700, 155); // top right: end
    ctx.closePath();
    ctx.fill();

    let gradient3 = ctx.createLinearGradient(100, 850, 345, 582);
    gradient3.addColorStop(0.70, "#49d8a6"); // lighter
    gradient3.addColorStop(1, "#2cb786"); // darker
    ctx.fillStyle = gradient3;
    ctx.beginPath();
    ctx.moveTo(345, 582); // middle
    ctx.lineTo(100, 850); // bottom left
    ctx.lineTo(350, 850); // bottom right
    ctx.lineTo(392, 613); // middle again
    ctx.closePath();
    ctx.fill();


    // yellow line
    let gradient4 = ctx.createLinearGradient(392, 613, 700, 155);
    gradient4.addColorStop(0, "#f9bb34"); // darker
    gradient4.addColorStop(0.20, "#ffcd60"); // lighter
    ctx.fillStyle = gradient4;
    
    // ctx.fillStyle = "blue";
    ctx.beginPath();
    ctx.moveTo(700, 155); // top right
    ctx.lineTo(392, 613); // middle
    ctx.lineTo(445, 640); // middle again
    ctx.lineTo(700, 220); // top right: end
    ctx.closePath();
    ctx.fill();
    // ctx.stroke();


    let gradient5 = ctx.createLinearGradient(350, 850, 392, 613);
    gradient5.addColorStop(0.80, "#ffcd60"); // lighter
    gradient5.addColorStop(1, "#f9bb34"); // darker
    // ctx.fillStyle = "blue";
    ctx.fillStyle = gradient5;
    ctx.beginPath();
    ctx.moveTo(392, 613); // middle
    ctx.lineTo(350, 850); // bottom left
    ctx.lineTo(525, 850); // bottom right
    ctx.lineTo(445, 640); // middle again
    ctx.closePath();
    ctx.fill();
    // ctx.stroke();

    // guide line
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, 343);
    ctx.lineTo(700, 810);
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
