import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const circleRad = 15;

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
    console.log('this.props.graph', this.props.graph);
    console.log('call createDummyGraph');
    this.props.graph.randomize(5, 4, 150, 0.6);
    
    // Clear it
    ctx.font = "13px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = "gray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = "white";
      ctx.arc(v.pos.x, v.pos.y, circleRad, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();
      // put text in vertex
      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.pos.x, v.pos.y);

      if(v.edges.length > 0) {
        for(let i = 0; i < v.edges.length; i++) {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(v.edges[i].destination.pos.x, v.edges[i].destination.pos.y);
          ctx.strokeStyle = 'black';
          ctx.stroke();
        }
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

    this.state = {
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
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
