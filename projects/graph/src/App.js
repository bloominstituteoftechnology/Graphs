import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";
import { O_NOCTTY } from "constants";

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

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
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext("2d");

    // Clear it
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME

 ctx.strokeStyle = "black";
    ctx.strokeRect(35, 70, 450, 330);

    //eyes one
    ctx.beginPath();
    ctx.moveTo(50,200);
    ctx.bezierCurveTo(100, 60, 190,130, 200, 200);
    ctx.stroke();
    
    ctx.beginPath();
    ctx.moveTo(50,200);
    ctx.bezierCurveTo(100, 300, 210,220, 200, 200);
    ctx.stroke();
    // eye 2
    ctx.beginPath();
    ctx.moveTo(320,200);
    ctx.bezierCurveTo(380,60, 450,130, 470, 200);
    ctx.stroke();
    
    ctx.beginPath();
    ctx.moveTo(320,200);
    ctx.bezierCurveTo(410, 300, 450,220, 470, 200);
    ctx.stroke();
// something else
    ctx.fillStyle = "#EAD299";
    ctx.fillRect(210, 110, 100, 100, canvasWidth, canvasHeight);

    ctx.fillStyle = "#EAD299";
    ctx.fillRect(210, 10, 100, 100, canvasWidth, canvasHeight);
  
    ctx.beginPath();

    ctx.moveTo(120, 300);
    ctx.lineWidth = 1;
    ctx.lineTo(400, 300);
    ctx.stroke();
    //lip lower
    ctx.beginPath();
    ctx.moveTo(300, 320);
    ctx.lineWidth = 3;
    ctx.lineTo(220, 320);
    ctx.stroke();
    //tooth one
    ctx.beginPath();
    ctx.moveTo(150, 320);
    ctx.lineWidth = 3;
    ctx.lineTo(140, 300);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(150, 320);
    ctx.lineWidth = 2;
    ctx.lineTo(160, 300);
    ctx.stroke();
    //tooth two
    ctx.beginPath();
    ctx.moveTo(350, 320);
    ctx.lineWidth = 2;
    ctx.lineTo(340, 300);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(350, 320);
    ctx.lineWidth = 4;
    ctx.lineTo(360, 300);
    ctx.stroke();
    // plate lines\
    ctx.beginPath();
    ctx.moveTo(210, 90);
    ctx.lineWidth = 1;
    ctx.lineTo(310, 90);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(310, 50);
    ctx.lineWidth = 1;
    ctx.lineTo(210, 50);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(310, 130);
    ctx.lineWidth = 1;
    ctx.lineTo(210, 130);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(310, 170);
    ctx.lineWidth = 1;
    ctx.lineTo(210, 170);
    ctx.stroke();
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
