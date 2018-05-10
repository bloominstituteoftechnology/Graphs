import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const vr = 10;
const wr = 6;

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
    // compute connected components
    
    this.props.graph.getConnectedComponents();
    
    for (let vertex of this.props.graph.vertexes) {
      const px = vertex.pos.x;
      const py = vertex.pos.y;
      
      // draw edges
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.strokeStyle = vertex.color;
        ctx.stroke();
        
        const wpx = (px + edge.destination.pos.x) / 2;
        const wpy = (py + edge.destination.pos.y) / 2;
        
        // draw weights
        ctx.beginPath();
        ctx.arc(wpx, wpy, wr, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fillStyle = 'white';
        ctx.fill();
        
        //draw weight values
        ctx.fillStyle = 'black';
        ctx.font = '9px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(edge.weight, wpx, wpy);
        
      }
    }
    
    for (let vertex of this.props.graph.vertexes) {
      const px = vertex.pos.x;
      const py = vertex.pos.y;
      
      // draw verts
      ctx.beginPath();
      ctx.arc(px, py, vr, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fillStyle = vertex.color;
      ctx.fill();
      
      // draw vert values (labels)
      ctx.fillStyle = 'white';
      ctx.font = '11px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(vertex.value, px, py);
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
  }

  newGraph = () => {
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.getConnectedComponents();
    this.setState(this);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <br />
        <br />
        <button onClick={this.newGraph}>Generate New Graph</button>
      </div>
    );
  }
}

export default App;
