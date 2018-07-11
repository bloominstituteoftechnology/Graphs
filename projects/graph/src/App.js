import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 750;
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
    
    ctx.fillStyle = 'teal';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)


    /*
    ctx.beginPath();
    ctx.arc(50, 50, 15, 0, 2 * Math.PI);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(300, 300, 15, 0, 2 * Math.PI);
    ctx.moveTo(300, 300);
    ctx.lineTo(50, 50);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(500, 150, 15, 0, 2 * Math.PI);
    ctx.moveTo(500, 150);
    ctx.lineTo(300, 300);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(20,100);
    ctx.lineTo(100, 100);

    ctx.moveTo(100,20);
    ctx.lineTo(100, 100);
    ctx.stroke();
    */

    // console.log("this.props.graph: ", this.props.graph);
    // this.props.graph.createDummyGraph();
    // console.log("call createDummyGraph: ");


    ctx.font = '15px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
 
    for (let vertex of this.props.graph.vertexes) {
      for ( let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    // this.props.graph.vertexes.forEach((v) => {
      for (let v of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, 15, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);
    // this.state.graph.createDummyGraph();
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
