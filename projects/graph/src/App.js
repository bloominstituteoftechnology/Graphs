import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 500;

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
    ctx.fillStyle = "grey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight); // (x, y, width, height) origin -- top left
//     ctx.moveTo(0,0);
//     ctx.lineTo(200,100);
//     ctx.moveTo(200,100);
//     ctx.lineTo(130,480);
//     ctx.lineTo(320,75);
//     ctx.stroke();
//
//     ctx.beginPath();
//     ctx.arc(95,50,40,0,2*Math.PI);
//     ctx.stroke();
//
//     // Create gradient
//     var grd=ctx.createLinearGradient(300,300,150,0);
//     grd.addColorStop(0,"red");
//     grd.addColorStop(1,"white");
//
// // Fill with gradient
//     ctx.fillStyle=grd;
//     ctx.fillRect(300,100,150,80);
//
//     for(var i = 0; i < 300; i++) {
//       ctx.moveTo(2*i, 20);
//       ctx.lineTo(3*i, 250);
//       let r = i+100;
//       let g = 30*i*i;
//       let b = i * 10;
//       ctx.strokeStyle= `rgb(${r},${g},${b})`;
//       ctx.stroke();
//     }
    ctx.beginPath();
    ctx.arc(95,50,40,0,2*Math.PI);
    ctx.lineTo(200, 150);
    for (let i = 0; i < canvasWidth; i++) {
      ctx.lineTo(22 * i, 50);
      ctx.lineTo(1000 / i, 500);
      let r = Math.floor(Math.random() * 8) * i + 50;
      let g = Math.floor((Math.random() * 2)) * i;
      let b = Math.floor(Math.random() * i);
      ctx.strokeStyle = `rgb(${r}, ${g}, ${b})`;
      ctx.stroke();
    }


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
