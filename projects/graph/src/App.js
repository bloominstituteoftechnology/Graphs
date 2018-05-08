import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = (window.innerWidth-20);
const canvasHeight = (window.innerHeight-20);

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

  stack = [];

  /**
   * Render the canvas
   */
  resetVertexes() {
    this.props.graph.vertexes.forEach((vertex) => {
      vertex.color = 'white';
    })
  }

  randomColor() {
    const genRand = () => {
      return Math.floor(Math.random() * Math.floor(255));
    };
    return `rgb(${genRand()}, ${genRand()}, ${genRand()})`;
  }

  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    ctx.clearRect(0,0,canvasWidth,canvasHeight);
    ctx.fillStyle = '#FFCD7D';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    const renderGraph = (q) => {
      q.forEach((vertex) => {
        vertex.edges.forEach((edge) => {
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.lineWidth = 5;
          ctx.strokeStyle = this.randomColor();
          ctx.stroke();
        })
      })
      q.forEach((vertex) => {
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, Math.PI * 2, true);
        ctx.strokeStyle = '#EB9D20'; // EB9D20
        ctx.stroke();
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();
        ctx.beginPath();
        ctx.font = '14px Georgia';
        ctx.fontStyle = 'bold';
        ctx.fillStyle = '#975D00';
        if (vertex.value.length < 3) {
          ctx.fillText(vertex.value, vertex.pos.x-9, vertex.pos.y+5);
        } else {
          ctx.fillText(vertex.value, vertex.pos.x-12, vertex.pos.y+5);
        }
        ctx.fill();
      })
    }
    let queue = this.props.graph.bfs(this.props.graph.vertexes[0]);
    while (queue.length > 0) {
      let nextQueue = [];
      renderGraph(queue);
      this.props.graph.vertexes.forEach((vertex) => {
        if (vertex.color === 'white') {
          nextQueue.push(vertex);
        } 
      })
      if (nextQueue.length > 0) {
        let nextStart = parseInt(nextQueue[0].value.substr(1));
        queue = this.props.graph.bfs(this.props.graph.vertexes[nextStart]);
      } else break;
    }
  }

  bfsRender(start = 0) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    let queue = this.props.graph.bfs(this.props.graph.vertexes[start]);
    let newQueue = [];
    queue.forEach((item) => {
      ctx.beginPath();
      ctx.arc(item.pos.x, item.pos.y, 20, 0, Math.PI * 2, true);
      ctx.strokeStyle = '#000000'; // EB9D20
      ctx.stroke();
    })
    this.props.graph.vertexes.forEach((vertex) => {
      if (vertex.color === 'white') {
        newQueue.push(vertex);
      }
    })
    if (newQueue.length > 0) {
      let nextStart = parseInt(newQueue[0].value.substr(1));
      console.log(nextStart);
      let _this = this;
      setTimeout(function() { _this.bfsRender(nextStart); }, 1000);
    }
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
        <button onClick = {() => {
            this.props.graph.vertexes = [];
            this.props.graph.randomize(5,5,120);
            this.updateCanvas();
          }}>New Graph</button>
        <button onClick = {() => {
          this.resetVertexes();
          this.bfsRender();
        }}>BFS</button>
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

    this.state.graph.randomize(5,5,120);
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
