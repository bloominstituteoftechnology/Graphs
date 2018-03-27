import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 700;
const canvasHeight = 700;

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
    ctx.fillStyle = 'indigo';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw verts
    // draw edges
    // draw vert values (labels)

    ctx.strokeStyle = 'white';
    ctx.lineWidth = '3';
    const { vertices } = this.props.graph;
    for (let i=0; i<vertices.length; i++) {
      const {x,y} = vertices[i].pos;
      vertices[i].edges.forEach(edge => {
        const {x:x2, y:y2} = edge.destination.pos;
        ctx.beginPath();
        ctx.moveTo(x,y);
        ctx.lineTo(x2, y2);
        ctx.stroke();
      });
    }

    ctx.fillStyle = 'white';
    ctx.lineWidth = 5;
    ctx.strokeStyle = 'white';

    for (let i=0; i<vertices.length; i++) {
      const {x,y} = vertices[i].pos;
      ctx.beginPath();
      ctx.arc(x,y,20,0,2*Math.PI);
      ctx.fill();
      ctx.stroke();
    }
    

    ctx.fillStyle = 'indigo';
    ctx.font = '14pt Arial';
    ctx.textAlign = 'center';

    for (let i=0; i<vertices.length; i++) {
      const {x,y} = vertices[i].pos;
      ctx.beginPath();
      ctx.fillText(vertices[i].value, x, y);
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
    this.state.graph.randomize(5,4,150,0.6);
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
