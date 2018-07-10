import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 900;
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
    
    // Clear it
    ctx.fillStyle = '#c0dfe8';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    console.log(ctx);
    

    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(10, 10, 880, 780);

    ctx.fillStyle = '#bf9ebe';

    // ctx.beginPath();
    // ctx.arc(110, 180, 90, 0, Math.PI)
    // ctx.stroke();

    // ctx.beginPath();
    // ctx.arc(290, 180, 90, 1, Math.PI, true)
    // ctx.fill();
    function strokeStar(x, y, r, n, inset) {
      ctx.save();
      ctx.beginPath();
      ctx.translate(x, y);
      ctx.moveTo(0,0-r);
      for (var i = 0; i < n; i++) {
          ctx.rotate(Math.PI / n);
          ctx.lineTo(0, 0 - (r*inset));
          ctx.rotate(Math.PI / n);
          ctx.lineTo(0, 0 - r);
      }
      let rand = Math.random() * 2;
      ctx.fillStyle = rand > 1 ? "red" : "blue";
      ctx.closePath();
      ctx.fill();
      ctx.restore();
  }
  let stars = strokeStar(200, 350, 30, 5, 3);

    // ctx.beginPath();
    // ctx.moveTo(300, 250);
    
    // ctx.stroke();

    const star = new Image();
    let rand = Math.random() * 2;
    const url1 = 'https://vectr.com/tmp/aMt2sqUiO/b1ox4deAmE.svg?width=640&height=640&select=b1ox4deAmEpage0';
    const url2 = 'https://vectr.com/tmp/aMt2sqUiO/ft9txtpky.svg?width=640&height=640&select=ft9txtpkypage0';
    

    function start() {
      //ball.src = "https://mdn.mozillademos.org/files/1456/Canvas_sun.png";
      
      window.requestAnimationFrame(game);
    }

    function game() {
      //ctx.globalCompositeOperation = "destination-over";
      // ctx.save();
      // ctx.translate(250, 250);
      

      const time = new Date();

      ctx.save();
      ctx.rotate(2 * time.getSeconds() + 2 * time.getMilliseconds());
      //ctx.translate(30, 40);
      star.src = rand > 1 ? url1 : url2;
      ctx.drawImage(star, (Math.random() * 1000), (Math.random() * 1000));

      //ctx.restore();
      // ctx.fillStyle = '#fff263'
      // ctx.beginPath();
      // //ctx.arc(30, 40, 300, 0, Math.PI);
      // ctx.fill();

      window.requestAnimationFrame(game);
    }

    start();


    






    



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
