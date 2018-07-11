import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 640;
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

    // Style the canvas
    ctx.fillStyle = "lightblue";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Aligns text
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // Create Edges
    this.props.graph.vertexes.forEach(vertex => {
      vertex.edges.forEach(edge => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y)
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      })
    })
    
    // Create Nodes/Vertices
    this.props.graph.vertexes.forEach(vertex => {
      ctx.beginPath();
      ctx.fillStyle = "white";
      ctx.arc(vertex.pos.x, vertex.pos.y, circleRadius, 0, 2 * Math.PI)
      ctx.fill();
      ctx.stroke();

      // Create Node/Verticies Labels
      ctx.beginPath();
      ctx.font = "10px Arial";
      ctx.fillStyle = "black";
      ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);
    })

    // BFS
    this.props.graph.vertexes.forEach(vertex => {
      this.props.graph.bfs(vertex);
    })
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
        <button className="App__Button" onClick={() => this.props.clickHandler()}>New Graph</button>
        <br/>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
      </div>
    )
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
    this.state.graph.randomize(5, 4, 150, 0.6)
  }
  clickHandler = () => {
    let graph = new Graph();
    graph.randomize(5, 4, 150, 0.6);
    this.setState({ graph: graph })
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} clickHandler={this.clickHandler}></GraphView>
      </div>
    );
  }
}

export default App;
