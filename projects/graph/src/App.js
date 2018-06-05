import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
const canvasHeight = 500;

const circleSize = 15;
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
    ctx.fillStyle = '#E91E63';
    ctx.fillRect(200, 200, canvasWidth, canvasHeight);

    console.log('in updateCanvas', this.props.graph.vertexes);
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '14px Arial';
    ctx.fillStyle = 'black';

    for (let vertex of this.props.graph.vertexes) {
    ctx.beginPath();      
    ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
    ctx.fillStyle = 'red'; // can make variable
    ctx.fill();
    ctx.stroke();

    
    
    ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }

    // let debugVertex = this.props.graph.vertexes[0];  changed variable to vertex

    
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
    this.state.graph.debugCreateTestData();
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
