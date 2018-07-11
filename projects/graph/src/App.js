import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 800;
const canvasHeight = 600;
const circleRadius = 15;

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

    console.log('this.props.graph: ', this.props.graph);

    
    
    ctx.fillStyle = 'lightgray';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '13px arial';
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    this.props.graph.vertexes.forEach(vert => {
      vert.edges.forEach(e => {
        ctx.beginPath();
        ctx.moveTo(vert.pos.x, vert.pos.y)
        ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
        ctx.stroke();
      });
    })

    this.props.graph.vertexes.forEach(v => {

      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();
      ctx.beginPath();
     
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });
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
   }

   button = () => {
      const graph = new Graph();
      graph.randomize(5, 4, 150, 0.6);
      this.setState({ graph });
    }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.button}>Randomize Graph</button>
      </div>
    );
  }
}

export default App;
