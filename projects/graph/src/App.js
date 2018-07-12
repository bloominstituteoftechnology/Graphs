import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 900;
const canvasHeight = 800;
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

    // debugging:
   //  console.log('this.props.graph: ', this.props.graph)

    // this.props.graph.createDummyGraph();
    // console.log('called createDummyGraph');
    
    // randomize method call
    this.props.graph.randomize(6, 5, 150, 0.6);
    
    // debugging:
    // console.log(this.props.graph.vertexes);
    
    // Clear it
    ctx.fillStyle = '#c0dfe8';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '14px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // draw dummy vertexes


    this.props.graph.vertexes.forEach(v => {
      // console.log("each vertex: ", v);
      // console.log("edge adress x ", v.edges[0].destination.pos.x);
      // console.log("edge adress y ", v.edges[0].destination.pos.y);

      // line to next vertex
      for (let edge of v.edges) {
        if (edge.destination.pos.x) {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        }
        
      }

    });

    this.props.graph.vertexes.forEach(v => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, (Math.PI * 2));
      ctx.fill();
      ctx.stroke();

      // fill the text

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });

    const toColor = [];
    this.props.graph.vertexes.forEach(v => {
      toColor.push(this.props.graph.bfs(v));
    });

    console.log(toColor)
    
   

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
