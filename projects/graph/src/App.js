import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 700;
const canvasHeight = 500;
const vertexRadius = 20;

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
    ctx.fillStyle = 'lightblue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    /* ctx.fillStyle = "Black";
    ctx.font = "10px Arial";
    ctx.fillText("Hello Word",10,50); */
    ctx.textAlign = "center";


    //console.log('in update canvas, vertex data is: ', this.props.graph )
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        //console.log('vertext names', vertex.value); 
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        //ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
        ctx.fillStyle = 'white';
        ctx.fill();
        ctx.stroke();
      }
      
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0,2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.strokeStyle = 'blue';
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.font = "10px Arial";
      ctx.textBaseline = "middle";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y)
    }
  }


  // !!! IMPLEMENT ME
  // compute connected components
  // draw edges
  // draw verts
  // draw vert values (labels)


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
    this.state.graph.randomize(3,4,120,.7);
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
