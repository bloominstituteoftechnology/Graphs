import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 600;
const canvasHeight = 600;

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
		var canvasGradient=ctx.createLinearGradient(0,0,200,200);
		canvasGradient.addColorStop(0,"yellow");
		canvasGradient.addColorStop(1,"skyblue");
    ctx.fillStyle = canvasGradient;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

		const drawLines = (n, cap, movex, movey, color) => {
			while (n < cap) {
				for (let i = 1; i < 100; i++) {
					ctx.beginPath(); 
					ctx.moveTo(movex, movey);
					ctx.strokeStyle = color;
					ctx.lineTo(canvasWidth/2 + Math.pow(i, 2), canvasHeight/2 * n);
					ctx.stroke();
				}
				n++;
			}
		}
		drawLines(-7, 3, 0, 0, "lemonchiffon");
		drawLines(3, 7, 0, 0, "lemonchiffon");
		// sun	
		ctx.beginPath();
		ctx.moveTo(0,0);
		ctx.arc(0,0,150,0,2*Math.PI);
		ctx.fillStyle = "yellow";
		ctx.fill();
		ctx.strokeStyle="white";
		ctx.stroke();
   // !!! IMPLEMENT ME
		// cloud circle
		ctx.beginPath();
		ctx.moveTo(550,100);
		ctx.arc(450,50,100,0,2*Math.PI);
		ctx.fillStyle = "white";
		ctx.fill();
		ctx.strokeStyle="white";
		ctx.stroke();
		// cloud circle
		ctx.beginPath();
		ctx.moveTo(600,100);
		ctx.arc(525,50,75,0,2*Math.PI);
		ctx.fillStyle = "white";
		ctx.fill();
		ctx.strokeStyle="white";
		ctx.stroke();
		// cloud circle
		ctx.beginPath();
		ctx.moveTo(500,125);
		ctx.arc(350,67,100,0,2*Math.PI);
		ctx.fillStyle = "white";
		ctx.fill();
		ctx.strokeStyle="white";
		ctx.stroke();
		// hill circle
		ctx.beginPath();
		ctx.moveTo(300,1200);
		ctx.arc(350,1100,600,0,2*Math.PI);
		ctx.fillStyle = "forestgreen";
		ctx.fill();
		ctx.strokeStyle="black";
		ctx.stroke();
		// hill circle
		ctx.beginPath();
		ctx.moveTo(0,1200);
		ctx.arc(50,1100,600,0,2*Math.PI);
		ctx.fillStyle = "forestgreen";
		ctx.fill();
		ctx.strokeStyle="black";
		ctx.stroke();
		// house square
		ctx.beginPath();
		ctx.moveTo(0,600);
		ctx.fillStyle="tan";
		ctx.fillRect(0, 448, 230, 115);
		ctx.moveTo(0,448);
		ctx.lineTo(230, 448);
		ctx.lineTo(230, 563);
		ctx.lineTo(0, 563);
		ctx.strokeStyle="black";
		ctx.stroke();
		// roof
		ctx.beginPath();
		ctx.moveTo(-20, 458);
		ctx.lineTo(113,348);
		ctx.lineTo(250, 458);
		ctx.fillStyle="darkred";
		ctx.fill();
		// door
		ctx.beginPath();
		ctx.moveTo(0, 600);
		ctx.fillStyle="darkred";
		ctx.fillRect(100,463, 50, 100);
		ctx.moveTo(100,563);
		ctx.lineTo(100,463);
		ctx.lineTo(150,463);
		ctx.lineTo(150,563);
		ctx.strokeStyle="black";
		ctx.stroke();
		// doorknob
		ctx.beginPath();
		ctx.moveTo(145, 513);
		ctx.arc(140,513,5,0,2*Math.PI);
		ctx.fillStyle="black";
		ctx.fill();
    // compctx.arcute connected components
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
