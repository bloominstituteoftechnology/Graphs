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

    function random(min, max) {
      let int = Math.random() * (max - min) + min;
      return Math.floor(int);
    }

    for (let i = 0; i < 10000; i++) {
      ctx.beginPath();
      ctx.fillStyle = `rgba(10, 10, 10, ${Math.random()})`;
      ctx.fillRect(random(10, 1000), random(10, 700), random(1, 10), random(1, 10));
      ctx.closePath();
    }

    // for (let i = 0; i < 200; i++) {
    //   ctx.beginPath();
    //   ctx.arc(random(100, 900), random(100, 600), random(1, 30), 0, 360);
    //   ctx.strokeStyle = `rgba(21, 0, 0, ${Math.random() * (0.2) + 0.1})`;
    //   ctx.lineWidth = 4;
    //   ctx.stroke();
    //   ctx.closePath();
    // }

    for (let i = 0; i < 1000; i++) {
      ctx.beginPath();
      ctx.font='30px sans-serif';
      ctx.strokeStyle = `rgba(0, 250, 0, ${Math.random()})`;
      ctx.strokeText(`${String.fromCharCode(random(65, 85))}`, random(100, 900), random(100, 700));
      ctx.rotate(random(0, 360)*Math.PI/180);
      ctx.closePath();
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
