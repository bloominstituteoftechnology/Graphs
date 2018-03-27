import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 700;
const canvasHeight = 480;
const vertexRadius = 10;
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
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = '#FF0000';
    ctx.fillStyle = "lightgray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log("this.props", this.props);
    // console.log("updating canvas");
    // console.log(this.props.graph.vertexes);
    console.log("edge", this.props.graph.vertexes[0].edges[0]);
    // var vertex = this.props.graph.vertexes[0];

    // let parentVert = this.props.graph.vertexes[0];
    let debugEdge = this.props.graph.vertexes[0].edges[0];
    console.log("debugEdge is", debugEdge);

    for (let parentVert of this.props.graph.vertexes) {
      for (let debugEdge of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(debugEdge.destination.pos.x, debugEdge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let vertex of this.props.graph.vertexes) {
      // node 1
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, Math.PI * 2);
      ctx.stroke();

      // value 1
      ctx.fillStyle = "white";
      ctx.fill();
      ctx.fillStyle = "black";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle"
      ctx.font = "10px Helvetica";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    // // line 1
    // ctx.moveTo(50, 50);
    // ctx.lineTo(100, 100);
    // ctx.stroke();

    // // node 1
    // ctx.beginPath();
    // ctx.moveTo(60, 50);
    // ctx.arc(50, 50, 10, 0, 2 * Math.PI, true);
    // ctx.fill();
    // ctx.stroke();

    // // num 1
    // ctx.beginPath();
    // ctx.font = "10px Helvetica";
    // ctx.strokeText("1", 48, 53);
    // ctx.stroke();

    // // node 2
    // ctx.arc(100, 100, 10, 0, 2 * Math.PI, true);
    // ctx.fill();
    // ctx.stroke();

    // // num 2
    // ctx.font = "10px Helvetica";
    // ctx.strokeStyle = "black";
    // ctx.strokeText("2", 98, 102);
    // ctx.stroke();

  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
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
    this.state.graph.debugCreateTestData();
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
