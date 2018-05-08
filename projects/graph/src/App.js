import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 10;

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
    let grd = ctx.createLinearGradient(canvasWidth / 2, 0, canvasWidth / 2, canvasHeight);
    grd.addColorStop(0, "lightyellow");
    grd.addColorStop(1, "skyblue");
    
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);


    let visited = {};
    for (let vertex of this.props.graph.vertexes) {
      const edges = vertex.edges;
      console.log('vertex is', vertex);
      for (let i = 0; i < edges.length; i++) {
        if (!visited[edges[i].destination.value]) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edges[i].destination.pos.x, edges[i].destination.pos.y);
          ctx.strokeStyle = 'lightslategray';
          ctx.stroke();
        }
      }
      visited[vertex.value] = 1;
    }

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2*Math.PI);
      ctx.fillStyle = 'gold';
      ctx.fill();
      ctx.strokeStyle= 'dodgerblue'; // TODO: Optimize this code. Many calls for stroke and fill
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.font = "10px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
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
    // this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5, 4, 150);
  }

  onButtonClick = () => {
    this.state.graph.randomize(5, 4, 150);
    this.setState({ graph: this.state.graph });
  }

  render() {
    return (
      <div className="App">
        <button onClick={this.onButtonClick}>REGEN</button>
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
