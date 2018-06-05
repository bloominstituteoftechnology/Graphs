import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = '750px';
const canvasHeight = '600px';

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
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // to draw lines, revisit
    // ctx.strokeStyle = 'red';
    // ctx.lineJoin = 'round';
    // ctx.lineCap = 'round';

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    const Particle = () => {
      this.x = canvas.width / 2;
      this.y = canvas.height / 2;
      this.vx = Math.random() * 10 - 1; // velocity of x axis
      this.vy = Math.random() * 10 - 1; // velocity of y axis
    };
    Particle.prototype.draw = () => {
      this.x += this.vx;
      this.y += this.vy;

      ctx.fillStyle = 'white';
      ctx.fillRect(this.x, this.y, 10, 10);
    };

    let particle = new Particle();

    setInterval(function() {
      // clear it, e.g. no "trail" as it moves
      ctx.fillStyle = 'black';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      particle.draw();
    }, 60);
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
      graph: new Graph(),
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
