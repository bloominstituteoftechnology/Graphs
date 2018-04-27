import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

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
    let ctx = canvas.getContext('2d');

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    ctx.fillStyle = '#43C59E';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const vertexes = this.props.graph.vertexes;
    const radius = 10;

    for (let vertex of vertexes) {//Todo - Optimization: loop through vertex twice to resolve a draw problem
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let vertex of vertexes) {
      ctx.beginPath();
      ctx.strokeStyle="black";
      ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2*Math.PI);
      ctx.fillStyle = vertex.color;
      ctx.fill();
      ctx.stroke();

      ctx.font = "10px Arial";
      ctx.fillStyle = 'white';
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(vertex.value, vertex.pos.x ,vertex.pos.y);
    }

    //**********************Matrix Code************************
    //*********************************************************
    // const matrixText =  "123456789田由甲申甴电甶男甸甹町画甼甽甾甿畀畁NEO畄畅畆畇畈畉畊GUELMIS畍畎畏畐畑";
    // matrixText.split('');

    // const fontSize = 10;
    // const columns = canvasWidth / fontSize;
    // let drops = [];

    // for (let i = 0; i < columns; i++) {
    //   drops[i] = 1;
    // }

    // function draw() {
    //   ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    //   ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //   ctx.fillStyle = "#0f0";
    //   ctx.font = fontSize + "px arial";
    //   for (let j = 0; j < drops.length; j++) {
    //     const index = Math.floor(Math.random() * matrixText.length);
    //     const text = matrixText[index];
    //     ctx.fillText(text, j * fontSize, drops[j] * fontSize);

    //     if (drops[j] * fontSize > canvasHeight && Math.random() > 0.975) drops[j] = 0;

    //     drops[j]++;
    //   }
    // }

    // setInterval(draw, 40);

    //*********************************************************
    //*********************************************************

    // ctx.fillStyle = '#020122';
    // ctx.fillRect(0, 21, canvasWidth, 700);

    // for (let i = 0; i < 100; i++) {
    //   ctx.beginPath();
    //   ctx.moveTo(0,24);
    //   ctx.strokeStyle='rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ')';
    //   ctx.lineTo(70 * i, 200 + i);
    //   ctx.stroke();
    // }

    // for (let j = 0; j < 100; j++) {
    //   ctx.beginPath();
    //   ctx.moveTo(canvasWidth, 24);
    //   ctx.strokeStyle='rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ')';
    //   ctx.lineTo(70 * j, 200 + j);
    //   ctx.stroke();
    // }

    // for (let j = 0; j < 100; j++) {
    //   ctx.beginPath();
    //   ctx.moveTo(700, 50);
    //   ctx.strokeStyle='rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ')';
    //   ctx.lineTo(70 * j, 200 + j);
    //   ctx.stroke();
    // }

    // for (let j = 0; j < 100; j++) {
    //   ctx.beginPath();
    //   ctx.moveTo(700, 50);
    //   ctx.strokeStyle='rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ')';
    //   ctx.lineTo(70 * j, 200 + j);
    //   ctx.stroke();
    // }

    // for (let j = 0; j < 500; j++) {
    //   ctx.beginPath();
    //   ctx.strokeStyle="white";
    //   ctx.arc(200 + j ,120 + j,90,0,2*Math.PI);
    //   ctx.stroke();
    // }

    // for (let j = 0; j < 500; j++) {
    //   ctx.beginPath();
    //   ctx.strokeStyle="white";
    //   ctx.arc(1300 - j ,120 + j,90,0,2*Math.PI);
    //   ctx.stroke();
    // }
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
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.getConnectedComponents();
    // this.state.graph.debugCreateTestData();
    // console.log("in app constructor: ", this);
    // this.state.graph.dump();
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
