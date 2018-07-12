import React, { Component } from 'react';
import { Graph } from './graph';
// import threeD from "./three/threeD";
import './App.css';

const canvasWidth = window.innerWidth; // 750;
const canvasHeight = window.innerHeight; // 600;
const circleRadius = 25;

const buttonStyle = {
  position: "absolute",
  top: 20,
  left: 20,
  color: "black",
  height: 45,
  opacity: 0.5,
  borderRadius: 5,
  cursor: "pointer"
}

/* GraphView */
class GraphView extends Component {
  state = {
    randomize: true
  }
  /* On mount */
  componentDidMount() {
    this.updateCanvas();
  }

  /* On state update */
  componentDidUpdate() {
    this.updateCanvas();
  }

  processGradient(gradient, color) {
    gradient.addColorStop(0.0, "white");
    gradient.addColorStop(0.8, color); // skyblue
    gradient.addColorStop(1.0, "transparent");
    return gradient;
  }

  /* Render the canvas */
  updateCanvas() {
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');
    const connections = this.props.graph.getConnectedComponents();
    const colors = ["skyblue", "limegreen", "pink", "yellow", "gray", "orange", "red"];

    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = "23px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    ctx.strokeStyle = "white";
    this.props.graph.vertexes.forEach(v => {
      v.edges.forEach(e => {
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
        ctx.stroke();
        ctx.fill();
      });
    });

    ctx.strokeStyle = "transparent";
    connections.forEach(connection => {
      const color = colors.shift() || "white";

      connection.forEach(v => {
        const x = v.pos.x, y = v.pos.y;
        const gradient = ctx.createRadialGradient(x, y, 0, x, y, circleRadius);

        ctx.strokeStyle = "transparent";
        ctx.beginPath();
        ctx.fillStyle = this.processGradient(gradient, color);
        ctx.arc(x, y, circleRadius, 0, Math.PI*2);
        ctx.stroke();
        ctx.fill();

        ctx.fillStyle = "black";
        ctx.fillText(v.value, x, y);
      });
    });
  }

  handleClick() {
    this.props.graph.randomize(5, 4, canvasHeight/5, 0.6);
  }
  
  /* Render */
  render() {
    return (
      <div width={canvasWidth} height={canvasHeight}>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
        <button onClick={() => this.handleClick()} style={buttonStyle}>randomize</button>
      </div>
    );
  }
}


/* App */
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      graph: new Graph(),
    };
    // this.state.graph.randomize(5, 4, canvasHeight/5, 0.6);
    this.state.graph.randomize(5, 4, 150, 0.6);
  }

  componentDidMount() {
    threeD(this.state.graph.vertexes, this.state.graph.getConnectedComponents());
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
