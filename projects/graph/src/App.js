import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 600;
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
    ctx.fillStyle = "lightblue";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      ctx.fillStyle = "red";
      ctx.fillRect(
        this.props.graph.vertexes[i].pos.x,
        this.props.graph.vertexes[i].pos.y,
        10,
        10
      );
      for (let j = 0; j < this.props.graph.vertexes[i].edges.length; j++) {
        ctx.fillStyle = "blue";
        // ctx.fillRect(
        //   this.props.graph.vertexes[i].pos.x +
        //     this.props.graph.vertexes[i].edges[j].connection.pos.x / 2,
        //   this.props.graph.vertexes[i].pos.y +
        //     this.props.graph.vertexes[i].edges[j].connection.pos.y / 2,
        //   10,
        //   10
        // );
        ctx.beginPath();
        ctx.moveTo(
          this.props.graph.vertexes[i].pos.x,
          this.props.graph.vertexes[i].pos.y
        );
        ctx.lineTo(
          this.props.graph.vertexes[i].edges[j].connection.pos.x,
          this.props.graph.vertexes[i].edges[j].connection.pos.y
        );
        ctx.stroke();
      }
    }
    console.log(canvas);
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

    this.state.graph.randomize(5, 4, 100, 0.6);
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
