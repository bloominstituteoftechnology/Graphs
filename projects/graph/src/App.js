import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 700;
const canvasHeight = 480;
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
    ctx.fillStyle = '#FF0000';
    ctx.fillStyle = "lightgray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // console.log("this.props.graph", this.props.graph);

    // edges
    for (let parentVert of this.props.graph.vertexes) {
      for (let debugEdge of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(debugEdge.destination.pos.x, debugEdge.destination.pos.y);
        ctx.stroke();
      }
    }

    // nodes
    for (let node of this.props.graph.vertexes) {

      // fill
      ctx.moveTo(node.pos.x, node.pos.y);
      ctx.beginPath();
      ctx.arc(node.pos.x, node.pos.y, vertexRadius, 0, Math.PI * 2);
      ctx.stroke();

      // fill
      ctx.fillStyle = node.fillColor;
      ctx.fill();

      // label
      ctx.fillStyle = "black";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle"
      ctx.font = "10px Helvetica";
      ctx.fillText(node.value, node.pos.x, node.pos.y);
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
    // this.state.graph.bfs(this.state.graph.vertexes[0]);
    this.state.graph.randomize(3, 3, 100);
    this.state.graph.getConnectedComponents();
  }

  /**
  * Render Button
  */
  handleClick() {
    console.log("button clicked");
    this.setState({
      graph: new Graph()
    });
    console.log("graph", this.state.graph.randomize);
    this.state.graph.randomize(3, 3, 100);
    this.state.graph.getConnectedComponents();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.handleClick.bind(this)}>
          Reload
        </button>
      </div>
    );
  }
}

export default App;
