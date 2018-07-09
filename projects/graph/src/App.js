import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

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
    const ctx = canvas.getContext('2d');
    
    
    var gradient = ctx.createLinearGradient(50, 400, 50, 0);
        gradient.addColorStop(0, 'blue');
        gradient.addColorStop(.3, 'skyblue');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.strokeStyle = 'yellow';
    for (let i = 0; i < 200; i++) {
      ctx.beginPath();
      ctx.moveTo(Math.cos(i) * 0, Math.sin(i) * 0);
      ctx.lineTo(Math.sin(i) * 200, Math.cos(i) * 200);
      ctx.stroke();
    }

    ctx.beginPath();
    ctx.arc(30, 20, 40, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'yellow';
    ctx.fillStyle = 'yellow';
    ctx.fill();

    ctx.beginPath();
    ctx.ellipse(350, 525, 250, 150, 1 * Math.PI/180, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#D4C6AC';
    ctx.fillStyle = '#D4C6AC';
    ctx.fill();
    

    ctx.beginPath();
    ctx.arc(300, 35, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(315, 30, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(330, 25, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(345, 25, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(360, 30, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(375, 35, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(315, 40, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(330, 45, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(345, 45, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(360, 40, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = 'white';
    ctx.fillStyle = 'white';
    ctx.fill();    


    ctx.beginPath();
    ctx.arc(210, 55, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(225, 50, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(240, 45, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(255, 45, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(270, 50, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(285, 55, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(225, 60, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(240, 65, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(255, 65, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
    ctx.beginPath();
    ctx.arc(270, 60, 20, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.strokeStyle = '#f7f7f7';
    ctx.fillStyle = '#f7f7f7';
    ctx.fill();    
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
