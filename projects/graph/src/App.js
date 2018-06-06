import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
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
  // START FO MY CUSTOM FUNCTIONS

  experimentalDraw(canvas, ctx) {
    ctx.fillStyle = 'lightblue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // // Create a gradient
    const rGrd = ctx.createRadialGradient(75, 50, 5, 90, 60, 100);
    rGrd.addColorStop(0, 'orange');
    rGrd.addColorStop(0.5, 'yellow');
    rGrd.addColorStop(1, 'lightblue');

    // // Fill with gradient
    ctx.fillStyle = rGrd;
    ctx.fillRect(0, 0, 200, 150);

    // Create gradient
    const lGrd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
    lGrd.addColorStop(0, 'blue');
    lGrd.addColorStop(0.5, 'yellow');
    lGrd.addColorStop(1, 'brown');

    // Fill with gradient
    ctx.fillStyle = lGrd;
    ctx.fillRect(0, 200, canvasWidth, canvasHeight);
  }

  drawEdges(ctx) {
    let vertexes = this.props.graph.vertexes;

    vertexes.forEach(vertex => {
      vertex.edges.forEach(edge => {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      });
    });
  }

  drawVertexes(ctx) {
    let vertexes = this.props.graph.vertexes;
    //console.log(vertexes[0].edges);

    vertexes.forEach(vertex => {
      ctx.beginPath();
      // draw the vertex
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = vertex.color;
      console.log(vertex);
      ctx.fill();
      ctx.stroke();

      // fill in the value
      ctx.fillStyle = 'black';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '16px Arial';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    });
  }

  // END OF MY CUSTOM FUNCTIONS
  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'gray';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //this.experimentalDraw(canvas, ctx);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    this.drawEdges(ctx);
    this.drawVertexes(ctx);
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
    // this.state.graph.debugCreateVertexes();
    this.state.graph.randomize(5, 4, 150, 0.6);
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
