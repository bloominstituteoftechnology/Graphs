import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 900;
const canvasHeight = 800;
const circleRadius = 15;

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

    console.log('this.props.graph: ', this.props.graph)

    this.props.graph.createDummyGraph();
    console.log('called createDummyGraph');
    
    // Clear it
    ctx.fillStyle = '#c0dfe8';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '14px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // draw dummy vertexes

    this.props.graph.vertexes.forEach(v => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, (Math.PI * 2));
      ctx.fill();
      ctx.stroke();

      // fill the text

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
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
