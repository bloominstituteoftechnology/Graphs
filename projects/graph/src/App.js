import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 400;
const canvasHeight = 400;

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
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    console.log('hey', this.props.graphs.vertexes);
    for (let vertex of this.props.graphs.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 10, 0, 2 * Math.PI);
      ctx.fillStyle = 'green';
      ctx.fill();
      ctx.strokeStyle = 'black';
      ctx.stroke();
      
      ctx.fillStyle = 'black';
      ctx.font = '10px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseLine = 'middle';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
    
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
