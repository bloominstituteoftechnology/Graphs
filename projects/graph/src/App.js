import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleRadius = 23;

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

    this.drawVertexes(ctx);
  }
  
  drawVertexes(ctx) {
    // Style the canvas
    ctx.fillStyle = "lightblue";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    // Aligns text
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

  const connectedList = this.props.graph.getConnectedComponents();

  connectedList.forEach(connectedComponent => { 
    // Create Edges
    ctx.strokeStyle = this.getRandomColor();
    connectedComponent.forEach(vertex => {
      vertex.edges.forEach(edge => {
        const x1 = vertex.pos.x;
        const y1 = vertex.pos.y;
        const x2 = edge.destination.pos.x;
        const y2 = edge.destination.pos.y;
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.stroke();
      })
    })

    connectedComponent.forEach(vertex => {
      const x = vertex.pos.x;
      const y = vertex.pos.y;
      // Create Nodes/Vertices
      ctx.beginPath();
      ctx.fillStyle = ctx.strokeStyle;
      ctx.arc(x, y, circleRadius, 0, 2 * Math.PI)
      ctx.fill();
      
      // Create Node/Verticies Labels
      ctx.beginPath();
      ctx.font = "16px Arial";
      ctx.fillStyle = "white";
      ctx.fillText(vertex.value, x, y);
      })
    })
  }

  getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
        <button className="App__Button" onClick={() => this.props.clickHandler()}>New Graph</button>
        <br/>
        <canvas className="Canvas" ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
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
      graph: new Graph(),
      connectedList: []
    };
    this.state.graph.randomize(5, 4, 150, 0.6);
  }

  clickHandler = () => {
    let graph = new Graph();
    graph.randomize(5, 4, 150, 0.6);
    this.setState({ graph: graph })
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={ this.state.graph } clickHandler={ this.clickHandler } />
      </div>
    );
  }
}

export default App;