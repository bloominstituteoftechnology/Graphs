import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
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
    // window.requestAnimationFrame(this.updateCanvas);
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
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // ------------- Retro C64 looking trippy thing ---------------
    // for(let x = 0; x < canvasWidth; x += 5) {
    //   for(let y = 0; y < canvasHeight; y += 5) {
    //       const r = (Math.sqrt(y * (x/20))) % 255;
    //       const g = (Math.cos(x*y + Math.sin(y)) * 100) % 255;
    //       const b = (r*(y/(Math.PI*r)) + g) % 255;
    //       ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    //       ctx.fillRect(x, y, 5, 5);
    //   }
    // }
    // -------------------------------------------

    // ------------- Happy Accident ---------------
    // for(let x = 0; x < canvasWidth; x++) {
    //   for(let y = 0; y < canvasHeight; y++) {
    //       const r = (Math.sqrt(y * (x/20))) % 255;
    //       const g = (Math.cos(x*y + Math.sin(y)) * 100) % 255;
    //       const b = (r*(y/(Math.PI*r)) + g) % 255;
    //       ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    //       ctx.fillRect(x, y, 1, 1);
    //   }
    // }
    // -------------------------------------------

    // --------------- FIB Spiral ----------------------

    for(let y = 0; y < canvasHeight; y++) {
      for(let x = 0; x < canvasWidth; x++) {
        const py = (y - canvasHeight/2) / canvasHeight ;
        const px = (x - canvasWidth/2) / canvasHeight ;
        const lp = Math.sqrt(Math.pow(py, 2) + Math.pow(px, 2));
        const spiralTension = 0.618;
        const theta = Math.atan(px/py);
        const spiral = ((Math.log(lp)/spiralTension) + theta);
        const r = ( Math.sin(10 * spiral) * 150 ) * Math.atan(x/y) % 255;
        const g = ( Math.sin(10 * spiral) * 150 ) % 255;
        const b = ( Math.sin(10 * spiral) * 150 ) + Math.sqrt(y) * 2 % 255;
        ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
        ctx.fillRect(x, y, 1, 1);
      }
    }
    // window.requestAnimationFrame(this.updateCanvas);

    // -----------------------------------------------


    // ------------ Space thing ---------------------------------------------
    // ctx.beginPath();
    // for(let x = 0; x < canvasWidth; x++) {
    //   for(let y = 0; y < canvasHeight; y++) {
    //     const r = Math.cos((Math.sqrt(y)*Math.tan(x)*-x)) % 255;
    //     const b = Math.tan((Math.sqrt(y)*Math.tan(x)*x)) % 255;
    //     const g = (b + (r + (Math.PI/2))) % 255;

    //     ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    //     ctx.fillRect(x, y, 1, 1);
    //   }
    // }

    // ctx.globalAlpha = 0.01;
    // ctx.lineWidth=1;
    // // for(let i = 0; i < 50; i++) {
    // //   // ctx.beginPath();
    // //   // ctx.fillStyle = 'black';
    // //   ctx.strokeStyle = 'rgb(200, 50, 100)';
    // //   ctx.arc((Math.cos(i)*canvasWidth), (i)*10, Math.sqrt(i), 0, Math.PI * 2);
    // //   // ctx.fill();
    // //   ctx.stroke();
    // //   ctx.closePath();
    // // }
    // // ctx.beginPath();
    // // for(let i = 0; i < 50; i++) {
    // //   // ctx.fillStyle = 'black';
    // //   ctx.strokeStyle = 'rgb(200, 50, 100)';
    // //   ctx.arc((i*i)/2, i*10, Math.sqrt(i), 0, Math.PI * 2);
    // //   // ctx.fill();
    // //   ctx.stroke();
    // //   ctx.closePath();
    // // }

    // ctx.beginPath();
    // for(let i = 0; i < 50; i++) {
    //   // ctx.fillStyle = 'black';
    //   ctx.strokeStyle = 'rgb(200, 50, 100)';
    //   ctx.arc(Math.cos(i)*canvasWidth, i*10, Math.sqrt(i), 0, Math.PI * 2);
    //   // ctx.fill();
    //   ctx.stroke();
    //   ctx.closePath();
    // }
    // ctx.globalAlpha = 1;
    // ctx.lineWidth=0.5;
    // ctx.beginPath();
    // // ctx.fillStyle = 'white';
    // ctx.strokeStyle = 'white';
    // const radgrad = ctx.createRadialGradient(canvasWidth/2, canvasHeight/2, 100, canvasWidth/2, canvasWidth/2, 1);
    // radgrad.addColorStop(0, 'rgba(0,0,0,0)');
    // radgrad.addColorStop(1, '#70002C');
    // // radgrad.addColorStop(1, 'white');
    // ctx.fillStyle = radgrad;
    // ctx.arc(canvasWidth/2, canvasHeight/2, 70, 0, Math.PI * 2);
    // ctx.fill();
    // ctx.stroke();
    // ctx.closePath();

    // -------------------------------------------------------

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
