import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 1000;

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
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components

    // draw edges
    // Edge 1 C
    ctx.moveTo(0.5*canvasWidth,0.25*canvasHeight);
    ctx.lineTo(0.5*canvasWidth,0.25*canvasHeight+100);

    // Edge 2
    ctx.moveTo(0.5*canvasWidth,0.25*canvasHeight+100);
    ctx.lineTo(0.5*canvasWidth-150,0.25*canvasHeight+200);

    // Edge 3
    ctx.moveTo(0.5*canvasWidth,0.25*canvasHeight+100);
    ctx.lineTo(0.5*canvasWidth+150,0.25*canvasHeight+200);

    // Edge 4
    ctx.moveTo(0.5*canvasWidth-150,0.25*canvasHeight+200);
    ctx.lineTo(0.5*canvasWidth-225,0.25*canvasHeight+300);

    // Edge 5
    ctx.moveTo(0.5*canvasWidth-150,0.25*canvasHeight+200);
    ctx.lineTo(0.5*canvasWidth-75,0.25*canvasHeight+300);

    // Edge 6
    ctx.moveTo(0.5*canvasWidth+150,0.25*canvasHeight+200);
    ctx.lineTo(0.5*canvasWidth+75,0.25*canvasHeight+300);

    // Edge 7
    ctx.moveTo(0.5*canvasWidth+150,0.25*canvasHeight+200);
    ctx.lineTo(0.5*canvasWidth+225,0.25*canvasHeight+300);

    // Edge 08
    ctx.moveTo(0.5*canvasWidth-225,0.25*canvasHeight+300);
    ctx.lineTo(0.5*canvasWidth-300,0.25*canvasHeight+400);

    // Edge 09
    ctx.moveTo(0.5*canvasWidth-225,0.25*canvasHeight+300);
    ctx.lineTo(0.5*canvasWidth-150,0.25*canvasHeight+400);

    // Edge 10
    ctx.moveTo(0.5*canvasWidth+75,0.25*canvasHeight+300);
    ctx.lineTo(0.5*canvasWidth+0,0.25*canvasHeight+400); 

    // Edge 11
    ctx.moveTo(0.5*canvasWidth+75,0.25*canvasHeight+300);
    ctx.lineTo(0.5*canvasWidth+150,0.25*canvasHeight+400); 

    ctx.stroke();


    // draw verts
    // Vert 01
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth,0.25*canvasHeight,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 02
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth,0.25*canvasHeight+100,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 03
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth-150,0.25*canvasHeight+200,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 04
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth+150,0.25*canvasHeight+200,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 05
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth-225,0.25*canvasHeight+300,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 06
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth+75,0.25*canvasHeight+300,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 07
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth-75,0.25*canvasHeight+300,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 08
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth+225,0.25*canvasHeight+300,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 09
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth-300,0.25*canvasHeight+400,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Veret 10
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth-150,0.25*canvasHeight+400,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 11
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth,0.25*canvasHeight+400,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // Vert 12
    ctx.beginPath();
    ctx.arc(0.5*canvasWidth+150,0.25*canvasHeight+400,30,0*Math.PI,2*Math.PI);
    ctx.fill();
    ctx.stroke();

    // draw vert values (labels)
    ctx.fillStyle = "black";
    ctx.font = "30px Arial";
    ctx.textAlign = "center";
    ctx.fillText("1", 0.5*canvasWidth,0.25*canvasHeight+10);
    
    ctx.fillText("2", 0.5*canvasWidth,0.25*canvasHeight+10+100);

    ctx.fillText("3", 0.5*canvasWidth-150,0.25*canvasHeight+200+10);

    ctx.fillText("4", 0.5*canvasWidth+150,0.25*canvasHeight+200+10);

    ctx.fillText("5", 0.5*canvasWidth-225,0.25*canvasHeight+300+10);

    ctx.fillText("6", 0.5*canvasWidth-75,0.25*canvasHeight+300+10);

    ctx.fillText("7", 0.5*canvasWidth+75,0.25*canvasHeight+300+10);

    ctx.fillText("8", 0.5*canvasWidth+225,0.25*canvasHeight+300+10);

    ctx.fillText("9", 0.5*canvasWidth-300,0.25*canvasHeight+400+10);

    ctx.fillText("10", 0.5*canvasWidth-150,0.25*canvasHeight+400+10);

    ctx.fillText("11", 0.5*canvasWidth,0.25*canvasHeight+400+10);

    ctx.fillText("12", 0.5*canvasWidth+150,0.25*canvasHeight+400+10);
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
