import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;
const radius = 20;

function drawLine(startx, starty, finx, finy, ctx) {
  ctx.strokeStyle = 'black';
  ctx.moveTo(startx, starty)
  ctx.lineTo(finx, finy);
}

function drawCircle(vertex, ctx) {
  ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2*Math.PI);
  var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
  chooseAColor(vertex, ctx);
  writeTheText(vertex, ctx);
}

function chooseAColor(vertex, ctx) {
  let color = 'white';
  const len = vertex.edges.length;
  switch (true) {
    case len === 0:
      color = 'maroon';
      break;
    case len === 1:
      color = 'lightblue';
      break;
    case len === 2:
      color = 'lightskyblue';
      break;
    case len === 3:
      color = 'dodgerblue';
      break;
    case len === 4:
      color = 'blue';
      break;
    case len >= 5:
      color = 'purple';
      break;
    default:
      color = 'orange';
      break;      
  }
  ctx.fillStyle = color;
  ctx.fill();
}

function writeTheText(vertex, ctx) {
  ctx.fillStyle = 'white';
  ctx.font = '20px Arial';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.props.graph.randomize(5, 5, 150, 0.6);
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
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fillStyle = 'white';
    ctx.fillRect(2, 2, canvasWidth-4, canvasHeight-4);
    ctx.lineWidth = 5;
    
    for (let vertex of this.props.graph.vertexes) {
      // console.log(vertex);
      ctx.beginPath();
      for (let edge of vertex.edges) {
        drawLine(vertex.pos.x, vertex.pos.y, edge.destination.pos.x, edge.destination.pos.y, ctx);
      }
      ctx.stroke();
    }
    ctx.lineWidth = 3;
    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath()
      drawCircle(vertex, ctx);
      ctx.stroke();
    }

    // !!! IMPLEMENT ME


    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
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