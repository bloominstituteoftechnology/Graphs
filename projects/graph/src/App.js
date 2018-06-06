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
    
    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    console.log('in updateCanvas', this.props.graph.vertexes);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';
    
    this.props.graph.vertexes.forEach(vertex => {
      if (vertex.edges.length > 0) {
        console.log("Edges: ", vertex.edges);
        vertex.edges.forEach(edge => {
          ctx.beginPath();
          ctx.lineWidth = 2.5;
          ctx.strokeStyle = 'rgb(0, 172, 174)';
          ctx.moveTo(edge.origin.x, edge.origin.y);
          ctx.lineTo(edge.destination.x, edge.destination.y);
          ctx.stroke();
        });
      }
      
    });

    this.props.graph.vertexes.forEach(vertex => {

      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 15, 0, 2 * Math.PI)
      ctx.fillStyle = 'rgb(0, 206, 209)';
      ctx.fill();
      ctx.strokeStyle = 'rgb(0, 172, 174)';
      ctx.stroke();
      ctx.fillStyle = 'white';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    });
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
    // this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5, 4, 125, 0.6);
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
