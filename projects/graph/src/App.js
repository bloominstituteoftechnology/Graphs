import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1400
const canvasHeight = 800

const circleRadius = 15


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
    //call dummy funciton
    this.props.graph.createDummyGraph(); 
    console.log('called createDummyGraph'); 

    //clear it
    ctx.fillStyle= 'grey'; 
    ctx.fillRect(0, 0, canvasWidth, canvasHeight); 
    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    
    // draw our dummy vertexes
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      // fill in the text
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
});

   
   
  }

  // !!! IMPLEMENT ME
  // compute connected components
  // draw edges
  // draw verts
  // draw vert values (labels)


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
        <GraphView graph={this.state.graph}>Canvas API</GraphView>
      </div>
    );
  }
}

export default App;
