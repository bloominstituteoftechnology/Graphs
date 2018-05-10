import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800
const canvasHeight = 800

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}
function getNeg() {
  return getRandomInt(10) % 2 === 0 ? 1 : -1;
}
function getDistance(x,y) {
  return Math.sqrt(Math.pow(400-x,2) + Math.pow(400-y,2));
}

function makeCirc(xgiven,y,size,ctx) {
  this.x = xgiven;
  this.y = y;
  this.size = size;
  ctx.strokeStyle = 'black';    
  ctx.beginPath();    
  // for (let i = 0; i < 360;) {
  // ctx.moveTo(canvasWidth/2, canvasHeight/2);      
  ctx.arc(xgiven, y, size, 0, 2*Math.PI);
  var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
  grd.addColorStop(0, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);   
  grd.addColorStop(1, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);
  ctx.fillStyle = grd;
  ctx.fill();
    // i += 360/60
  // }
  ctx.stroke();
}
function makeTri(x, y, distance, ctx) {
  const point1 = {
    x: x,
    y: y,
  };
  const point2 = {
    x: point1.x + getRandomInt(distance) * getNeg(),
    y: point1.y + getRandomInt(distance) * getNeg(),
  };
  const point3 = {
    x: point2.x + getRandomInt(distance) * getNeg(),
    y: point2.y + getRandomInt(distance) * getNeg(),
  };

  this.point1 = point1;
  this.point2 = point2;
  this.point3 = point3;
}

function drawTri(obj, ctx) {
  ctx.strokeStyle = 'black';
  ctx.moveTo(obj.point1.x, obj.point1.y);
  ctx.lineTo(obj.point2.x, obj.point2.y);
  ctx.lineTo(obj.point3.x, obj.point3.y);
  ctx.lineTo(obj.point1.x, obj.point1.y);
  // var grd = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  // // light blue
  // grd.addColorStop(0, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);   
  // // dark blue
  // grd.addColorStop(1, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);
  // ctx.fillStyle = grd;
  // ctx.fill();
  ctx.stroke();
}

function drawBall(ball, ctx) {
  ctx.strokeStyle = 'black';    
  ctx.beginPath();    
  // for (let i = 0; i < 360;) {
  // ctx.moveTo(canvasWidth/2, canvasHeight/2);      
  ctx.arc(ball.x, ball.y, ball.size, 0, 2*Math.PI);
  var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
  grd.addColorStop(0, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);   
  grd.addColorStop(1, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);
  ctx.fillStyle = grd;
  ctx.fill();
    // i += 360/60
  // }
  ctx.stroke();
}

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

    let balls = [];
    let triangles = [];
    
    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fillStyle = 'white';
    ctx.fillRect(2, 2, canvasWidth-4, canvasHeight-4);

    // !!! IMPLEMENT ME
    ctx.moveTo(400,400);

    ctx.strokeStyle = 'black';
    ctx.beginPath();
    let angle;
    for (let i=0; i< 100000; i++) {
      if (i <= 300) {
        angle = 2 * i;
      } else {
        angle = .6 * i;        
      }
      let x= 400 +(1+angle)*Math.cos(angle);
      let y= 400 +(1+angle)*Math.sin(angle);
      getNeg() === -1 ? balls[balls.length] = new makeCirc(x,y,getRandomInt(20), ctx) : ( getDistance(x,y) > 200 ? triangles[triangles.length] = new makeTri(x,y, getRandomInt(50), ctx) : balls[balls.length] = new makeCirc(x,y,getRandomInt(20), ctx) );
    }
    ctx.stroke();
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
