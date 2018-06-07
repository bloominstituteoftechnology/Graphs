import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

const circlesize = 15;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvas();
    // for (let v of this.props.graph.vertexes) {
      // this.props.graph.bfs(this.props.graph.vertexes[0]);
    // }
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

    console.log("updateCanvas: ", this.props.graph.vertexes);
    
    // Clear it
    ctx.fillStyle = 'cyan';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    for (let vertex of this.props.graph.vertexes) {
      ctx.lineWidth = .25;
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }
    
    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circlesize, 0, 2 * Math.PI);
      ctx.fillStyle = vertex.color;
      ctx.fill();

      ctx.fillStyle = 'black';
      ctx.stroke();
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '15px Ariel';
      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
  }

  // updateCanvasComponents() {
  //   const connectedComponents = this.props.graph.getConnectedComponents();

  //   for (let component of connectedComponents) {
  //     const clr = 'green';
  //     this.updateCanvas(clr);
  //   }
  // }
  
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
    this.newGraphHandler = this.newGraphHandler.bind(this);
    this.state = {
      graph: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    // this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5,4,150,0.6);

    this.state.graph.getConnectedComponents();
  }
  newGraphHandler() {
    const state = {graph : new Graph()};
    state.graph.randomize(5,4,150,0.6);
    this.setState(state);
    // this.state.graph.getConnectedComponents();
    this.forceUpdate();
  }

  render() {
    function refresh() {
      window.location.reload();
    }
    return (
      <div className="App">
        <button onClick={(this.newGraphHandler, refresh)}>New Graph</button>
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
