import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
const canvasHeight = 400;
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
    ctx.fillStyle = '#DCDCCC';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log('in updateCanvas', this.props);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = 'black';
    ctx.font = '16px Arial';

    this.props.graph.vertexes.forEach(debugVertex => {
    ctx.beginPath();
    ctx.arc(debugVertex.pos.x, debugVertex.pos.y, circleSize, 0, 2 * Math.PI);
    ctx.fillStyle = 'white'; // TODO: make variable
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = 'black';

    ctx.fillText(debugVertex.value, debugVertex.pos.x, debugVertex.pos.y);
    });

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
