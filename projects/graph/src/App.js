import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvas();
    let refresh = setInterval(() => {
      action();
    }, 2000);
    let action = () => {
      this.props.graph.bfs();
      this.updateCanvas();
      console.log(this.props.graph)
      if (this.props.graph.stack.length === 0) {
        clearInterval(refresh);
      }
    }
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvas();
  }

  updateCanvas() {

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    ctx.fillStyle = '#7a9cd3';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    this.props.graph.vertexes.forEach((vertex) => {
      vertex.edges.forEach((edge) => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
      })
      ctx.lineWidth = 4;
      ctx.strokeStyle = '#FFFFFF';
      ctx.stroke();
    })
    this.props.graph.vertexes.forEach((vertex) => {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, Math.PI * 2, true);
      ctx.strokeStyle = '#324056'; // EB9D20
      ctx.stroke();
      ctx.fillStyle = vertex.color;
      ctx.fill();
      ctx.beginPath();
      ctx.font = '16px Georgia';
      ctx.fontStyle = 'bold';
      ctx.fillStyle = '#324056';
      ctx.fillText(vertex.value, vertex.pos.x - 7, vertex.pos.y + 4);
      ctx.fill();
    })
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

    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.bfs();
  }

  handleRandomize = (e) => {
    console.log('randomize')
    this.state.graph.randomize(5, 4, 150, 0.6);
  }
  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        {/* <button onClick={this.handleRandomize}>Randomize</button> */}
      </div>
    );
  }
}

export default App;
