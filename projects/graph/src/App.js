import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000; 
const canvasHeight = 800;
let circleSize = 15;
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
    this.props.graph.randomize(10, 10, 75);
    ctx.fillStyle = 'goldenrod';
    ctx.fillRect(0,0, canvasWidth, canvasHeight);
    console.log('in update canvas', this.props.graph.vertexes);
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let vertex = this.props.graph.vertexes[i];
      for (let j = 0; j < vertex.edges.length; j++){
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(vertex.edges[j].destination.pos.x, vertex.edges[j].destination.pos.y);
        ctx.stroke();
      }

    }
    
    
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let vertex = this.props.graph.vertexes[i];
      ctx.beginPath(vertex.pos.x, vertex.pos.y);
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2*Math.PI);
      let vertColor = Math.floor((Math.random() * 16777215) + 1);
      let color = '#'+(Math.random()*0xFF6633<<0).toString(16);
      ctx.fillStyle = color;
      console.log(vertex.value + ' ' + color);
      ctx.fill();
      ctx.stroke();

      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '15px Arial';
      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
    
    // My beautiful artwork below
    // ctx.fillStyle = 'lightgrey';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // ctx.fillStyle = 'goldenrod';
    // ctx.fillRect(100, 0, 100, 800);

    // ctx.fillRect(350, 0, 40, 800);

    // ctx.strokeStyle = 'red';
    // for (let i = 2; i < 1000; i+=8){
    //   ctx.beginPath();
    //   ctx.arc(i*i/2000,i*i/1000,50, 0, Math.PI * 2);
    //   ctx.stroke();
    // }

    // ctx.moveTo(4/2000, 4/1000);
    // ctx.lineTo(1000*1000/2000, 1000*1000/1000);
    // ctx.stroke();

    // for (let i = 0; i < 250; i+=.5) {
    //   ctx.strokeStyle = 'black';
    //   ctx.beginPath();
    //   ctx.arc(250,300,i, i, .75*Math.PI + i);
    //   ctx.stroke();
    // }
    // for (let i = 0; i < 150; i++) {
    //   ctx.strokeStyle = 'green';
    //   ctx.beginPath();
    //   ctx.arc(400,150,i, i*Math.PI, .75*Math.PI + i);
    //   ctx.stroke();
    // }
    // for (let i = 0; i < 100; i++) {
    //   ctx.strokeStyle = 'blue';
    //   ctx.beginPath();
    //   ctx.arc(100,650,i, i*Math.PI, .75*Math.PI + i);
    //   ctx.stroke();
    // }
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
