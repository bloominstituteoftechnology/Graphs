import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

const vertexRadius = 20;

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

    //create canvas background
    ctx.fillStyle = "lightgray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // check to see we have our vertexes
    //console.log(this.props.graph.vertexes);
    //console.log(this.props.graph.vertexes[0].edges[0]);

    //draw the edge
    for (let parentVert of this.props.graph.vertexes){
      for (let parentEdges of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(parentEdges.destination.pos.x, parentEdges.destination.pos.y);    
        ctx.stroke();
      }
    }
    // create nodes from debug creator in graph.js
    for (const parentVert of this.props.graph.vertexes) {
      ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
      ctx.beginPath();
      ctx.arc(parentVert.pos.x, parentVert.pos.y, vertexRadius, 0, 2*Math.PI);  
      ctx.stroke();
      ctx.fillStyle = parentVert.fillColor;
      ctx.fill();
      ctx.font = "12px Arial";
      ctx.fillStyle = "black"
      ctx.textBaseline = "middle";
      ctx.textAlign = "center"
      ctx.fillText(parentVert.value, parentVert.pos.x, parentVert.pos.y);
     
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

    //this.state.graph.debugCreateTestData();
    this.state.graph.randomize(3, 3, 80, .45);
    let ans = this.state.graph.dfs(this.state.graph.vertexes[0]);
    if (ans.length < this.state.graph.vertexes.length) {
      for (let vertex of this.state.graph.vertexes) {
        if (vertex.fillColor === "white") {
          ans = this.state.graph.dfs(vertex);
        }
      }
    }

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