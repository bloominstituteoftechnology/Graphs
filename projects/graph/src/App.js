import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
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
    // Sky
    ctx.fillStyle = 'goldenrod';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //sun colors
    ctx.fillStyle = 'sienna';
    ctx.fillRect(0, 10, 600, 10);
    ctx.fillRect(0, 20, 600, 10);
    ctx.fillRect(0, 30, 600, 10);
    ctx.fillRect(0, 0, 600, 10);
    
    ctx.fillStyle = 'peru';
    ctx.fillRect(0, 40, 600, 10);
    ctx.fillRect(0, 50, 600, 10);
    ctx.fillRect(0, 60, 600, 10);
    ctx.fillRect(0, 70, 600, 10);

    ctx.fillStyle = 'sandybrown';
    ctx.fillRect(0, 130, 600, 10);
    ctx.fillRect(0, 140, 600, 10);
    ctx.fillRect(0, 150, 600, 10);
    ctx.fillRect(0, 160, 600, 10);

    ctx.fillStyle = 'darkgoldenrod';
    ctx.fillRect(0, 210, 600, 10);
    ctx.fillRect(0, 200, 600, 10);
    ctx.fillRect(0, 190, 600, 10);
    ctx.fillRect(0, 180, 600, 10);
    ctx.fillRect(0, 170, 600, 10);

    //sun
    ctx.fillStyle = 'yellow';
    ctx.fillRect(225, 110, 150, 150);

    //ground
    ctx.fillStyle = 'brown';
    ctx.fillRect(0, 215, canvasWidth, 200);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

      // let xWid = Math.floor((Math.random()*600)+1);
      // let yHi = Math.floor((Math.random()*400)+1);
      // let bubSize = Math.floor((Math.random()*30)+1);
    
    ctx.fillStyle = 'maroon';
    //neck
    ctx.fillRect(300, 200, 10, 70);
    //head
    ctx.fillRect(290, 190, 20, 20);
    //body
    ctx.fillRect(295, 220, 17, 45);
    ctx.fillRect(295, 215, 20, 20);
    ctx.fillRect(295, 245, 20, 15);
    //left leg
    ctx.fillRect(290, 260, 10, 15);
    ctx.fillRect(285, 270, 10, 15);
    ctx.fillRect(280, 280, 7, 10);
    ctx.fillRect(279, 280, 5, 20);
    //right leg
    ctx.fillRect(310, 260, 10, 15);
    ctx.fillRect(315, 270, 10, 15);
    ctx.fillRect(320, 280, 7, 10);
    ctx.fillRect(323, 280, 5, 20);
    //left arm
    ctx.fillRect(290, 220, 15, 5);
    ctx.fillRect(290, 225, 15, 5);
    ctx.fillRect(285, 230, 5, 5);
    ctx.fillRect(280, 230, 5, 5);
    ctx.fillRect(275, 225, 5, 5);
    ctx.fillRect(270, 220, 5, 5);

    // clouds
    ctx.fillStyle = 'orange';
    ctx.fillRect(90, 50, 10, 10);
    ctx.fillRect(110, 50, 10, 10);
    ctx.fillRect(100, 50, 10, 10);
    ctx.fillRect(100, 60, 10, 10);
    ctx.fillRect(110, 60, 10, 10);
    ctx.fillRect(120, 60, 10, 10);
    ctx.fillRect(80, 60, 10, 10);
    ctx.fillRect(90, 60, 10, 10);
    ctx.fillRect(100, 70, 10, 10);
    ctx.fillRect(110, 70, 10, 10);
    ctx.fillRect(120, 70, 10, 10);
    ctx.fillRect(80, 70, 10, 10);
    ctx.fillRect(90, 70, 10, 10);
    ctx.fillRect(130, 70, 10, 10);

    ctx.fillStyle = 'orange';
    ctx.fillRect(90, 150, 10, 10);
    ctx.fillRect(110, 150, 10, 10);
    ctx.fillRect(100, 150, 10, 10);
    ctx.fillRect(100, 160, 10, 10);
    ctx.fillRect(110, 160, 10, 10);
    ctx.fillRect(120, 160, 10, 10);
    ctx.fillRect(80, 160, 10, 10);
    ctx.fillRect(90, 160, 10, 10);
    ctx.fillRect(100, 170, 10, 10);
    ctx.fillRect(110, 170, 10, 10);
    ctx.fillRect(120, 170, 10, 10);
    ctx.fillRect(80, 170, 10, 10);
    ctx.fillRect(90, 170, 10, 10);
    ctx.fillRect(130, 170, 10, 10);
  
    

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
