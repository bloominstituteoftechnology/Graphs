import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

const getRandomColor = () => {
  let letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
};
// !!! IMPLEMENT ME
const canvasWidth = 750;
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
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    const canvasRadius = 20;
    const vertexes = this.props.graph.vertexes;

    for (let component of this.props.connectedComponents) {
      const color = getRandomColor();
      ctx.strokeStyle = color;
      ctx.lineWidth = 5;
      //Each vertex gets looped through
      for (let i = 0; i < component.length; i++) {
        const vertex = vertexes[component[i]];
        //Draw an edge in a random color
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        }
      }

      // !!! IMPLEMENT ME
      // compute connected components
      // draw edges
      // draw verts
      // draw vert values (labels)
      //overlap
      ctx.lineWidth = 4;
      for (let i = 0; i < component.length; i++) {
        const vertex = vertexes[component[i]];
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, canvasRadius, 0, 2 * Math.PI);
        ctx.fillStyle = "white";
        ctx.fill();
        ctx.stroke();
        ctx.font = "bold 12px Roboto";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillStyle = "black";
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
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
      graph: new Graph(),
      connectedComponents: []
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method

    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.connectedComponents = this.state.graph.getConnectedComponents();
  }

  render() {
    return (
      <div className="App">
        <GraphView
          graph={this.state.graph}
          connectedComponents={this.state.connectedComponents}
        />{" "}
      </div>
    );
  }
}

export default App;
