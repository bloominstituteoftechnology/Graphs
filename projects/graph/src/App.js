import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

const g = new Graph();

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    console.log('from graph view graph', this.props.graph);
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
    ctx.fillStyle = 'gray';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //draw circle
    for(let v of this.props.graph.vertexes){
      const vx = v.pos.x;
      const vy = v.pos.y;
      ctx.fillStyle="yellow";
      ctx.beginPath();
      ctx.arc(vx, vy, 15, 0, 2*Math.PI);
      ctx.stroke();
      ctx.fill();

      ctx.font = "13px Comic Sans MS";
      ctx.fillStyle = "blue";
      ctx.textAlign= "center";
      ctx.textBaseline="middle";
      ctx.fillText(v.value, vx, vy);
      for(let e of v.edges){
        //draw line
        const dx = e.destination.pos.x;
        const dy = e.destination.pos.y;
        ctx.moveTo(vx, vy);
        ctx.lineTo(dx, dy);
        ctx.stroke();
      }
     }

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
    console.log('this state random graph', this.state.graph.vertexes);
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
