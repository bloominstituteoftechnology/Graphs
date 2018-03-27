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
    ctx.strokeStyle = "black";
    ctx.fillStyle = 'lightgray';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log("Updating Canvas");
    console.log(this.props.graph.vertexes);

    console.log("edge", this.props.graoh.vertexes[0], edges[0]);


    // remember to draw lines
    for (let parentVert of this.props.graph.vertexes)
    {
    for (let debugEdge of parentVert.edges)
    {
    ctx.moveTo(debugNode.pos.x, debugNode.pos.y);
    ctx.beginPath();
    ctx.arc(debugNode.pos.x, debugNode.pos.y, vertexRadius, 0, Math.PI * 2);
    ctx.stroke();
    // !!! IMPLEMENT ME;
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    //draw the fill
    ctx.fillStyle = "white";
    ctx.fill();

    //Draw the label
    ctx.fillstyle = "black";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.font = "10px Arial";
    ctx.fillText(debugNode.value, debugNode.pos.x, debugNode.pos.y);
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

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
