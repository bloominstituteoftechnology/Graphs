import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 900;

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

    console.log('this.props.graph: ', this.props.graph);
    //call our dummy function
    this.props.graph.createDummyGraph();
    console.log('called createDummyGraph');
    
    // Clear it
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw our dummy vertex
    ctx.arc(10, 10, 10, 0, 2 * Math.PI); //deciding what to draw next
    ctx.stroke();//put your pen down and draw the stroke
    ctx.beginPath();
    ctx.arc(100, 100, 10, 0, 2 * Math.PI);
    ctx.stroke();
    console.log('called ctx.arc');

    // ctx.fillStyle = 'red'; // HAT 1
    // ctx.fillRect(200, 10, 20, 20);    

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
