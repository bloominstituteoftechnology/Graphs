import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const circleRad = 15;

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
    this.props.graph.randomize(5, 4, 150, 0.6)
    for(let i = 0; i < this.props.graph.vertexes.length; i++) {
      if(this.props.graph.vertexes[i].color === 'white'){
        // color map all connected vertices
        this.props.graph.bfs(this.props.graph.vertexes[i]);
      }
    }

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
        
    // Clear it
    ctx.font = "13px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = "gray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw vertices
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = v.color;
      ctx.arc(v.pos.x, v.pos.y, circleRad, 0, 2*Math.PI);
      ctx.fill();
      
      // put text in vertex
      ctx.beginPath();
      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.pos.x, v.pos.y);


      // draw edges between connected vertices
      if(v.edges.length > 0) {
        for(let i = 0; i < v.edges.length; i++) {
          ctx.beginPath();
          ctx.strokeStyle = v.color;
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(v.edges[i].destination.pos.x, v.edges[i].destination.pos.y);
          ctx.stroke();
        }
      }
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

    this.handleButton = () => {
      this.setState({graph: new Graph ()});
    }

    this.doBFS = () => {
      for(let i = 0; i < this.state.graph.vertexes.length; i++) {
        if(this.state.graph.vertexes[i].color === 'white'){
          // color map all connected vertices
          this.state.graph.bfs(this.state.graph.vertexes[i]);
        }
      }
    }
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView><br/>
        <button onClick={() => this.handleButton()}>Re-Roll Graph</button>
      </div>
    );
  }
}

export default App;