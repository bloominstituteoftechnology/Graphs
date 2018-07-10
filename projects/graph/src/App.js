import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const xCount = 7;
const yCount = 7;
const boxSize = 100;
const probability = 0.6;

// Figure out the canvas size
const canvasWidth = boxSize * xCount;
const canvasHeight = boxSize * yCount;
const radius = boxSize / 8;

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

  drawVerts(vertexes) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    ctx.fillStyle = 'maroon';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    ctx.lineWidth = 1.5;
    ctx.strokeStyle = 'white';

    // set up the verts and edges
    for (let v of vertexes) {
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.stroke();
    }

    // fill in the verts with color
    for (let v of vertexes) {
      ctx.beginPath();
      ctx.fillStyle = 'black';
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.fill();
    }
    
    // label the verts
    for (let v of vertexes) {
      ctx.beginPath();
      ctx.font = '14px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillStyle = 'white';
      ctx.fillText(v.value, v.pos.x, v.pos.y );
    }
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    const g = this.props.graph;
    this.drawVerts(g.vertexes);
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
    this.state.graph.randomize(xCount, yCount, boxSize, probability);
  }
  refreshPage(){ 
    window.location.reload(); 
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <input type="button" value="Reload Page" onClick={ this.refreshPage }/>
      </div>
    );
  }
}

export default App;