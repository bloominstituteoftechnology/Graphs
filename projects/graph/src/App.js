import React, { Component } from 'react';
import { Graph, Edge} from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;

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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // graph passed from the App class through this.props
    const { vertexes } = this.props.graph;
    
    for (let i = 0; i < vertexes.length; i++) {
      // vertexes have position properties of x and y
      const x = vertexes[i].pos.x;
      const y = vertexes[i].pos.y;
      //drawing the edges
      for (let j = 0; j < vertexes[i].edges.length; j++ ) {
        // destination has properties x and y as well 
        const x2 = vertexes[i].edges[j].destination.pos.x;
        const y2 = vertexes[i].edges[j].destination.pos.y;
  
        // use begin path inside for loop rather than outside of it.
        ctx.beginPath();
        // initial point 
        ctx.moveTo(x, y);
        // second point 
        ctx.lineTo(x2, y2);
        // draw the line itself 
        ctx.stroke();
      }
    }
    // drawing the nodes
    for (let e of vertexes) {
      // default color has been set to green
      ctx.fillStyle = e.color;
      ctx.beginPath();
      ctx.arc(e.pos.x, e.pos.y, 10, 0, 2 * Math.PI);
      ctx.fill();
    }
    // drawing the text
    for (let i of vertexes) {
      ctx.font = '20px serif';
      ctx.fillText(i.value, i.pos.x + 15, i.pos.y);
    }
    // creating new graph class instance to access breadth first search algorithm function
    const graphClass = new Graph();
    graphClass.bfs(vertexes, ctx);
    // compute connected components
    graphClass.getConnectedComponents(vertexes, ctx);

    //update node after component edges have been drawn 
    for (let e of vertexes) {
      ctx.fillStyle = e.color;
      ctx.beginPath();
      ctx.arc(e.pos.x, e.pos.y, 10, 0, 2 * Math.PI);
      ctx.fill();
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
    this.onRefresh = this.onRefresh.bind(this);
    // use the graph randomize() method
   this.state.graph.randomize(5, 4, 150);
  }
  onRefresh() {
    window.location = 'http://localhost:3000/';  
  }

  render() {
    return (
      <div className="App">
        <button className='buttonRefresh' onClick={this.onRefresh}>Refresh</button>
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
