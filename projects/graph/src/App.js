import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
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
    // also can use canvas.width = canvas.width;

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (label)

    //Edges
    ctx.lineWidth = 3;
    ctx.strokeStyle = '#CCCC00';

    // Let V be the set of vertices in G
    for (let v of this.props.graph.vertexes) {
      // Let E the set of edges in G (vertex)
      for (let e of v.edges) {
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y); //Point1 of edge
        const v2 = e.destination; //
        ctx.lineTo(v2.pos.x, v2.pos.y); // connect 2 points with a line
        ctx.stroke(); // fill the line in
      }
    }

    // Vertexes
    ctx.fillStyle = 'purple';
    ctx.lineWidth = 2;
    ctx.strokeStyle = 'orange';

    // Let V be the set of vertices in G
    for (let v of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, 22, 0, 2 * Math.PI, false);
      ctx.fill();
      ctx.stroke();
    }

    // Labels
    ctx.fillStyle = 'black';
    ctx.font = 'italic 12pt Calibri';
    ctx.textAlign = 'center';

    for (let v of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    }
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 3, 150, 0.6);
    this.state.graph.bfs(this.state.graph.vertexes[0]);
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
