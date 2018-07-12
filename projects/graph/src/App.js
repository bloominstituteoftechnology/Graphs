import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';
import { randomFill } from 'crypto';

// !!! IMPLEMENT ME
const canvasWidth = 1050;
const canvasHeight = 800;

const circleRadius = 35;

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

    // Clear it
    ctx.fillStyle = 'teal';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.font= '15px Ariel';
    ctx.textAlign = 'center';
    ctx.textBaseline= 'middle';

    // draw the line between vertexes
    for(let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    //draw dummy vertex
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle ='red';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y)
    });

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
    this.state.graph.randomize(5, 4, 150, 0.6);
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
