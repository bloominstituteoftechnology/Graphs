import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 700;
const circleRadius = 20;

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

    // this.props.graph.createDummyGraph();

    ctx.fillStyle = "blue";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';


    let prevX = 0;
    let prevY = 0;

    this.props.graph.vertexes.forEach(vertex => {
      // Create Nodes/Vertices
      ctx.beginPath();
      ctx.fillStyle = "white";
      ctx.arc(vertex.pos.x, vertex.pos.y, circleRadius, 0, 2 * Math.PI)
      ctx.fill();
      ctx.stroke();

      // Create Edges
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      if (prevX > 0 && prevY > 0) ctx.lineTo(prevX, prevY);
      ctx.stroke();

      // Create Node/Verticies Labels
      ctx.beginPath();
      ctx.font = "10px Arial";
      ctx.fillStyle = "black";
      ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);

      prevX = vertex.pos.x;
      prevY = vertex.pos.y;
    })
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
    this.setState({ graph: this.state.graph.randomize(5, 4, 150, 0.6) })
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
