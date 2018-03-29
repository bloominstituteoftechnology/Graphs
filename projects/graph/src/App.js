import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// Define the size of the random graph
const xCount = 5;
const yCount = 4;
const boxSize = 150;
const probability = 0.6;

// Figure out the canvas size
const canvasWidth = boxSize * xCount;
const canvasHeight = boxSize * yCount;
const radius = boxSize / 8;

let lastRandomIndex = -1;

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
    ctx.fillStyle = '#eee';
    ctx.textAlign = "center";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    const { vertexes } = this.props.graph;

    for (let i = 0; i < vertexes.length; i++) {

      const vertex = vertexes[i];

      for (let e = 0; e < vertex.edges.length; e++) {

        const edge = vertex.edges[e];
        edge.weight = Math.floor(Math.random() * 10);
        
        console.log(edge.weight);

        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#000';
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);

        ctx.stroke();
        
        const weightPosX = (vertex.pos.x + edge.destination.pos.x) / 2;
        const weightPosY = (vertex.pos.y + edge.destination.pos.y) / 2;

        ctx.beginPath();
        ctx.moveTo(weightPosX, weightPosY);

        ctx.arc(weightPosX, weightPosY, 10, 0, 2 * Math.PI);
        ctx.fillStyle = '#eee';
        ctx.strokeStyle =  '#eee';
        ctx.fill();

        ctx.font = 'bold 14px sans-serif';
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillStyle = '#000';
        ctx.fillText(edge.weight, weightPosX, weightPosY);


      }
    }

    for (let i = 0; i < vertexes.length; i++) {

      const vertex = vertexes[i];

      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.beginPath();

      ctx.arc(vertex.pos.x, vertex.pos.y, 25, 0, 2 * Math.PI);
      
      ctx.fillStyle = vertex.fillColor;
      ctx.strokeWidth = 5;
      ctx.strokeStyle = (vertex.fillColor !== 'white') ? '#eee' : '#000';
      ctx.fill();

      ctx.font = 'bold 18px sans-serif';
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillStyle = (vertex.fillColor !== 'white') ? 'white' : '#000';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);

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
    
    this.state.graph.randomize(xCount, yCount, boxSize, probability);

    
  }

  generateGraph = () => {

    const state = {
      graph: new Graph()
    };

    state.graph.randomize(xCount, yCount, boxSize, probability);

    this.setState(state);

  }

  doBreadthFirstSearch = () => {

    const state = {
      graph: this.state.graph
    };

    this.setState(state);

    this.state.graph.bfs(this.state.graph.vertexes[0]);

  }

  render() {
    return (
      <div className="App">
        <GraphView graph={ this.state.graph }></GraphView>
        <br/>
        <button onClick={ this.generateGraph }>Re-generate Graph</button>
        <button onClick={ this.doBreadthFirstSearch }>BFS Search Graph</button>
      </div>
    );
  }
}

export default App;
