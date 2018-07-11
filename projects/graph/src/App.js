import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

const canvasWidth = 750;
const canvasHeight = 600;
const radius = 10;

function randomColor() {
  let chars = "ABCDEF0123456789";
  let color = "#";
  for (var i = 0; i < 6; i++) {
    color += chars[Math.floor(Math.random() * 16)];
  }
  return color;
}

// function containsObject(obj, arr) {
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i].connection.value === obj.value) {
//       return true;
//     }
//   }
//   return false;
// }

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

    ctx.strokeStyle = randomColor();

    for (let vertex of this.props.graph.vertexes) {
      // if (i > 0) {
      //   // console.log(
      //   //   this.props.graph.vertexes[i - 1],
      //   //   this.props.graph.vertexes[i].edges
      //   // );
      //   if (
      //     containsObject(
      //       this.props.graph.vertexes[i - 1],
      //       this.props.graph.vertexes[i].edges
      //     )
      //   ) {
      //     ctx.strokeStyle = randomColor();

      //     console.log("INCLUDES " + i);
      //   }
      // }

      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.connection.pos.x, edge.connection.pos.y);
        ctx.stroke();
      }
    }
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      ctx.fillStyle = "blue";
      ctx.beginPath();
      ctx.arc(
        this.props.graph.vertexes[i].pos.x,
        this.props.graph.vertexes[i].pos.y,
        radius,
        0,
        2 * Math.PI
      );
      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = "white";
      ctx.font = "10px Georgia";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(
        this.props.graph.vertexes[i].value,
        this.props.graph.vertexes[i].pos.x,
        this.props.graph.vertexes[i].pos.y
      );
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

    this.state.graph.randomize(5, 4, 150, 0.6);
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
