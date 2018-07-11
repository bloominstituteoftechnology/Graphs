import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750
const canvasHeight = 600

const circleRadius = 15


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

    // console.log('this.props.graph: ', this.props.graph); 
    // //call dummy funciton
    // this.props.graph.createDummyGraph(); 
    // console.log('called createDummyGraph'); 

    //clear it
    ctx.fillStyle= 'grey'; 
    ctx.fillRect(0, 0, canvasWidth, canvasHeight); 
//     ctx.font = '13px Arial';
//     ctx.textAlign = 'center';
//     ctx.textBaseline = 'middle';
    
//     // draw our dummy vertexes
//     this.props.graph.vertexes.forEach((v) => {
//       ctx.beginPath();
//       ctx.fillStyle = 'white';
//       ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
//       ctx.fill();
//       ctx.stroke();

//       // fill in the text
//       ctx.fillStyle = 'black';
//       ctx.fillText(v.value, v.pos.x, v.pos.y);
// });

   
  

  // !!! IMPLEMENT ME
  // compute connected components
  // draw edges
  // draw verts
  // draw vert values (labels)
  this.props.graph.getConnectedComponents(); //to access those that are connected

  for (let vertex of this.props.graph.vertexes) {
    const posX = vertex.pos.x;
    const posY = vertex.pos.y;

    for (let edge of vertex.edges) {
      ctx.beginPath();
      ctx.moveTo(posX, posY);
      ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
      ctx.strokeStyle = vertex.color; 
      ctx.stroke();
    }
  }

  for (let vertex of this.props.graph.vertexes) {
    const posX = vertex.pos.x;
    const posY = vertex.pos.y;

    ctx.beginPath();
    ctx.arc(posX, posY, circleRadius, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fillStyle = vertex.color;
    ctx.fill();

    ctx.fillStyle = 'white';
    ctx.font = '12px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(vertex.value, posX, posY);
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
