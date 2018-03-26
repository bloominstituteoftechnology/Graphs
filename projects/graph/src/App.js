import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 700;
const canvasHeight = 700;

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
    let radius = 15;
    // Clear it
    ctx.fillStyle = "grey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    

    ctx.beginPath();
    ctx.arc(350,200, 30,0,2*Math.PI);
    ctx.stroke();
    ctx.moveTo(350,230);
    ctx.lineTo(200,370);
    ctx.stroke();

    ctx.moveTo(350,230);
    ctx.lineTo(300,370);
    ctx.stroke();

    ctx.font = "30px Arial";
    ctx.textAlign = "center";
    ctx.strokeText("1",345,207);

    ctx.beginPath();
    ctx.arc(200,400, 30,0,2*Math.PI);
    ctx.stroke();
    ctx.font = "30px Arial";
    ctx.textAlign = "center";
    ctx.strokeText("2",195,395);

    ctx.beginPath();
    ctx.arc(300,400, 30,0,2*Math.PI);
    ctx.stroke();
    ctx.font = "30px Arial";
    ctx.textAlign = "center";
    ctx.strokeText("3",295,395);
    

    
   

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
