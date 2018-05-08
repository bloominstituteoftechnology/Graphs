import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 400;
const canvasHeight = 400;

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
    ctx.fillStyle = 'red';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.clearRect(0 + 1, 0 + 1, canvasWidth - 2, canvasHeight - 2);
    ctx.strokeRect(0 + 2, 0 + 2, canvasWidth - 4, canvasHeight - 4);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    for (var i = 0; i < 400; i++) {
      ctx.beginPath();
      ctx.moveTo(i * 10, 0);
      ctx.lineTo(i * 10, 400);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(0, i * 10);
      ctx.lineTo(400, i * 10);
      ctx.stroke();
    }

    // let radius = canvas.height / 2;
    // ctx.translate(radius, radius);
    // radius = radius * 0.90;
    // setInterval(drawClock, 1000);
    
    // function drawClock(ctx, radius) {
    //   let now = new Date();
    //   let hour = now.getHours();
    //   let minute = now.getMinutes();
    //   let second = now.getSeconds();

    //   hour=hour%12;
    //   hour=(hour*Math.PI/6)+(minute*Math.PI/(6*60))+(second*Math.PI/(360*60));

    //   minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
    //   second=(second*Math.PI/30);
    //   console.log(hour, minute, second);
    // }

    // for (let i = 0; i < 3; i++) {
    //   const max = 320;
    //   const min = 80;
    //   const x = Math.floor(Math.random() * (max - min + 1)) + min;
    //   const y = Math.floor(Math.random() * (max - min + 1)) + min;
    //   ctx.beginPath();
    //   ctx.arc(x, y, 40, 0, 2*Math.PI);
    //   ctx.stroke();
    // }

    // for (let i = 0; i < 3; i++) {
    //   ctx.globalAlpha=0.2;
    //   const max = 320;
    //   const min = 80;
    //   const x = Math.floor(Math.random() * (max - min + 1)) + min;
    //   const y = Math.floor(Math.random() * (max - min + 1)) + min;
    //   // const gradient=ctx.createLinearGradient(0,0,0,170);
    //   // gradient.addColorStop(0,"black");
    //   // gradient.addColorStop(1,"white");
    //   // ctx.fillStyle = gradient;
    //   ctx.fillStyle = 'red';
    //   ctx.fillRect(x, y, 80, 80);
    // }

    // for (let i = 0; i < 2; i++) {
    //   const x = Math.floor(Math.random() * 400);
    //   const y = Math.floor(Math.random() * 400);
    //   ctx.moveTo(200, 200);
    //   ctx.lineTo(x, y);

    //   ctx.lineWidth = 10;
    //   ctx.strokeStyle = '#666666';

    //   ctx.stroke();
    // }

      // const max = 320;
      // const min = 80;
      // const x = Math.floor(Math.random() * (max - min + 1)) + min;
      // const y = Math.floor(Math.random() * (max - min + 1)) + min;
      // // the triangle
      // ctx.beginPath();
      // ctx.moveTo(x, y);
      // ctx.lineTo(100, 300);
      // ctx.lineTo(300, 300);
      // ctx.closePath();
      
      // // the outline
      // ctx.lineWidth = 5;
      // ctx.strokeStyle = '#666666';
      // ctx.stroke();
      
      // // the fill color
      // ctx.fillStyle = "#FFCC00";
      // ctx.fill();

    // for (let i = 0; i < 2; i++) {
    //   const max = 320;
    //   const min = 80;
    //   const x = Math.floor(Math.random() * (max - min + 1)) + min;
    //   const y = Math.floor(Math.random() * (max - min + 1)) + min;
    //   // the rectangle
    //   ctx.rect(x,y,150,100);
    //   ctx.stroke();
      
    //   // the outline
    //   ctx.lineWidth = 5;
    //   ctx.strokeStyle = '#666666';
    //   ctx.stroke();
      
    //   // the fill color
    //   ctx.fillStyle = "#FFCC00";
    //   ctx.fill();
    // }

  }
  
  /**
   * Render
   */
  render() {
    // const borderStyles = {
    //     border: '10px solid gray',
    // };
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
