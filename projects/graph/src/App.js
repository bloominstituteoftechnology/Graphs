import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1280;
const canvasHeight = 720;

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
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Draw Pretty Picture
    function getRandomColor() {
      var letters = '0123456789ABCDEF';
      var color = '#';
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }

    let centerX = canvasWidth / 2;
    let centerY = canvasHeight / 2;
    let radius = -540;
    let radius2 = 0;
    for (let i = 0.25; i < 1080; i = i + 0.25) {
      let strokeColor = getRandomColor();
      let x = centerX + (radius + i) * Math.cos(-i * Math.PI / 180) * -1;
      let y = centerY + (radius + i) * Math.sin(-i * Math.PI / 180) * -1;
      let lineX = centerX + (radius + i) * Math.cos(-i * Math.PI / 180) * -3;
      let lineY = centerY + (radius + i) * Math.sin(-i * Math.PI / 180) * -3;
      ctx.strokeStyle = `${strokeColor}55`;
      ctx.beginPath();
      ctx.fillStyle = `${strokeColor}33`;
      ctx.arc(x, y, 9, 0.01, 0.01 * Math.PI);
      ctx.stroke();
      ctx.lineTo(lineX, lineY);
      ctx.stroke();
      ctx.fill();
    }

    // End Draw Pretty Picture

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
