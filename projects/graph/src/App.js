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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw verts
    // draw edges
    // draw vert values (labels)

    ctx.lineWidth = '3';
    const { vertices } = this.props.graph;
    for (let i=0; i<vertices.length; i++) {
      const {x,y} = vertices[i].pos;
      vertices[i].edges.forEach(edge => {
        const {x:x2, y:y2} = edge.destination.pos;
        let r = Math.round(Math.random()*255);
        let g = Math.round(Math.random()*255);
        let b = Math.round(Math.random()*255);
        ctx.strokeStyle = `rgb(${r},${g},${b})`;
        ctx.beginPath();
        ctx.moveTo(x,y);
        ctx.lineTo(x2, y2);
        ctx.stroke();
      });
    }

    ctx.fillStyle = 'white';
    ctx.lineWidth = 5;
    ctx.strokeStyle = 'black';

    for (let i=0; i<vertices.length; i++) {
      const {x,y} = vertices[i].pos;
      ctx.beginPath();
      ctx.arc(x,y,20,0,2*Math.PI);
      ctx.fill();
      ctx.stroke();
    }
    

    ctx.fillStyle = 'black';
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

    this.newGraph = this.newGraph.bind(this);

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.setState({graph: this.state.graph.randomize(5,4,150,0.6)});
  }

  newGraph = () => {
    this.state.graph.randomize(5,4,150,0.6);
    this.updateCanvas();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button className="Button" onClick={this.newGraph}>New Graph</button>
      </div>
    );
  }
}

export default App;
