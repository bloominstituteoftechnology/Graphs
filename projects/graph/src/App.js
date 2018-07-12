import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const circleRadius = 16;

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

  getColor() {
    const r = Math.floor(Math.random() * 256),
          g = Math.floor(Math.random() * 256),
          b = Math.floor(Math.random() * 256);
          return 'rgb(' + r + ',' + g + ',' + b + ')';
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
     let canvas = this.refs.canvas;
     let ctx = canvas.getContext('2d');

     //console.log('this.props.graph: ', this.props.graph);
     // call our dummy function
    //this.props.graph.createDummyGraph();
     //console.log('called createDummyGraph');


     // Clear it 
      ctx.fillStyle = 'grey';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
      this.drawVertexes(ctx);
      this.colorVertexes(ctx);
  }

  drawVertexes(ctx) {
    ctx.font = '14px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        ctx.fillText(edge.weight, (vertex.pos.x + edge.destination.pos.x) / 2, (vertex.pos.y + edge.destination.pos.y) / 2);
      }
    }

    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // fill in the text
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });
  }

  colorVertexes(ctx) {
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        const color = this.getColor();
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
    this.buttonHandler = this.buttonHandler.bind(this);

    this.state = {
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.getConnectedComponents();
  }

  buttonHandler() {
    const state = {
      graph: new Graph()
    };
    state.graph.randomize(5, 4, 150, 0.6);
    state.graph.getConnectedComponents();
    this.setState(state);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick = {this.buttonHandler}>New Graph</button>
      </div>
    );
  }
}

export default App;
