import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";
import { O_NOCTTY } from "constants";

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const circleRadius =15;

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
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext("2d");
console.log(this.props.graph)
this.props.graph.createDummyGraph();
    // Clear it
    ctx.fillStyle = "pink";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
// draw dummy vertex

ctx.font = '13px Arial';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';

this.props.graph.vertexes.forEach(v =>{
  console.log(v)
    v.edges.forEach(e=>{
      ctx.beginPath();
      ctx.moveTo(v.pos.x,v.pos.y);
      ctx.lineTo(e.destination.pos.x, e.destination.pos.y)
      ctx.stroke();
    })
  })

this.props.graph.vertexes.forEach(v =>{


  ctx.beginPath();
  ctx.fillStyle = 'white';
  ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();

  // fill in the text
  ctx.fillStyle = 'black';
  ctx.fillText(v.value, v.pos.x, v.pos.y);

});

// ctx.beginPath();
// ctx.lineWidth = 1;
// ctx.arc(20,20,10,0,2* Math.PI);

// ctx.stroke();

// ctx.beginPath();
// ctx.lineWidth = 1;
// ctx.arc(200,400,10,0,2* Math.PI);

// ctx.stroke();

    // my cat
//  ctx.strokeStyle = "black";
//     ctx.strokeRect(35, 70, 450, 330);

//     //eyes one
//     ctx.beginPath();
//     ctx.moveTo(50,200);
//     ctx.bezierCurveTo(100, 60, 190,130, 200, 200);
//     ctx.stroke();
    
//     ctx.beginPath();
//     ctx.moveTo(50,200);
//     ctx.bezierCurveTo(100, 300, 210,220, 200, 200);
//     ctx.stroke();
//     // eye 2
//     ctx.beginPath();
//     ctx.moveTo(320,200);
//     ctx.bezierCurveTo(380,60, 450,130, 470, 200);
//     ctx.stroke();
    
//     ctx.beginPath();
//     ctx.moveTo(320,200);
//     ctx.bezierCurveTo(410, 300, 450,220, 470, 200);
//     ctx.stroke();
// // something else
//     ctx.fillStyle = "#EAD299";
//     ctx.fillRect(210, 110, 100, 100, canvasWidth, canvasHeight);

//     ctx.fillStyle = "#EAD299";
//     ctx.fillRect(210, 10, 100, 100, canvasWidth, canvasHeight);
  
//     ctx.beginPath();

//     ctx.moveTo(120, 300);
//     ctx.lineWidth = 1;
//     ctx.lineTo(400, 300);
//     ctx.stroke();
//     //lip lower
//     ctx.beginPath();
//     ctx.moveTo(300, 320);
//     ctx.lineWidth = 3;
//     ctx.lineTo(220, 320);
//     ctx.stroke();
//     //tooth one
//     ctx.beginPath();
//     ctx.moveTo(150, 320);
//     ctx.lineWidth = 3;
//     ctx.lineTo(140, 300);
//     ctx.stroke();
//     ctx.beginPath();
//     ctx.moveTo(150, 320);
//     ctx.lineWidth = 2;
//     ctx.lineTo(160, 300);
//     ctx.stroke();
//     //tooth two
//     ctx.beginPath();
//     ctx.moveTo(350, 320);
//     ctx.lineWidth = 2;
//     ctx.lineTo(340, 300);
//     ctx.stroke();
//     ctx.beginPath();
//     ctx.moveTo(350, 320);
//     ctx.lineWidth = 4;
//     ctx.lineTo(360, 300);
//     ctx.stroke();
//     // plate lines\
//     ctx.beginPath();
//     ctx.moveTo(210, 90);
//     ctx.lineWidth = 1;
//     ctx.lineTo(310, 90);
//     ctx.stroke();
//     ctx.beginPath();
//     ctx.moveTo(310, 50);
//     ctx.lineWidth = 1;
//     ctx.lineTo(210, 50);
//     ctx.stroke();
//     ctx.beginPath();
//     ctx.moveTo(310, 130);
//     ctx.lineWidth = 1;
//     ctx.lineTo(210, 130);
//     ctx.stroke();
//     ctx.beginPath();
//     ctx.moveTo(310, 170);
//     ctx.lineWidth = 1;
//     ctx.lineTo(210, 170);
//     ctx.stroke();
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
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
    this.state.graph.randomize(5, 4, 150, 0.6)
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
