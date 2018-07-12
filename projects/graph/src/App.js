import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;

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
    // canvas constants
    let canvas = this.refs.canvas;
    canvas.addEventListener("click", this.handleVertexClick, false);

    let ctx = canvas.getContext("2d");
    ctx.font = "11px serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    // clear canvas upon updating
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // vertex constant
    const vertexRadius = 10;
    // group of components
    const connectedComponents = this.props.graph.getConnectedComponents();
    // draw edges and vertices
    this.drawEdges(ctx, connectedComponents);
    this.drawVertexes(ctx, vertexRadius);
    this.drawWeights(ctx, connectedComponents);
  }

  handleVertexClick = e => {
    let canvas = this.refs.canvas;
    const vertexRadius = 10;
    let canvasLeft = canvas.offsetLeft; // finds the number of pixels from the top left the canvas is from its immediate container
    let canvasTop = canvas.offsetTop; // finds the number of pixels from the top the canvas is from its immediate container

    // find the x and y position of the click
    // event.pageX - x coordinate of the click relative to the left edge of the entire document
    // event.pageY - y coordinate of the click relative to the top edge of the entire document]

    let clickX = e.pageX - canvasLeft; // x position of the click inside the canvas
    let clickY = e.pageY - canvasTop; // y position of the click inside the canvas

    // detect collision between click and a vertex
    const vertexes = this.props.graph.vertexes;
    vertexes.forEach(v => {
      let x = v.pos.x;
      let y = v.pos.y;
      // valid clicks must occur within the boundaries of a vertex
      if (
        clickY > y - vertexRadius &&
        clickY < y + vertexRadius &&
        clickX > x - vertexRadius &&
        clickX < x + vertexRadius
      ) {
        console.log(`vertex ${v.value} was clicked`);
      }
    });
  };

  drawWeights(ctx, connectedComponents) {
    ctx.font = "20px serif";
    connectedComponents.forEach(component => {
      for (let v of component) {
        let x = v.pos.x;
        let y = v.pos.y;
        // draw the weight of a v's edges with the corresponding v color
        for (let edge of v.edges) {
          // not all vertexes will have edges
          if (edge.weight) {
            let edgeX = edge.destination.pos.x;
            let edgeY = edge.destination.pos.y;
            // find the midpoint between a vertex and its edge - this is where the weight will be written
            let weightX = (x + edgeX) / 2;
            let weightY = (y + edgeY) / 2;
            ctx.beginPath();
            ctx.moveTo(weightX, weightY);
            ctx.fillStyle = v.color;
            ctx.fillText(`${edge.weight}`, weightX, weightY);
            ctx.closePath();
          }
        }
      }
    });
  }

  colorVertexes() {
    let redOffset = Math.random() * 256;
    let greenOffset = Math.random() * 256;
    let blueOffset = Math.random() * 256;
    // create a random color
    let color = `rgb(${redOffset}, ${greenOffset}, ${blueOffset})`;
    return color;
  }

  drawEdges(ctx, connectedComponents) {
    // draw and color edges of connected components
    connectedComponents.forEach(component => {
      let componentColor = this.colorVertexes(); // obtain a color for each component in the list of connected components
      for (let v of component) {
        let x = v.pos.x;
        let y = v.pos.y;
        v.color = componentColor;
        // draw each edge with the color of its component
        for (let edge of v.edges) {
          let edgeX = edge.destination.pos.x;
          let edgeY = edge.destination.pos.y;
          // draw a line to each connected component
          ctx.beginPath();
          ctx.strokeStyle = v.color; // color of component
          ctx.moveTo(x, y);
          ctx.lineTo(edgeX, edgeY);
          ctx.fill();
          ctx.stroke();
          ctx.closePath();
        }
      }
    });
  }

  drawVertexes(ctx, vertexRadius) {
    const vertexes = this.props.graph.vertexes;
    // draw vertexes of the graph instance
    vertexes.forEach(vertex => {
      let x = vertex.pos.x;
      let y = vertex.pos.y;
      ctx.beginPath();
      ctx.fillStyle = vertex.color;
      ctx.strokeStyle = "black";
      ctx.arc(x, y, vertexRadius, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
      // draw vert values (labels)
      ctx.fillStyle = "black";
      ctx.fillText(`${vertex.value}`, x, y);
      ctx.closePath();
    });
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
    const g = this.state.graph;
    g.randomize(5, 4, 150, 0.6);
  }

  generateGraph = e => {
    // generate a new instance of Graph, save it to state, and call randomize to generate vertexes and edges
    const newGraph = new Graph();
    this.setState({ graph: newGraph });
    newGraph.randomize(5, 4, 150, 0.6);
  };

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <button onClick={this.generateGraph}>Generate Graph</button>
      </div>
    );
  }
}

export default App;
