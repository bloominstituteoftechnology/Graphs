import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = '750px';
const canvasHeight = '600px';

const circleSize = 15;

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
    ctx.fillStyle = 'hsl(209.2, 49%, 64%)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    console.log('in updateCanvas', this.props.graph.vertexes);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';

    // Figure if there is a way to do this w/o looping through vertexes twice?
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
      console.log('edges of vertices: ', vertex.edges);
    }

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.stroke();
    }

    // to draw lines, revisit
    // ctx.strokeStyle = 'red';
    // ctx.lineJoin = 'round';
    // ctx.lineCap = 'round';

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    // const Particle = () => {
    //   this.x = canvas.width / 2;
    //   this.y = canvas.height / 2;
    //   this.vx = Math.random() * 10 - 1; // velocity of x axis
    //   this.vy = Math.random() * 10 - 1; // velocity of y axis
    // };
    // Particle.prototype.draw = () => {
    //   this.x += this.vx;
    //   this.y += this.vy;

    //   ctx.fillStyle = 'white';
    //   ctx.fillRect(this.x, this.y, 10, 10);
    // };

    // let particle = new Particle();

    // setInterval(function() {
    //   // clear it, e.g. no "trail" as it moves
    //   ctx.fillStyle = 'hsl(209.2, 49%, 64%)';
    //   ctx.fillRect(0, 0, canvas.width, canvas.height);

    //   particle.draw();
    // }, 60);
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

    this.state.graph.randomize(5, 4, 150, 0.6);
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
