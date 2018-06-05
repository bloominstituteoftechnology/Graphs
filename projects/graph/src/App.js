import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleSize = 15;

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
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

  generateBubbles(num) {
    let bubbles = [];
    for (let i = 0; i < num; i++) {
      let bubble = {};
      bubble.color = `rgba(${getRandomInt(1, 100)}, ${getRandomInt(
        1,
        255
      )}, ${getRandomInt(200, 255)}, ${Math.random() / 1.2})`;
      bubble.x = getRandomInt(1, canvasWidth);
      bubble.y = getRandomInt(1, canvasHeight);
      bubble.r = getRandomInt(1, 20);
      bubble.speed = 1 / (bubble.r / 20);
      bubbles.push(bubble);
    }
    return bubbles;
  }
  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");

    console.log("In update canvas", this.props);
    // let bubbles = this.generateBubbles(1000);
    // // Clear it
    // setInterval(() => {
    ctx.fillStyle = "darkblue";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fill();

    //   for (let i = 0; i < bubbles.length; i++) {
    //     ctx.fillStyle = `${bubbles[i].color}`;
    //     ctx.beginPath();
    //     ctx.arc(bubbles[i].x, bubbles[i].y, bubbles[i].r, 0, 2 * Math.PI);
    //     ctx.fill();
    //     // ctx.stroke();
    //     bubbles[i].y -= bubbles[i].speed;
    //     if (bubbles[i].y < 0) bubbles[i].y = canvasHeight;
    //   }
    // }, 50);

    // ctx.
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = "white";
      ctx.fill();
      ctx.stroke();

      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.font = "16px Arial";
      ctx.fillStyle = "black";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      for (let edge of vertex.edges) {
        console.log("Edge: ", edge);
        ctx.fillStyle = "black";
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
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
    this.state.graph.randomize(5, 4, 150, 0.6);
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
