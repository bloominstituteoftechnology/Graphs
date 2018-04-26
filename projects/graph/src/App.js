import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
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
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    ctx.fillStyle = 'cyan';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const radius = 10;
    const vertexes = this.props.graph.vertexes;
    // ctx.beginPath();
    // ctx.arc(vertexes[0].pos.x, vertexes[0].pos.y, radius, 0, 2*Math.PI);
    // ctx.fillStyle = 'white';
    // ctx.fill();
    // ctx.stroke();

    // ctx.font = '12px Arial';
    // ctx.fillStyle = 'black';
    // ctx.fillText(vertexes[0].value, vertexes[0].pos.x, vertexes[0].pos.y);

    for (let i = 0; i < vertexes.length; i++) {
      ctx.beginPath();
      ctx.arc(vertexes[i].pos.x, vertexes[i].pos.y, radius, 0, 2*Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.stroke();

      ctx.font = '12px Arial';
      ctx.fillStyle = 'black';
      ctx.fillText(vertexes[i].value, vertexes[i].pos.x, vertexes[i].pos.y - radius);

      console.log("EDGES", vertexes[i].edges);
      for (let j = 0; j < vertexes[i].edges.length; j++) {
        ctx.beginPath();
        ctx.moveTo(vertexes[i].pos.x, vertexes[i].pos.y);
        ctx.lineTo(vertexes[i].edges[j].destination.pos.x, vertexes[i].edges[j].destination.pos.y);
        ctx.fillStyle = 'black';
        ctx.stroke();
      }
      // if (vertexes[i + 1]) {
      //   ctx.beginPath();
      //   ctx.moveTo(vertexes[i].pos.x + radius, vertexes[i].pos.y)
      //   ctx.lineTo(vertexes[i + 1].pos.x, vertexes[i + 1].pos.y);
      //   ctx.fillStyle = 'black';
      //   ctx.stroke();
      // }
    }
    
    // Clear it
    // const gradient = ctx.createLinearGradient(0, 0, 500, 500)
    // gradient.addColorStop(0, 'red');
    // gradient.addColorStop(0.15, 'orange');
    // gradient.addColorStop(0.3, 'yellow');
    // gradient.addColorStop(0.45, 'green');
    // gradient.addColorStop(0.6, 'blue');
    // gradient.addColorStop(0.75, 'indigo');
    // gradient.addColorStop(0.9, 'violet');
    // const gradient2 = ctx.createLinearGradient(0, 0, 500, 500)
    // gradient2.addColorStop(0, 'violet');
    // gradient2.addColorStop(0.15, 'indigo');
    // gradient2.addColorStop(0.3, 'blue');
    // gradient2.addColorStop(0.45, 'green');
    // gradient2.addColorStop(0.6, 'yellow');
    // gradient2.addColorStop(0.75, 'orange');
    // gradient2.addColorStop(0.9, 'red');
    // ctx.fillStyle = gradient;
    // ctx.strokeStyle = gradient2;
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    // for (let i = 0; i < 100; i++) {
      // ctx.beginPath();
      // ctx.arc(75 + i, 75 + i, 50 * i, 0, Math.PI * 2, true); // Outer circle
      // ctx.arc(50 * 2 * i, 50 + 10 * i, 80, 0, Math.PI * 2);
      // for (let i = 0; i < 100; i++) {
      //   ctx.strokeRect(50 + 14 * i, 50 + 10 * i, 40, 40);
      //   ctx.strokeRect(500 + 5 * i, 300 + 5 * i, 50, 50);
      //   ctx.rotate(i * Math.PI/180);
      //   for (let j = 0; j < 100; j++) {
          // ctx.strokeRect(8 * i, 50 + i, 10 + 2 * i, 20 + 3 * i);
          // ctx.strokeRect(10 + 8 * j, 10 + 5 * j, 10 + 6 * j, 10 + 8 * j);
        // }

        // ctx.bezierCurveTo(10 * i, 10 * i, 40 + i, 50 + i, 200 + i, 70 + 5 * i);
        // ctx.bezierCurveTo(500 + i, 100 + i, 40 + i, 60 + i, 900 - i, 1000 - 5 * i);
      // }
      // ctx.stroke();
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

    this.state.graph.randomize(5, 4, 200, 0.6);
    this.state.graph.getConnectedComponents();
    this.state.graph.dump();
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
