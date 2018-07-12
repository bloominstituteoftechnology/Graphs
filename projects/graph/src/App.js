import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;

const canvasHeight = 500; 
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
    
    ctx.fillStyle = 'beige';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    const connections = this.props.graph.getConnectedComponents();
    connections.forEach((component) => {
      this.drawVertexes(ctx, component, this.generateRandomColor());
    })
    // this.drawVertexes(ctx, this.generateRandomColor());
  }

  drawVertexes(ctx, vertexes, color) {
    ctx.font = '8px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    
    ctx.strokeStyle = color;
    for(let v of vertexes) {
      for(let e of v.edges) {
        let d = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(d.pos.x, d.pos.y);
        ctx.stroke();
      }
    for(let v of vertexes) {
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.arc(v.pos.x, v.pos.y, 10, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    }
    }
    
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  }
  generateRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i<6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
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
    //Bound the function to the app
    this.poo = this.poo.bind(this);

    this.state = {
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(7, 7, 60, 0.6);
  }
  
  //Make a new randomize function for a click function instead of having to refresh
  //Built a state which was a new graph then did the randomize func and set the new state to state
  poo() {
    const state ={
      graph: new Graph()
    };
    state.graph.randomize(7, 7, 60, 0.45);
    // this.state.graph.getConnectedComponents();
    this.setState(state);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.poo}>New Graph</button>
      </div>
    );
  }
}

export default App;
