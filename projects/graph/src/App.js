import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleSize = 15;

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
    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");
    let graph = this.props.graph;
    let start, end;

    canvas.addEventListener(
      "click",
      function(event) {
        console.log(`Clicked the canvas at ${event.pageX}, ${event.pageY}`);
        const x = event.pageX - canvas.offsetLeft;
        const y = event.pageY - canvas.offsetTop;
        let clickedVertex;

        for (let vertex of graph.vertexes) {
          if (
            Math.abs(vertex.pos.x - x) <= circleSize &&
            Math.abs(vertex.pos.y - y) <= circleSize
          ) {
            clickedVertex = vertex;
            if (!start) {
              start = clickedVertex;

              ctx.textAlign = "center";
              ctx.textBaseline = "middle";
              ctx.font = "16px Arial";
              ctx.fillStyle = "black";

              ctx.fillText("START", vertex.pos.x, vertex.pos.y + 20);
            } else if (!end) {
              end = clickedVertex;
              ctx.textAlign = "center";
              ctx.textBaseline = "middle";
              ctx.font = "16px Arial";
              ctx.fillStyle = "black";

              ctx.fillText("END", vertex.pos.x, vertex.pos.y + 20);
              graph.highlightShortestPath(start, end);
              console.log("You clicked: ", clickedVertex, start, end);
              // start = null;
              // end = null;
            }
          }
        }
      },
      false
    );

    console.log("In update canvas", this.props);
    // let bubbles = this.generateBubbles(1000);
    // // Clear it
    // setInterval(() => {
    ctx.fillStyle = "darkslategrey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fill();

    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.font = "16px Arial";
    ctx.fillStyle = "black";

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        // ctx.fillStyle = "black";
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.strokeStyle = vertex.color;
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        ctx.fillText(
          edge.weight,
          (vertex.pos.x + edge.destination.pos.x) / 2,
          (vertex.pos.y + edge.destination.pos.y) / 2
        );
      }
    }

    for (let vertex of this.props.graph.vertexes) {
      console.log("VERTEXES: ", vertex);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = vertex.color;
      ctx.strokeStyle = "white";
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "black";

      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
  }

  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas id="canvas" width={canvasWidth} height={canvasHeight} />
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

    // !!! IMPLEMENT ME
    this.state.graph.randomize(5, 4, 150, 0.6);
    // use the graph randomize() method
  }
  render() {
    this.state.graph.getConnectedComponents();
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <button
          onClick={() => {
            let blankGraph = this.state.graph;
            blankGraph.vertexes = [];
            this.setState({ graph: blankGraph });
            this.state.graph.randomize(5, 4, 150, 0.6);
            this.setState({ graph: this.state.graph }); // Lazy way? Is there a better way to force a re-render?
          }}
        >
          RELOAD
        </button>
      </div>
    );
  }
}

export default App;
