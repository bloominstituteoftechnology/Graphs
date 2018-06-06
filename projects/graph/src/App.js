import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleSize = 20;

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
    ctx.fillStyle = 'rgb(0, 206, 209)';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log('in updateCanvas', this.props.graph.vertexes);
    

    this.props.graph.vertexes.forEach((vertex, index, array) => {
      console.log(vertex,index, array);
      vertex.edges.forEach(edge => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        console.log(edge);
        ctx.stroke();
      });
    });
    this.props.graph.vertexes.forEach((vertex, index, array) => {
      ctx.beginPath();
    ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
    ctx.fillStyle = 'white';
    ctx.fill();
    ctx.stroke();
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';
    ctx.fillStyle = 'black';
    ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    ctx.closePath();
    });


    // const rectangles = setInterval(() => {
    //   ctx.fillStyle = `#${randomFromPalette()}`;
    //   ctx.fillRect(randomX(), randomY(), randomX(), randomY());
    // }, 100)

    // const circles = setInterval (() => {
    //   ctx.beginPath();
    //   ctx.arc(randomY(), randomX(), randomX()/2, 0, 2 * Math.PI);
    //   ctx.stroke();
    //   ctx.fill();
    //   ctx.closePath();
    // }, 1000);

    // const lines = setInterval(() => {
    //     ctx.beginPath();
    //     ctx.moveTo(randomX(), randomY());
    //     ctx.strokeStyle = `#${randomFromPalette()}`
    //     ctx.lineTo(randomX(), randomY());
    //     ctx.stroke();
    //     ctx.closePath();
    //   }, 100);
    

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
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
