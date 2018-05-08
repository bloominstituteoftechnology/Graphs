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

    const clock = () => {
      var now = new Date();
      ctx.save();
      ctx.clearRect(10, 10, 350, 350);
      ctx.translate(200, 200);
      // ctx.scale(0.4, 0.4);
      ctx.rotate(-Math.PI / 2);
      ctx.strokeStyle = 'black';
      ctx.fillStyle = 'white';
      ctx.lineWidth = 4;
      ctx.lineCap = 'round';
    
      // Hour marks
      ctx.save();
      for (var i = 0; i < 12; i++) {
        ctx.beginPath();
        ctx.rotate(Math.PI / 6);
        ctx.moveTo(100, 0);
        ctx.lineTo(120, 0);
        ctx.stroke();
      }
      ctx.restore();
    
      // Minute marks
      ctx.save();
      ctx.lineWidth = 5;
      for (i = 0; i < 60; i++) {
        if (i % 5 !== 0) {
          ctx.beginPath();
          ctx.moveTo(117, 0);
          ctx.lineTo(120, 0);
          ctx.stroke();
        }
        ctx.rotate(Math.PI / 30);
      }
      ctx.restore();
     
      var sec = now.getSeconds();
      var min = now.getMinutes();
      var hr  = now.getHours();
      hr = hr >= 12 ? hr - 12 : hr;
    
      ctx.fillStyle = 'black';
    
      // write Hours
      ctx.save();
      ctx.rotate(hr * (Math.PI / 6) + (Math.PI / 360) * min + (Math.PI / 21600) *sec);
      ctx.lineWidth = 14;
      ctx.beginPath();
      ctx.moveTo(-20, 0);
      ctx.lineTo(80, 0);
      ctx.stroke();
      ctx.restore();
    
      // write Minutes
      ctx.save();
      ctx.rotate((Math.PI / 30) * min + (Math.PI / 1800) * sec);
      ctx.lineWidth = 10;
      ctx.beginPath();
      ctx.moveTo(-28, 0);
      ctx.lineTo(112, 0);
      ctx.stroke();
      ctx.restore();
     
      // Write seconds
      ctx.save();
      ctx.rotate(sec * Math.PI / 30);
      ctx.strokeStyle = '#D40000';
      ctx.fillStyle = '#D40000';
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.moveTo(-30, 0);
      ctx.lineTo(83, 0);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(0, 0, 10, 0, Math.PI * 2, true);
      ctx.fill();
      ctx.beginPath();
      ctx.arc(95, 0, 10, 0, Math.PI * 2, true);
      ctx.stroke();
      ctx.fillStyle = 'rgba(0, 0, 0, 0)';
      ctx.arc(0, 0, 3, 0, Math.PI * 2, true);
      ctx.fill();
      ctx.restore();
    
      ctx.beginPath();
      ctx.lineWidth = 14;
      ctx.strokeStyle = '#325FA2';
      ctx.arc(0, 0, 142, 0, Math.PI * 2, true);
      ctx.stroke();
    
      ctx.restore();
    
      // window.requestAnimationFrame(clock);
    }
    
    // window.requestAnimationFrame(clock);
    setInterval(clock, 1000);

    // for (var i = 0; i < 400; i++) {
    //   ctx.lineWidth = 0.2;
    //   ctx.beginPath();
    //   ctx.moveTo(i * 10, 0);
    //   ctx.lineTo(i * 10, 400);
    //   ctx.stroke();

    //   ctx.beginPath();
    //   ctx.moveTo(0, i * 10);
    //   ctx.lineTo(400, i * 10);
    //   ctx.stroke();
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
