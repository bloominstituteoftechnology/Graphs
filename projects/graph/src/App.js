import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = (window.innerWidth-20);
const canvasHeight = (window.innerHeight-20);

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

  stack = [];

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    ctx.clearRect(0,0,canvasWidth,canvasHeight);
    ctx.fillStyle = '#FFCD7D';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    this.props.graph.vertexes.forEach((vertex) => {
      vertex.edges.forEach((edge) => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.lineWidth = 5;
        ctx.strokeStyle = '#FFFFFF';
        ctx.stroke();
        // this.stack.push(`
        //   ctx.moveTo(vertex.pos.x, vertex.pos.y);
        //   ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        //   ctx.lineWidth = 5;
        //   ctx.strokeStyle = '#FFFFFF';
        //   ctx.stroke();`
        // )
      })
    })
    this.props.graph.vertexes.forEach((vertex) => {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, Math.PI * 2, true);
      ctx.strokeStyle = '#EB9D20'; // EB9D20
      ctx.stroke();
      ctx.fillStyle = '#FFFFFF';
      ctx.fill();
      ctx.beginPath();
      ctx.font = '14px Georgia';
      ctx.fontStyle = 'bold';
      ctx.fillStyle = '#975D00';
      ctx.fillText(vertex.value, vertex.pos.x-7, vertex.pos.y+4);
      ctx.fill();
    })
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
        <button onClick = {() => {
            this.props.graph.vertexes = [];
            this.props.graph.randomize(3,3,150);
            this.updateCanvas();
          }}>New Graph</button>
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

    this.state.graph.randomize(3,3,150);
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
