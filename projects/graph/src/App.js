import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
let canvasWidth = 500;
let canvasHeight = 500;

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
    
    // Base Layer
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, 500, 500);

    ctx.fillStyle = 'white';
    ctx.fillRect(80, 80, 340, 340);

    ctx.fillStyle = 'grey';
    ctx.fillRect(150, 150, 200, 200);

    // Top Left
    ctx.fillStyle = 'red';
    ctx.fillRect(0, 0, 70, 70);

    ctx.fillStyle = 'orange';
    ctx.fillRect(0, 0, 60, 60);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(0, 0, 50, 50);

    ctx.fillStyle = 'green';
    ctx.fillRect(0, 0, 40, 40);

    ctx.fillStyle = 'blue';
    ctx.fillRect(0, 0, 30, 30);

    ctx.fillStyle = 'indigo';
    ctx.fillRect(0, 0, 20, 20);

    ctx.fillStyle = 'violet';
    ctx.fillRect(0, 0, 10, 10);

    // Top Right
    ctx.fillStyle = 'red';
    ctx.fillRect(430, 0, 70, 70);

    ctx.fillStyle = 'orange';
    ctx.fillRect(440, 0, 60, 60);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(450, 0, 50, 50);

    ctx.fillStyle = 'green';
    ctx.fillRect(460, 0, 40, 40);

    ctx.fillStyle = 'blue';
    ctx.fillRect(470, 0, 30, 30);

    ctx.fillStyle = 'indigo';
    ctx.fillRect(480, 0, 20, 20);

    ctx.fillStyle = 'violet';
    ctx.fillRect(490, 0, 10, 10);
    
    // Bottom Left
    ctx.fillStyle = 'red';
    ctx.fillRect(0, 430, 70, 70);

    ctx.fillStyle = 'orange';
    ctx.fillRect(0, 440, 60, 60);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(0, 450, 50, 50);

    ctx.fillStyle = 'green';
    ctx.fillRect(0, 460, 40, 40);

    ctx.fillStyle = 'blue';
    ctx.fillRect(0, 470, 30, 30);

    ctx.fillStyle = 'indigo';
    ctx.fillRect(0, 480, 20, 20);

    ctx.fillStyle = 'violet';
    ctx.fillRect(0, 490, 10, 10);

    // Bottom Right
    ctx.fillStyle = 'red';
    ctx.fillRect(430, 430, 70, 70);

    ctx.fillStyle = 'orange';
    ctx.fillRect(440, 440, 60, 60);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(450, 450, 50, 50);

    ctx.fillStyle = 'green';
    ctx.fillRect(460, 460, 40, 40);

    ctx.fillStyle = 'blue';
    ctx.fillRect(470, 470, 30, 30);

    ctx.fillStyle = 'indigo';
    ctx.fillRect(480, 480, 20, 20);

    ctx.fillStyle = 'violet';
    ctx.fillRect(490, 490, 10, 10);
    
    // Center
    ctx.fillStyle = 'red';
    ctx.fillRect(215, 215, 70, 70);

    ctx.fillStyle = 'orange';
    ctx.fillRect(220, 220, 60, 60);

    ctx.fillStyle = 'yellow';
    ctx.fillRect(225, 225, 50, 50);

    ctx.fillStyle = 'green';
    ctx.fillRect(230, 230, 40, 40);

    ctx.fillStyle = 'blue';
    ctx.fillRect(235, 235, 30, 30);

    ctx.fillStyle = 'indigo';
    ctx.fillRect(240, 240, 20, 20);

    ctx.fillStyle = 'violet';
    ctx.fillRect(245, 245, 10, 10);



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
