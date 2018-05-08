import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 10;

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
    ctx.fillStyle = 'lightgrey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    //console.log('Update Canvas, vertex data: ', this.props);

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.beginPath();
        ctx.lineTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
      
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.font = "11px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
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
    this.state.graph.randomize(5, 4, 150, 0.6);
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
