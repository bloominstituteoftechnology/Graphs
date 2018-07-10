import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleRadius = 15;

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
  updateCanvas = () => {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.props.graph.vertexes = [];
    this.props.graph.randomize(5, 4, 150);

    // Clear it
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // !!! IMPLEMENT ME
    const getRandomInt = max => Math.floor(Math.random() * Math.floor(max));
    const getRandomColor = () => `rgb(${getRandomInt(256)}, ${getRandomInt(256)}, ${getRandomInt(256)})`;
    const groups = this.props.graph.getConnectedComponents();

    groups.forEach(group => {
      // compute connected components
      // draw edges
      group.forEach(v => {
        ctx.strokeStyle = 'black';

        v.edges.forEach(edge => {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        });
      });

      // draw verts
      // draw vert values (labels)
      const color = getRandomColor();
      group.forEach(v => {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();
  
        // fill in the text
        ctx.fillStyle = 'white';
        ctx.fillText(v.value, v.pos.x, v.pos.y);
      });
    });

    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);
  }
  
  /**
   * Render
   */
  render() {
    return (
    <div>
      <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
      <button onClick={this.updateCanvas}>Generate New Graph</button>
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
