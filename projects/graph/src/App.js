import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 1000;

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
    ctx.fillStyle = '#FFFAF0';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    const { vertexes } = this.props.graph;

    for (let i = 0; i < vertexes.length; i++) {
      const {x, y} = vertexes[i].pos;
      console.log(vertexes[i]);
      vertexes[i].edges.forEach((edge) => {
        const {x: x2 , y: y2} = edge.destination.pos;

        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x2, y2);
        ctx.stroke();
      });
    }

    ctx.fillStyle = 'dimgray';
    ctx.lineWidth = 2;
    ctx.strokeStyle = 'blue';

    for (let i = 0; i < vertexes.length; i++) {
      const {x, y} = vertexes[i].pos;
      ctx.beginPath();
      ctx.arc(x, y, 20, 0, 2 * Math.PI, false);
      ctx.fill();
      ctx.stroke();
    }

    ctx.fillStyle = 'black';
    ctx.font = '13pt Helvetica';
    ctx.textAlign = 'center';

    for (let i = 0; i < vertexes.length; i++) {
      const {x, y} = vertexes[i].pos;
      ctx.beginPath();
      ctx.fillText(vertexes[i].value, x, y);
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
    this.state.graph.randomize(5,4,150,0.6);
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
