import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1400
const canvasHeight = 800


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
    let ctx = canvas.getContext("2d");
    let raf;
    let running = false;

    // Clear it
    ctx.fillStyle = "#626D71";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fillStyle = "#CDCDC0";
    ctx.fillRect(100, 100, canvasWidth, canvasHeight);
    ctx.fillStyle = "#DDBC95";
    ctx.fillRect(200, 200, canvasWidth, canvasHeight);
    ctx.fillStyle = "#B38867";
    ctx.fillRect(300, 300, canvasWidth, canvasHeight);
    var ball = {
      x: 100,
      y: 100,
      vx: 5,
      vy: 1,
      radius: 10,
      color: 'dark-brown',
      draw: function() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
        ctx.closePath();
        ctx.fillStyle = this.color;
        ctx.fill();
      }
    };
    
    function clear() {
      ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
      // ctx.fillRect(0,0,canvas.width,canvas.height);
    }
    
    function draw() {
       clear();
      ball.draw();
      ball.x += ball.vx;
      ball.y += ball.vy;
    
      if (ball.y + ball.vy > canvas.height || ball.y + ball.vy < 0) {
        ball.vy = -ball.vy;
      }
      if (ball.x + ball.vx > canvas.width || ball.x + ball.vx < 0) {
        ball.vx = -ball.vx;
      }
    
      raf = window.requestAnimationFrame(draw);
    }
    
    canvas.addEventListener('mousemove', function(e) {
      if (!running) {
        clear();
        ball.x = e.clientX;
        ball.y = e.clientY;
        ball.draw();
      }
    });
    
    canvas.addEventListener('click', function(e) {
      if (!running) {
        raf = window.requestAnimationFrame(draw);
        running = true;
      }
    });
    
    canvas.addEventListener('mouseout', function(e) {
      window.cancelAnimationFrame(raf);
      running = false;
    });
    
    ball.draw();
  
  }

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  

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
      <header className="App-header">
          {/* <img src={logo} className="App-logo" alt="logo" /> */}
          <h1 className="App-title">Canvas API</h1>
        </header>
        <GraphView graph={this.state.graph}>Canvas API</GraphView>
      </div>
    );
  }
}

export default App;
