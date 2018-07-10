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
    // call our dummy function
    this.props.graph.createDummyGraph();
    console.log('called createDummyGraph');

    // Clear it
    // ctx.fillStyle = 'white';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);


    //CIRCLE
  // var gradient = ctx.createRadialGradient(250, 250, 249, 250, 250, 100);
  // gradient.addColorStop(0, 'magenta');
  // gradient.addColorStop(1, 'yellow');
  // ctx.fillStyle = gradient;
  // ctx.fillRect(25, 25, 450, 450); 

//TRIANGLES
    // var gradient = ctx.createLinearGradient(25, 475, 775, 25);
    // gradient.addColorStop(0, 'orange');
    // gradient.addColorStop(1, 'magenta');
    // ctx.fillStyle = gradient;
    // // ctx.fillStyle = 'orange';
    // ctx.beginPath();
    // ctx.moveTo(25, 25);
    // ctx.lineTo(775, 25);
    // ctx.lineTo(25, 475);
    // ctx.fill();

    // var gradient = ctx.createLinearGradient(25, 475, 775, 25);
    // gradient.addColorStop(0, 'magenta');
    // gradient.addColorStop(1, 'orange');
    // ctx.fillStyle = gradient;
    // // ctx.fillStyle = 'magenta';
    // ctx.beginPath();
    // ctx.moveTo(775, 475);
    // ctx.lineTo(775, 25);
    // ctx.lineTo(25, 475);
    // ctx.closePath();
    // ctx.fill();

    // ctx.strokeStyle = 'red';
    // ctx.strokeRect(0, 0, 500, 500);

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
