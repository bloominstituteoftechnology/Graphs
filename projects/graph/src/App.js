import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000; 
const canvasHeight = window.innerHeight;
const circle = 15;
let temp = 0;

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

    // window.location.reload
    
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // call our dummy function
    // this.props.graph.createDummyGraph();

    this.props.graph.randomize(5, 4, 150, 0.6);
    
    // Clear it
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';


    
    // draw our dummy vertexes
    this.props.graph.vertexes.forEach((v, index) => {
        ctx.beginPath();
        ctx.fillStyle = 'white';
        ctx.arc(v.pos.x, v.pos.y, circle, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
        ctx.fillStyle = 'black';
        ctx.fillText(v.value, v.pos.x, v.pos.y);

      })


    // ctx.arc(10, 10, 10, 0, 2 * Math.PI);  // deciding what we're going to draw next
    // ctx.stroke(); // put your pen down and draw the stroke
    // ctx.beginPath();
    // ctx.arc(100, 100, 10, 0, 2 * Math.PI);
    // ctx.stroke();
    // console.log('called ctx.arc');
    
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  }


  newGraph() {
    window.location.reload()
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
    <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
    <button onClick={() => {
      this.newGraph()
    }}>New Graph</button>
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    const g = new Graph();
    g.randomize(5, 4, 150, 0.6);
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