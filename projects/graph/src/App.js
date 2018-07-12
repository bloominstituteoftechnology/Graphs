import React, { Component } from "react";
import TinyColor from "tinycolor2";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const quadrantSize = 110;
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
    this.props.graph.randomize(
      Math.floor(this.props.width / quadrantSize),
      Math.floor(this.props.height / quadrantSize),
      quadrantSize,
      0.5
    );

    // Clear it
    ctx.fillStyle = "lightgrey";
    ctx.fillRect(0, 0, this.props.width, this.props.height);

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
          ctx.fillStyle = color;
          ctx.lineWidth = 0.5;
          ctx.strokeStyle = "hsl(0,0%,50%)";
          ctx.setTransform(1, 0, 0, 1, 0.5, 0.5);
          i.edges.forEach(j => {
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
      <div className="canvas-parent">
        <canvas
          ref="canvas"
          width={this.props.width}
          height={this.props.height}
        />
        <button className="generate-graph" onClick={e => this.props.callback()}>
          Generate Graph
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
      graph: new Graph(),
      width: 0,
      height: 0
    };
  }

  componentDidMount = () => {
    this.updateWindowDimensions();
    window.addEventListener("resize", this.updateWindowDimensions);
  };

  componentWillUnmount = () => {
    window.removeEventListener("resize", this.updateWindowDimensions);
  };

  updateWindowDimensions = () => {
    this.setState({
      width: window.innerWidth - 50,
      height: window.innerHeight - 50
    });
  };

  generateNewGraph = () => {
    this.setState({ graph: new Graph() });
  };

  render() {
    return (
      <div className="App">
        <GraphView
          graph={this.state.graph}
          callback={this.generateNewGraph}
          width={this.state.width}
          height={this.state.height}
        />
      </div>
    );
  }
}

export default App;
