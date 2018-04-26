import React, { Component, version } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasHeight = 800;
const canvasWidth = 1200;

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

  randomizeColor(colorCode = "") {
    if (colorCode.length === 6) return "#" + colorCode;
    const randomColor = ((Math.random() * 240) | 0).toString(16);
    colorCode += randomColor.length === 1 ? "0" + randomColor : randomColor;
    return this.randomizeColor(colorCode);
  }
  
  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = '#80CBC4';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const vertexes = this.props.graph.vertexes;
    const radius = 20;

    for (let vertex of vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.strokeStyle = this.randomizeColor();
        ctx.stroke();
      }
    }

    for (let vertex of vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2*Math.PI);
      ctx.fillStyle = this.randomizeColor();
      ctx.fill();
      ctx.stroke();
      ctx.font = "12px Verdana";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillStyle = "white";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
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
    this.state.graph.randomize(5, 7, 111, 0.6);
    this.state.graph.bfs(0);
  }

  onHandleClick = () => {
    const graph = new Graph();
    graph.randomize(5, 7, 111, 0.6);
    this.setState({graph});
  }


  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.onHandleClick}>Generate New Graph</button>
      </div>
    );
  }
}

export default App;
