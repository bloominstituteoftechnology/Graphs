import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750
const canvasHeight = 600

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

    ctx.fillStyle = 'blue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.fillStyle = 'gold'
    
    const radius = 23;
    const verticies = this.props.graph.verticies;

    verticies.map(vertex => {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 10,0,2*Math.PI)
      ctx.fill();
      vertex.edges.map(edge => {
        const vertexPair = edge.destination;
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(vertexPair.pos.x, vertexPair.pos.y);
        ctx.stroke();
      })
    })

    for (let vertex of verticies) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2 * Math.Pi);
      ctx.fillStyle = 'green';
      ctx.fill();
      ctx.stroke();


      
      
    
 
      
    // Clear it
    

    

    // verticies.map(vertex => {
    //   // for(let v of this.props.graph.vertexes) {
    //   ctx.beginPath();
    //   ctx.arc(vertex.pos.x, vertex.pos.y, 10,0,2*Math.PI)
    //   ctx.fill();
    //   vertex.edges.map(edge => {
    //     const vertexPair = edge.destination;
    //     ctx.beginPath();
    //     ctx.moveTo(vertex.pos.x, vertex.pos.y);
    //     ctx.lineTo(vertexPair.pos.x, vertexPair.pos.y);
    //     ctx.stroke();
    //   })
   }


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
    this.state.graph.randomize(7,3.5,170, 0.6);
    this.state.graph.bfs(0);

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