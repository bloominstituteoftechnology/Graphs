import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000; 
const canvasHeight = window.innerHeight;
const circle = 15;

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
    this.props.graph.getConnectedComponents()
    
    // Clear it
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';


    
    // draw our dummy vertexes
    this.props.graph.vertexes.forEach((v) => {
      console.log(this.props.graph.vertexes[0])
        ctx.beginPath();
        ctx.fillStyle = v.color;
        ctx.arc(v.pos.x, v.pos.y, circle, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
        ctx.fillStyle = 'black';
        ctx.fillText(v.value, v.pos.x, v.pos.y)
      })

      this.props.graph.vertexes.forEach(v => {
        v.edges.forEach(edge => {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
          ctx.fill();
        });
      });
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