import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 10;

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

  getRandomColor() {
    let color = ((Math.random() * 240)|0).toString(16);

    if (color.length === 1) {
      color = '0' + color;
    }
    return color;
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    const connectedComponents = this.props.graph.getConnectedComponents();

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    ctx.filter = 'blur(0.5px)';
    
    // Clear it
    ctx.fillStyle = 'lightgrey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Draw edges first
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    // Now draw vertices and text
    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.font = "11px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }

    for (let item of connectedComponents) {
      item = item[0];
      const newColor = '#' + this.getRandomColor() + this.getRandomColor() + this.getRandomColor();
      ctx.beginPath();
      ctx.arc(item.pos.x, item.pos.y, vertexRadius, 0, 2 * Math.PI);
      ctx.fillStyle = newColor;
      ctx.fill();
      ctx.stroke();
    }
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
    this.state.graph.randomize(5, 4, 150, 0.6);
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
