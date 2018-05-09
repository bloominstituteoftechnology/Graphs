import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

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
    ctx.fillStyle = 'blue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // console.log('hey', this.props.graphs.vertexes);
    // for (let vertex of this.props.graphs.vertexes) {
    //   ctx.beginPath();
    //   ctx.arc(vertex.pos.x, vertex.pos.y, 10, 0, 2 * Math.PI);
    //   ctx.fillStyle = 'green';
    //   ctx.fill();
    //   ctx.strokeStyle = 'black';
    //   ctx.stroke();
      
    //   ctx.fillStyle = 'black';
    //   ctx.font = '10px Arial';
    //   ctx.textAlign = 'center';
    //   ctx.textBaseLine = 'middle';
    //   ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    // }
   this.props.graph.vertexes.map(vertex => {

     vertex.edges.map(edge => {
       //draw line from center of vertex to center of other vertex
       ctx.moveTo(vertex.pos.x, vertex.pos.y);
       ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
       ctx.stroke();
     });
    //  ctx.arc(vertex.pos.x, vertex.pos.y, 5, 0, Math.PI*2);
   });

   for (let vertex of this.props.graph.vertexes){
    ctx.arc(vertex.pos.x, vertex.pos.y, 5, 0, Math.PI*2);
    ctx.stroke();   
   }

    
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
    this.state.graph.randomize(5,4,150);
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
