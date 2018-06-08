import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 600;

const circleSize = 15;

const width = 6;
const height = 4;
const pxBox = 150;
const probability = 0.6;

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
    let clear = true;

    // Code for Original Solution
    // const getRandomColor = () => {
    //   let letters = '0123456789ABCDEF';
    //   let color = '#';
    //   for (let i = 0; i < 6; i++) {
    //     color += letters[Math.floor(Math.random() * 16)];
    //   }
    //   return color;
    // };

    // Clear it
    if (clear) {
      ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    }

    // Don't need this code below because made the whole body one color
    // Canvas
    // ctx.fillStyle = 'rgb(0, 206, 209)';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log('in updateCanvas', this.props.graph.vertexes);

    // Text Inside Vertices
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';
    ctx.fillStyle = 'black';

    // To Do: figure out if there is a way to do this without looping through vertices twice

    // Edges
    ctx.lineWidth = 2;

    // For original implementation
    // ctx.strokeStyle = getRandomColor();

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        console.log();
        ctx.beginPath();
        ctx.strokeStyle = vertex.color;
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    // Vertices
    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.strokeStyle = vertex.color;

      ctx.fillStyle = vertex.color; // TODO: Make variable
      ctx.fill();
      ctx.fillStyle = 'black'; // TODO: Make variable
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.stroke();
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
    this.newGraphButton = this.newGraphButton.bind(this);

    this.state = {
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method

    this.state.graph.randomize(width, height, pxBox, probability);
    this.state.graph.getConnectedComponents();
  }

  newGraphButton() {
    const state = {
      graph: new Graph()
    };

    state.graph.randomize(width, height, pxBox, probability);
    state.graph.getConnectedComponents();

    this.setState(state);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <button onClick={this.newGraphButton}>New Graph</button>
      </div>
    );
  }
}

export default App;
