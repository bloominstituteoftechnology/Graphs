import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = window.innerWidth;
const canvasHeight = (window.innerWidth * .80 | 0);

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
    let canvas = this.refs.canvas;
    let c = canvas.getContext('2d');
    
    // Clear it
    c.fillStyle = '#000000';
    c.fillRect(0, 0, canvasWidth, canvasHeight);
    let i = 0;
    
    // console.log(c.strokeStyle);
    
    
    let stroke = (() => {
      do {
        c.beginPath();
        c.moveTo(i * 2, i / 2);
        c.strokeStyle = this.randomRGBA(i, i, i, 0.1);
        c.lineTo(i < canvasWidth ? canvasWidth / 2: 0, i < canvasHeight ? canvasHeight / 2 : i / 2);//, (Math.random() * canvasHeight) + 1)|0;
        c.stroke();
        i += 1;
      } while (i <=  127);
      })();

      stroke;
      stroke;



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
