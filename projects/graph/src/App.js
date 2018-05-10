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
      for (let i = 0; i < edges.length; i++) {
        if (!visited[edges[i].destination.value]) {
          const vertAX = vertex.pos.x;
          const vertAY = vertex.pos.y;
          const vertBX = edges[i].destination.pos.x;
          const vertBY = edges[i].destination.pos.y;
          ctx.beginPath();
          ctx.moveTo(vertAX, vertAY);
          ctx.lineTo(vertBX, vertBY);
          ctx.lineWidth = `${edges[i].weight}`
          ctx.strokeStyle = 'lightslategray';
          ctx.stroke();

          ctx.beginPath();
          ctx.lineWidth = '1';
          ctx.arc((vertAX + vertBX) / 2, (vertAY + vertBY) / 2, vertexRadius * 0.6, 0, 2 * Math.PI);
          ctx.fillStyle = 'lightyellow';
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = 'lightslategray';
          ctx.font = '7px Arial';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(edges[i].weight, (vertAX + vertBX) / 2, (vertAY + vertBY) / 2);
        }
      }
      visited[vertex.value] = 1;
    }

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2*Math.PI);
      ctx.fillStyle = vertex.color;
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
    this.state.graph.getConnectedComponents();
  }

  onButtonClick = () => {
    this.state.graph.randomize(5, 4, 150);
    this.state.graph.getConnectedComponents();
    this.setState({ graph: this.state.graph });
  }

  render() {
    return (
      <div className="App" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.onButtonClick} style={{ width: '100px' }}>REGEN</button>
      </div>
    );
  }
}

export default App;
