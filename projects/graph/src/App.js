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
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'green';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    ctx.fillStyle = 'white';
    // ctx.rect(20,20,150,100);
    // ctx.stroke();
    
    // ctx.fillRect(125, 125, 40, 40);
    // ctx.clearRect(45, 45, 60, 60);
    // ctx.strokeRect(50, 50, 30, 30);

    
    // ctx.lineTo(100,100);
    // ctx.stroke();
    ctx.fillStyle = 'red';
    for(let i=0; i < 2; i++){
        for(let j=0; j < 100; j++){
          
          //ctx.beginPath();
          ctx.moveTo(150+i*150,150+i*150);
          ctx.arc(150,150,100,50*j,20);
          //ctx.lineTo(10,100);
          ctx.stroke();
          ctx.closePath();
          //ctx.fill();
          ctx.fillStyle = 'blue';
        }
    }
  
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
