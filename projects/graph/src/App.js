import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 1000; 
 const canvasHeight = 900;
 const circleRadius = 15;

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

    // !!! IMPLEMENT ME
    ctx.font = "13px Arial";
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);

      // v.edges.forEach((l) => {
      //   ctx.beginPath();
      //   ctx.moveTo(v.pos.x, v.pos.y);
      //   ctx.lineTo(l.destination.pos.x, l.destination.pos.y);
      //   ctx.stroke();
      // })
    })
    ctx.fillStyle = 'red';
    ctx.strokeStyle = 'red';
    let change = this.props.graph.bfs(this.props.graph.vertexes[0]);
    change.forEach((v) => {
      ctx.beginPath();
      // ctx.fillStyle = 'red';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();
      v.edges.forEach((l) => {
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(l.destination.pos.x, l.destination.pos.y);
        ctx.stroke();
      })
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

    // !!! IMPLEMENT ME
    this.state.graph.randomize(5, 3, 200);
    //console.log("props", this.props)
    console.log("state:\n", this.state)
    // use the graph randomize() method
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
