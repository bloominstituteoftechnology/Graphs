import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;

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
    
    function getRandomInt(max) {
      return Math.floor(Math.random() * Math.floor(max));
    }
    function getNeg() {
      return getRandomInt(10) % 2 === 0 ? 1 : -1;
    }
    function makeCirc(x,y,size) {
      ctx.strokeStyle = 'black';    
      ctx.beginPath();    
      // for (let i = 0; i < 360;) {
      // ctx.moveTo(canvasWidth/2, canvasHeight/2);      
      ctx.arc(x, y, size, 0, 2*Math.PI);
      var grd = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      // light blue
      grd.addColorStop(0, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);   
      // dark blue
      grd.addColorStop(1, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);
      ctx.fillStyle = grd;
      ctx.fill();
        // i += 360/60
      // }
      ctx.stroke();
    }
    function makeTri(x, y, distance) {
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
      ctx.strokeStyle = 'black';
      ctx.moveTo(point1.x, point1.y);
      ctx.lineTo(point2.x, point2.y);
      ctx.lineTo(point3.x, point3.y);
      ctx.lineTo(point1.x, point1.y);
      var grd = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      // light blue
      grd.addColorStop(0, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);   
      // dark blue
      grd.addColorStop(1, `rgba(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)},.75)`);
      ctx.fillStyle = grd;
      ctx.fill();
      ctx.stroke();
    }

    
    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fillStyle = 'white';
    ctx.fillRect(2, 2, canvasWidth-4, canvasHeight-4);

    // !!! IMPLEMENT ME
    // ctx.fillStyle = 'blue';
    ctx.strokeStyle = 'blue';
    ctx.beginPath();
    for(let i = 0; i < 500; i++) {
      ctx.moveTo(canvasWidth/2, canvasHeight/2);
      ctx.lineTo(Math.sin(i*4*Math.PI), 30*i);
    }
    ctx.stroke();

    ctx.strokeStyle = 'orange';
    ctx.beginPath();
    for(let i = 0; i < 500; i++) {
      ctx.moveTo(canvasWidth/2, canvasHeight/2);
      ctx.lineTo(-Math.sin(i*4*Math.PI), -30*i);
    }
    ctx.stroke();

    ctx.strokeStyle = 'purple';
    ctx.beginPath();
    for(let i = 0; i < 500; i++) {
      ctx.moveTo(canvasWidth/2, canvasHeight/2);
      ctx.lineTo(800+Math.sin(i*4*Math.PI), -30*i);
    }
    ctx.stroke();

    
    ctx.strokeStyle = 'red';
    ctx.beginPath();
    for(let i = 0; i < 500; i++) {
      ctx.moveTo(canvasWidth/2, canvasHeight/2);
      ctx.lineTo(800+Math.cos(i*4*Math.PI), 25*i);
    }
    ctx.stroke();

    for(let i = 0; i < getRandomInt(600); i++) {
      makeCirc(getRandomInt(800),getRandomInt(750),getRandomInt(100));
    }
    for(let i = 0; i < getRandomInt(1000); i++) {
      makeTri(getRandomInt(780),getRandomInt(800),getRandomInt(350));
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
