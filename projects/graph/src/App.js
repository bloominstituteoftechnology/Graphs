import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
// const canvasWidth = 
// const canvasHeight = 
const canvasWidth = window.innerHeight;
const canvasHeight = window.innerWidth;
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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    // !!! IMPLEMENT ME
    let matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()";
    
    

    let font_size = 10;
    let columns = canvasWidth/font_size; 
    let drops = [];


    for( let x = 0; x < columns; x++)
      drops[x] = 1;


    function draw() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.04)"; 
    ctx.fillRect(0, 0, canvasWidth, canvasHeight); 

    ctx.fillStyle = "#0F0"; 
    ctx.font = font_size + "px arial";


    for(let i = 0; i < drops.length; i++) {
    let text = matrix[Math.floor(Math.random()*matrix.length)]; 
    ctx.fillText(text, i*font_size, drops[i]*font_size); 


    if(drops[i]*font_size > canvasHeight && Math.random() > 0.975)
        drops[i] = 0;
    drops[i]++; 
    }
}

setInterval(draw, 35);
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
