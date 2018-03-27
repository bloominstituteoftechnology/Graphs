import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = window.innerWidth;
const canvasHeight = window.innerHeight;

/**
 * GraphView
 */
class GraphView extends Component {
  constructor(props) {
    super();
    // let vertex = new Graph();

  }
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
  
  randomHEX() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
  }

  randomRGB() {
    return `rgb(${((Math.random() * 255) + 1) | 0}, ${((Math.random() * 255) + 1) | 0}, ${((Math.random() * 255) + 1) | 0}`;
  }

  randomRGBA(r, g, b, a) {
    return `rgba(${!!r ? r : ((Math.random() * 255) + 1) | 0}, ${!!g ? g : ((Math.random() * 255) + 1) | 0}, ${!!b ? b : ((Math.random() * 255) + 1) | 0}, ${!!a ? a : Math.random().toFixed(2) }`;
  }


  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = document.getElementById('LS');//this.ref.canvas;
    let c = canvas.getContext('2d');
    
    // Clear it
    c.fillStyle = 'blue';
    c.fillRect(0, 0, canvasWidth, canvasHeight);

    // const root = this.props.graph.vertexes;
    // console.log(root);
    let x = 0;
    let y = 0;
    let j = 0;
    for (let j = 0; j < 10; j++) {
      
      x += j;//root[j].pos.x;
      y += j;//root[j].pos.y;
      // c.moveTo(0, 0);
      c.beginPath();
      c.arc(x, y, 20, 0, Math.PI * 2);
      c.closePath();
      c.stroke();
      c.fillStyle = this.randomRGBA(0,0,0,0.6);
      c.fill();
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
    return <canvas id="LS" ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}


/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = { graph: new Graph() };
  }

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    componentDidMount() {
      this.state.graph = this.state.graph.randomize(2, 2);
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
