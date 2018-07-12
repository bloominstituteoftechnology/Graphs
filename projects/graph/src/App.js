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
    this.drawVertexes(connections, ctx);
  }

  drawVertexes(connections, ctx) {
    ctx.font = '8px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    ctx.fillStyle = 'white';

    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, 10, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
      for(let e of v.edges) {
        let d = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(d.pos.x, d.pos.y);
        ctx.stroke();
      }
    })

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
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
    this.state.graph.getConnectedComponents();
  }
  
  //Make a new randomize function for a click function instead of having to refresh
  //Built a state which was a new graph then did the randomize func and set the new state to state
  poo() {
    const state ={
      graph: new Graph()
    };
    state.graph.randomize(7, 7, 60, 0.45);
    this.state.graph.getConnectedComponents();
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
