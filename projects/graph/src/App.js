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
    console.log('updating canvas');
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    // ctx.beginPath();
    // ctx.clearRect(0, 0, canvasWidth, canvasHeight);
    // ctx.stroke();
    // ctx.closePath();
    canvas.width = canvas.height;

    // this.props.graph.createDummyGraph();
    // Clear it
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.cont = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        ctx.closePath();
      }
    }

    this.props.graph.vertexes.forEach( v => {
      ctx.beginPath();
      ctx.fillStyle = v.color;
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();
      
      // fill in text
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
      ctx.closePath();
    });

    

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
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
      </div>
    );
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

  componentWillMount() {
    this.newGraph();
  }

  newGraph = () => {
    this.state.graph = new Graph();
    this.state.graph.randomize(5, 4, 160, 0.6);
    const components = this.state.graph.getConnectedComponents();
    const colors = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'purple', 'black', 'white', 'brown'];

    components.forEach( (component, i) => {
      for (let vertex of component) {
        vertex.color = colors[i];
      }
    });

    this.setState({ graph: this.state.graph });
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button className="btn" onClick={this.newGraph}>Refresh</button>
      </div>
    );
  }
}

export default App;
