import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
// const canvasWidth = 
// const canvasHeight = 
const canvasWidth = 750;
const canvasHeight = 600;

const circlesize = 15;

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
    console.log('in update canvas', this.props.graph.vertexes);
    // Clear it
    ctx.fillStyle = 'cyan';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '15px Ariel';
    ctx.fillStyle = 'black';

    for (let vertex of this.props.graph.vertexes) {
      // ctx.moveTo(vertex.pos.x, vertex.pos.y);
      // ctx.lineTo(100, 100);
      // ctx.stroke();
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circlesize, 0, 2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();

      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.stroke();


      for (let edge of vertex.edges) {
        const posX = vertex.pos.x;
        const posY = vertex.pos.y;
        ctx.beginPath();
        ctx.moveTo(posX, posY);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

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
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
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

    this.state.graph.randomize(5, 4, 150, 0.6)
    // !!! IMPLEMENT ME
    // use the graph randomize() method
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
