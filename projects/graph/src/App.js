import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = window.innerWidth - 5;
const canvasHeight = window.innerHeight - 5;

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
    let y = 0;
    let traverse = 1;
    let velocity = 0;
    const MAX_VEL = 3;

    const draw = () => {
      let canvas = this.refs.canvas;
      let ctx = canvas.getContext('2d');

      // Clear it

      ctx.fillStyle = 'black';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
      ctx.fillStyle = 'red';
      ctx.fillRect(canvasWidth / 2, y, 30, 30);


      if (traverse === 1) {
        if (~~y + 30 <= canvasHeight){
          y += velocity;
          if (velocity < MAX_VEL) {
            velocity += 0.01;
          }
        } else {
          traverse = 0;
        }
      } else {
        if (velocity > 0.01) {
          y -= velocity;
          velocity -= 0.014;
        } else {
          if (~~y + 30 < canvasHeight) {
            traverse = 1;
          } else {
            clearInterval(a)
          }
        }
      }
    }
    
    const a = window.setInterval(draw, 1)
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
