import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 1400;
const canvasHeight = 1400;

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
    //this.updateCanvas();
  }


  /*
   *  Fill Text
   */
  fillText(text, x = 50, y = 100, color = 'black', font = '20px serif') {
    this.ctx.font = font ? font : this.font;
    this.ctx.fillStyle = color ? color : this.color;
    this.ctx.fillText(text, x, y);
    this.ctx.fill();
  }
  
  clearScreen() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }
  
  getRandomHexColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
  }
  
  getRandomeRGBAColor() {
   /* TODO : IMPLEMENT ME*/ 
  }
  
  drawCircle(location, size, offsetX = 0, offsetY = 0) {
    this.ctx.moveTo(location.x + offsetX , location.y + offsetY);
    this.ctx.beginPath();
    this.ctx.fillStyle = this.getRandomHexColor();
    this.ctx.strokeStyle = this.getRandomHexColor();
    this.ctx.arc(location.x, location.y, size, 0, Math.PI * 2, true); // Outer circle
    this.ctx.fill();
    this.ctx.stroke();
  }
  
  
  /**
   * Render the canvas
   */
  updateCanvas() {
    this.canvas = this.refs.canvas;
    /** @type {CanvasRenderingContext2D} */
    this.ctx = this.canvas.getContext('2d');
    this.ctx.strokeStyle = 'black';
    this.ctx.fillStyle = 'lightgrey';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    this.clearScreen();
    this.props.graph.randomize(this.canvas.width, this.canvas.height, 50);
    
    for(let vert of this.props.graph.vertexes){
      /*
      if(vert.edges[0] !== undefined && vert.edges[0].destination !== undefined){
        this.ctx.moveTo(vert.pos.x, vert.pos.y);
        this.ctx.lineTo(vert.edges[0].destination.pos.x, vert.edges[0].destination.pos.y);
        this.ctx.strokeStyle = this.getRandomHexColor(); 
        this.ctx.stroke();
      }
      
      */
     // draw verts
      this.drawCircle(vert.pos, 10, 10);      
      // draw vert values (labels)
      this.ctx.moveTo(vert.pos.x, vert.pos.y);    
      this.ctx.beginPath();
      this.ctx.font = "10px Abel";
      this.ctx.strokeStyle = 'black';    
      this.ctx.textBaseline = "middle"
      this.ctx.strokeText(vert.value, vert.pos.x -3, vert.pos.y);
      this.ctx.stroke();      
    };
    
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
