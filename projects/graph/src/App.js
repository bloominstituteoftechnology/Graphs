import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = window.innerWidth - 5;
const canvasHeight = window.innerHeight - 5;
const radius = 14;

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

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    // this.props.graph.createDummyGraph();

    // Clear it
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '12px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // draw our dummy vertexes
    this.props.graph.vertexes.forEach((v) => {
      v.edges.forEach((e) => {
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(e.dest.pos.x, e.dest.pos.y);
        ctx.stroke();
      })
    })

    this.props.graph.vertexes.forEach((v) => {
      this.props.graph.bfs(v);
      ctx.beginPath();
      ctx.fillStyle = v.color;
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();
      //
      // // fill in the text
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(10, 6, 100, 0.4);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button className='button' onClick={
          () => {
            const graph = new Graph();
            graph.randomize(10, 6, 100, 0.4);
            this.setState({ graph });
          }
        }>Hit me</button>
      </div>
    );
  }
}

export default App;
