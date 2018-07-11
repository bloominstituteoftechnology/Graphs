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

  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");

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
      ctx.font = "10px Georgia";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(
        this.props.graph.vertexes[i].value,
        this.props.graph.vertexes[i].pos.x,
        this.props.graph.vertexes[i].pos.y
      );
    }
    // console.log(canvas);
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
