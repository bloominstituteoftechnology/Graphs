import React, { Component } from 'react';
import { Edge, Vertex, Graph } from './graph';
import './App.css';
import img from './images/picasso00.jpg';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const CIRCLE_RADIUS = 25;

/**
 * GraphView
 */
class GraphView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      vertexes: this.props.graph.vertexes
    };
  }
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

    /*
    ctx.fillStyle = "yellow";
    ctx.fillRect(50, 50, 350, 200);

    ctx.fillStyle = "green";
    ctx.fillRect(100, 50, 250, 100);

    let grd = ctx.createLinearGradient(0, 0, 170, 0);
    grd.addColorStop(0, "black");
    grd.addColorStop(1, "white");

    ctx.fillStyle = grd;
    ctx.fillRect(0, 75, 350, 25);

    const lineObjMkr = (a, b) => {
      ctx.moveTo(a, b);
      ctx.lineTo(100, 100);
      ctx.stroke();
    };

    lineObjMkr(100, 0);*/

    // ctx.strokeStyle = "red";

    /*ctx.shadowBlur = 20;
    ctx.shadowColor = "black";
    ctx.shadowOffsetX = 50;

    let grd = ctx.createLinearGradient(0, 0, 150, 0);
    grd.addColorStop(0, "black");
    grd.addColorStop(1, "white");

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, 400, 150);

    // let grd1 = ctx.createLinearGradient(0, 0, 150, 0);
    // grd1.addColorStop(0, "white");
    // grd1.addColorStop(1, "black");

    // ctx.fillStyle = grd1;
    // ctx.fillRect(150, 0, 150, 150);

    for (let i = 0; i < 100; i++) {
      ctx.strokeStyle = `rgb(100, ${i}, 100`;
      ctx.beginPath();
      ctx.arc(150, i, i, 0, 1 * Math.PI);
      ctx.stroke();
    }

    ctx.font = "30px Arial";
    ctx.fillStyle = "red";
    ctx.textAlign = "center";
    ctx.fillText("3d", canvas.width / 2, canvas.height / 2);
    console.log(canvas.height + " " + canvas.width);

    ctx.fillStyle = "red";
    ctx.fillRect(135, 45, 30, 60);*/

    //Clear it
    ctx.fillStyle = 'rgb(0, 206, 209)';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log(this.state.vertexes[0].pos);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    for (let vertex of this.state.vertexes) {
      for (let edge of vertex.edges) {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.fillStyle = 'black';
        ctx.stroke();
      }

      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, CIRCLE_RADIUS, 0, 2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();

      ctx.font = '16px Arial';
      ctx.fillStyle = 'black';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.stroke();
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
    this.state.graph.randomize(5, 4, 150);
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
