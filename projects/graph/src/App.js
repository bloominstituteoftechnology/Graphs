import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;
const circleRadius = 10;

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

    console.log("this.props.graph: ", this.props.graph);
    // call dummy function
    //this.props.graph.createDummyGraph();
    //console.log("called createDummyGraph");

    // Clear it
    ctx.fillStyle = "red";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = "10px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    // randomize
    this.props.graph.randomize(7, 7, 100, 0.6);

    // draw edges
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    // draw  verts
    for (let v of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.fillStyle = "white";
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      // fill in text
      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.pos.x, v.pos.y);
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
