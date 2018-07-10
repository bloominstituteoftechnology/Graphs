import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

let canvasWidth = 750;
let canvasHeight = 600;
const circleRadius = 25;

/* GraphView */
class GraphView extends Component {
  /* On mount */
  componentDidMount() {
    this.updateCanvas();
  }

  /* On state update */
  componentDidUpdate() {
    this.updateCanvas();
  }

  /* Render the canvas */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // dummy canvas
    // console.log("this.props.graph", this.props.graph);
    // this.props.graph.createDummyGraph();
    
    // Clear it
    ctx.fillStyle = 'gray';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
/*
    // draw dummy vertex
    ctx.font = "23px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    this.props.graph.vertexes.forEach(v => {
      // fill node (circle)
      ctx.beginPath();
      ctx.fillStyle = "white";
      ctx.arc(v.position.x, v.position.y, circleRadius, 0, Math.PI*2);
      ctx.stroke();
      ctx.fill();

      // fill text
      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.position.x, v.position.y);
    });
*/

    ctx.font = "23px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    this.props.graph.vertexes.forEach(v => {
      ctx.beginPath();
      ctx.fillStyle = "white";
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, Math.PI*2);
      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  }
  
  /* Render */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}


/* App */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph()
    };

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
