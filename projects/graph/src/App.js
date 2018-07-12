import React, { Component } from "react";
import TinyColor from "tinycolor2";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 1200;
const canvasHeight = 900;
const circleRadius = 15;

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
    this.props.graph.randomize(8, 6, 150, 0.5);

    // Clear it
    ctx.fillStyle = "lightgrey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    function getRandomColor(seed) {
      var letters = "0123456789ABCDEF";
      var color = "#";
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random(seed) * 16)];
      }
      return color;
    }

    // draw the lines
    let color;
    let connected = [];
    for (let vertex of this.props.graph.vertexes) {
      if (vertex.color !== "black") {
        color = TinyColor(getRandomColor(vertex.pos.x));
        // console.log(vertex);

        connected = this.props.graph.bfs(vertex);
        connected.forEach(i => {
          i.edges.forEach(j => {
            ctx.fillStyle = color;
            ctx.lineWidth = 0.5;
            ctx.strokeStyle = "hsl(0,0%,50%)";
            ctx.setTransform(1, 0, 0, 1, 0.5, 0.5);
            ctx.moveTo(i.pos.x, i.pos.y);
            ctx.lineTo(j.destination.pos.x, j.destination.pos.y);
            ctx.stroke();
          });
        });

        // draw our vertexes
        connected.forEach(v => {
          ctx.beginPath();
          ctx.fillStyle = color;
          ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
          ctx.fill();
          ctx.stroke();

          // fill in the text
          ctx.beginPath();
          ctx.font = "13px Arial";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.textShadowColor = "rgba(0, 0, 0, 0.75)";
          ctx.textShadowOffset = { width: -1, height: 1 };
          ctx.textShadowRadius = 10;
          ctx.fillStyle = color.isDark() ? "White" : "Black";
          ctx.fillText(v.value, v.pos.x, v.pos.y);
        });
      }
    }
  }

  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />
        <br />
        <button className="generate-graph" onClick={e => this.props.callback()}>
          {" "}
          Generate Graph{" "}
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
  }

  generateNewGraph = () => {
    this.setState({ graph: new Graph() });
  };

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} callback={this.generateNewGraph} />
      </div>
    );
  }
}

export default App;
