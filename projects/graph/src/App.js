import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const g = this.props.graph;

    g.randomize(5, 4, 150, 0.6);
    g.dump();
    console.log(g.bfs(g.vertexes[0]));

    for (let v of g.vertexes) {
      if (v.pos) {
        ctx.beginPath();
        ctx.fillStyle = 'black';
        ctx.arc(v.pos.x, v.pos.y, 20, 0, Math.PI * 2, true);
        ctx.fill();
        for (let e of v.edges) {
          ctx.beginPath();
          ctx.strokeStyle='black';
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
          ctx.closePath();
          ctx.stroke();
        }
        ctx.font = '15px serif';
        ctx.fillStyle = 'white';
        ctx.fillText(`${v.value}`, v.pos.x - 10, v.pos.y);
      }
    }
  }
  
  /**
   * Render
   */
  render() {
    return (
    <div>
      <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
    </div>
    );
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
  }

  newGraph = () => {
    const newGraph = new Graph();
    this.setState({ graph: newGraph });
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.newGraph}>MORE!</button>
      </div>
    );
  }
}

export default App;
