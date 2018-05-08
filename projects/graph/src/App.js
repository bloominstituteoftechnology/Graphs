import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 700;

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
    function random(min, max) {
      let int = Math.random() * (max - min) + min;
      return Math.floor(int);
    }

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'rgb(10, 10, 10)';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    let w = 1000;
    let h = 700;
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(0, 0);
      ctx.lineTo(w, h);
      ctx.lineWidth = 1;
      ctx.strokeStyle = '#AA0000';
      ctx.stroke();
      ctx.closePath();
      w -= 10;
    }

    w = 0;
    h = 700;
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(500, 0);
      ctx.lineTo(w, h);
      ctx.strokeStyle = '#AA0000';
      ctx.stroke();
      ctx.closePath();
      w += 10;
    }

    w = 0;
    h = 700;
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(1000, 0);
      ctx.lineTo(w, h);
      ctx.strokeStyle = '#AA0000';
      ctx.stroke();
      ctx.closePath();
      w += 10;
    }

    w = 0;
    h = 0;
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(0, 700);
      ctx.lineTo(w, h);
      ctx.strokeStyle = '#AA0000';
      ctx.stroke();
      ctx.closePath();
      w += 10;
    }

    w = 0;
    h = 0;
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(1000, 700);
      ctx.lineTo(w, h);
      ctx.strokeStyle = '#AA0000';
      ctx.stroke();
      ctx.closePath();
      w += 10;
    }

    w = 0;
    h = 0;
    for (let i = 0; i < 100; i++) {
      ctx.beginPath();
      ctx.moveTo(500, 700);
      ctx.lineTo(w, h);
      ctx.strokeStyle = '#AA0000';
      ctx.stroke();
      ctx.closePath();
      w += 10;
    }

    for (let i = 0; i < 10000; i++) {
      ctx.beginPath();
      ctx.fillStyle = `rgba(10, 10, 10, ${Math.random()})`;
      ctx.fillRect(random(10, 1000), random(10, 700), random(1, 10), random(1, 10));
      ctx.closePath();
    }

    this.props.graph.vertexes.forEach(v => {
      // Draw edges
      v.edges.forEach(e => {
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
        ctx.strokeStyle = 'white';
        ctx.stroke();
        ctx.closePath();
      });

      ctx.beginPath();
      // Draw vertex circles
      ctx.strokeStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, 20, 0, 2*Math.PI);
      ctx.fillStyle = 'black';
      ctx.fill();
      ctx.stroke();
      // Draw vertex labels
      ctx.fillStyle = 'white';
      ctx.font = '20px Georgia';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(v.value, v.pos.x, v.pos.y);

      ctx.closePath();
    });
    console.log(this.props.graph);
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
    // this.state.graph.debugCreateVertex();
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
