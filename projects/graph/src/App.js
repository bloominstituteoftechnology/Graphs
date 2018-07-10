import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
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
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    const graph = this.props.graph;
    graph.randomize(5, 4, 150, 0.6);

    // DUMMY GRAPH--------------------------------------------
    // console.log('this.props.graph: ', this.props.graph);
    // //call our dummy function
    // this.props.graph.createDummyGraph();
    // console.log('called createDummyGraph');
    // DUMMY GRAPH--------------------------------------------

    // Clear it
    ctx.fillStyle = '#000066';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        ctx.fillText(edge.weight, (vertex.pos.x + edge.destination.pos.x) / 2, (vertex.pos.y + edge.destination.pos.y) / 2);
      }
    }

    // draw our dummy vertex
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = 'black';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      // ctx.lineCap="square";
      // // ctx.moveTo(200, 20);
      // ctx.lineTo(300, 20);
      ctx.fill();
      ctx.stroke();

      // fill in the text
      ctx.fillStyle = 'white';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });

    // ctx.arc(10, 10, 10, 0, 2 * Math.PI); //deciding what to draw next
    // ctx.stroke();//put your pen down and draw the stroke
    // ctx.beginPath();
    // ctx.arc(100, 100, 10, 0, 2 * Math.PI);
    // ctx.stroke();
    // console.log('called ctx.arc');
//-----------------------------------------------------
    // ctx.fillStyle = 'red'; // HAT 1
    // ctx.fillRect(200, 10, 20, 20);    

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
