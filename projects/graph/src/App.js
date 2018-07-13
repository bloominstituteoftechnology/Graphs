import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

const canvasWidth = 750;
const canvasHeight = 600;
const radius = 15;

let canvas;
let ctx;

function randomColor() {
  let chars = "ABCDEF0123456789";
  let color = "#";
  for (var i = 0; i < 6; i++) {
    color += chars[Math.floor(Math.random() * 16)];
  }
  return color;
}

// Copied from internet to make the label black or white depending on the background color
function fontColor(bgColor, lightColor, darkColor) {
  var color = bgColor.charAt(0) === "#" ? bgColor.substring(1, 7) : bgColor;
  var r = parseInt(color.substring(0, 2), 16); // hexToR
  var g = parseInt(color.substring(2, 4), 16); // hexToG
  var b = parseInt(color.substring(4, 6), 16); // hexToB
  var uicolors = [r / 255, g / 255, b / 255];
  var c = uicolors.map(col => {
    if (col <= 0.03928) {
      return col / 12.92;
    }
    return Math.pow((col + 0.055) / 1.055, 2.4);
  });
  var L = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  return L > 0.179 ? darkColor : lightColor;
}

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

  vertexClick = () => {
    let rect = canvas.getBoundingClientRect();
    let x = window.event.clientX - rect.left;
    let y = window.event.clientY - rect.top;
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let dist = Math.sqrt(
        (y - this.props.graph.vertexes[i].pos.y) *
          (y - this.props.graph.vertexes[i].pos.y) +
          (x - this.props.graph.vertexes[i].pos.x) *
            (x - this.props.graph.vertexes[i].pos.x)
      );
      if (dist <= radius) {
        console.log(
          "Vertex " + this.props.graph.vertexes[i].value + " clicked"
        );
      }
      // this click statement treats the circles as rectangles so it's bad
      // if (
      //   x <= this.props.graph.vertexes[i].pos.x + radius &&
      //   x >= this.props.graph.vertexes[i].pos.x - radius &&
      //   y <= this.props.graph.vertexes[i].pos.y + radius &&
      //   y >= this.props.graph.vertexes[i].pos.y - radius
      // ) {
      //   console.log("VERTY CLICKED" + this.props.graph.vertexes[i].value);
      // }
    }
    console.log("x: " + x + " y: " + y);
  };

  updateCanvas() {
    canvas = this.refs.canvas;
    ctx = canvas.getContext("2d");

    // Clear it
    ctx.fillStyle = "lightblue";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const componentArr = this.props.graph.getConnectedComponents();
    // console.log(componentArr);

    for (let i = 0; i < componentArr.length; i++) {
      const color = randomColor();
      ctx.strokeStyle = color;
      ctx.fillStyle = color;
      for (let vertex of componentArr[i]) {
        vertex.color = color;
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.connection.pos.x, edge.connection.pos.y);
          ctx.stroke();

          ctx.fillStyle = "black";
          ctx.font = `${radius}px Georgia`;
          ctx.textAlign = "middle";
          ctx.textBaseline = "top";
          ctx.fillText(
            edge.weight,
            (vertex.pos.x + edge.connection.pos.x) / 2,
            (vertex.pos.y + edge.connection.pos.y) / 2
          );
          ctx.fillStyle = color;
        }

        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();
      }
    }

    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      ctx.fillStyle = fontColor(
        this.props.graph.vertexes[i].color,
        "white",
        "black"
      );
      ctx.font = `${radius}px Georgia`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(
        this.props.graph.vertexes[i].value,
        this.props.graph.vertexes[i].pos.x,
        this.props.graph.vertexes[i].pos.y
      );
    }

    canvas.addEventListener("click", this.vertexClick, false);
  }

  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />
        <br />
        <button
          onClick={() => {
            this.props.regenerate();
            this.updateCanvas();
          }}
        >
          Regenerate
        </button>
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

    this.state.graph.randomize(5, 4, 150, 0.6);
  }

  regenerate = () => {
    this.state.graph.vertexes = [];
    this.state.graph.randomize(5, 4, 150, 0.6);
  };

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} regenerate={this.regenerate} />
      </div>
    );
  }
}

export default App;
