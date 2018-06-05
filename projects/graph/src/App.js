import React, { Component } from 'react';
import { Graph, Vertex, Edge } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

const circleSize = 15;

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
  updateCanvas = () => {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = '#f1f1f1';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px, Ariel';
    ctx.fillStyle = 'black';

    let vertex = this.props.graph.vertexes;

    for (let vertex of this.props.graph.vertexes) {
      let { value, pos, edges } = vertex;

      ctx.beginPath();
      ctx.arc(pos.x, pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.fillStyle = 'black';
      ctx.fillText(value, pos.x, pos.y);
      ctx.stroke();

      // console.log('find edges: ', edges);
      // iterate over edges array to access destination. forEach?
      edges.forEach(edge => {
        console.log('inside edges destination: ', edge.destination.pos);
        let edgeX = edge.destination.pos.x;
        let edgeY = edge.destination.pos.y;

        ctx.lineTo(edgeX, edgeY);
      });

      ctx.stroke();
    }
    console.log('vertex array: ', vertex);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    // window.requestAnimationFrame(this.updateCanvas);
  };

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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.debugCreateTestData();
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
