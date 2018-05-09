import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 700;
const pxBox = 150;

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

    // Draw background
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
      ctx.fillRect(
        random(10, 1000),
        random(10, 700),
        random(1, 10),
        random(1, 10)
      );
      ctx.closePath();
    }
    // End draw background

    // Draw Graph

    let colors = [
      'black',
      'darkgreen',
      'maroon',
      'darkblue',
      'purple',
      'darkorange',
      'lightblue'
    ];

    this.props.graph.connectedComponents.forEach((component, i) => {
      component.forEach(v => {
        v.edges.forEach(e => {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
          ctx.strokeStyle = 'rgba(100, 100, 100)';
          ctx.lineWidth = 5;
          ctx.stroke();
          ctx.closePath();
        });
      });

      component.forEach(v => {
        ctx.beginPath();
        // Draw vertex circles
        ctx.strokeStyle = 'rgb(100, 100, 100)';
        ctx.arc(v.pos.x, v.pos.y, 25, 0, 2 * Math.PI);
        ctx.fillStyle = colors[i];
        ctx.fill();
        ctx.stroke();
        // Draw vertex labels
        ctx.fillStyle = 'rgb(200, 200, 200)';
        ctx.font = '20px Georgia';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(v.value, v.pos.x, v.pos.y);

        ctx.closePath();
      });
    });
  }

  regenerateHandler = () => {
    // this.setState({ state: this.state });
    this.props.graph.reset();

    this.props.graph.randomize(
      Math.floor(canvasWidth / pxBox),
      Math.floor(canvasHeight / pxBox),
      pxBox,
      0.6
    );

    this.props.graph.getConnectedComponents();

    this.updateCanvas();

    console.log('BANG');
  };

  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />
        <button
          onClick={() => {
            this.regenerateHandler();
          }}
        >
          REGENERATE
        </button>
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

    this.state.graph.randomize(
      Math.floor(canvasWidth / pxBox),
      Math.floor(canvasHeight / pxBox),
      pxBox,
      0.6
    );

    this.state.graph.getConnectedComponents();
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
