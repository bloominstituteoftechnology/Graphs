import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 12;
const graphX = 5, graphY = 4, boxSize = 150, probability = 0.6;
let searchType;

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
    const getRandomColor = () => {
      let color = ((Math.random() * 240)|0).toString(16);

      if (color.length === 1) {
        color = '0' + color;
      }
      return color;
    }

    let connectedComponents;

    switch(searchType) {
      case 'BFS':
        connectedComponents = this.props.graph.getConnectedComponentsBFS();
        break;
      case 'DFS':
        connectedComponents = this.props.graph.getConnectedComponentsDFS();
        break;
      default:
        connectedComponents = this.props.graph.getConnectedComponentsBFS();
        break;
    }

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'darkgrey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let group of connectedComponents) {
      const newColor = '#' + getRandomColor() + getRandomColor() + getRandomColor();
      
      for (let vertex of group) {
        for (let edge of vertex.edges) {
          console.log(edge.destination.value);
          ctx.strokeStyle = newColor;
          ctx.lineWidth = edge.weight;
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        }
      }

      for (let vertex of group) {
        for (let edge of vertex.edges) {
          ctx.fillStyle = 'white';
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.arc((vertex.pos.x + edge.destination.pos.x) / 2, (vertex.pos.y + edge.destination.pos.y) / 2, vertexRadius / 1.5, 0, 2 * Math.PI);
          ctx.fill();
          ctx.stroke();
          ctx.fillStyle = 'black';
          ctx.font = "10px Arial";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(edge.weight, (vertex.pos.x + edge.destination.pos.x) / 2, (vertex.pos.y + edge.destination.pos.y) / 2);
        }
      }

      ctx.strokeStyle = 'transparent';

      for (let vertex of group) {
        ctx.fillStyle = newColor;
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = 'black';
        ctx.font = "12px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      }
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
    this.newGraph = this.newGraph.bind(this);

    this.state = {
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(graphX, graphY, boxSize, probability);
  }

  newGraph() {
    const state = {
      graph: new Graph()
    };
    state.graph.randomize(graphX, graphY, boxSize, probability);

    this.setState(state);
  }

  bfsType = () => {
    searchType = 'BFS';
    this.newGraph();
  }

  dfsType = () => {
    searchType = 'DFS';
    this.newGraph();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <br />
        <button onClick={this.bfsType}>BFS Graph</button>
        <button onClick={this.dfsType}>DFS Graph</button>
      </div>
    );
  }
}

export default App;
