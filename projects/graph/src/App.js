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

    ctx.beginPath();
    ctx.arc(110, 180, 90, 0, Math.PI)
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(290, 180, 90, 1, Math.PI, true)
    ctx.fill();

    // ctx.beginPath();
    // ctx.moveTo(300, 250);
    
    // ctx.stroke();

    const ball = new Image();

    function start() {
      ball.src = "https://cdn.pixabay.com/photo/2013/07/12/14/09/football-147854_960_720.png";
      //ball.src = "https://mdn.mozillademos.org/files/1456/Canvas_sun.png";
      ball.size = '50px';
      
      window.requestAnimationFrame(game);
    }

    function game() {
      //ctx.globalCompositeOperation = "destination-over";
      ctx.save();
      ctx.translate(250, 250);

      const time = new Date();

      ctx.save();
      ctx.rotate(((2 * Math.PI) / 6) * time.getSeconds() + ((2 * Math.PI) / 60000) * time.getMilliseconds());
      ctx.translate(205, 40);
      ctx.drawImage(ball, -12, -12);

      ctx.restore();
      ctx.beginPath();
      ctx.arc(300, 400, 300, 0, Math.PI * 2);
      ctx.stroke();

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
