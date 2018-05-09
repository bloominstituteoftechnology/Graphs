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
    ctx.fillStyle = '#42d1f4';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // drawing edges and vertices
    this.props.graph.vertexes.map(vertex => {
     vertex.edges.map(edge => {
       //draw line from center of vertex to center of other vertex
       ctx.moveTo(vertex.pos.x, vertex.pos.y);
       ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
       ctx.stroke();
       return edge;
     });
     
    ctx.moveTo(vertex.pos.x, vertex.pos.y);
     ctx.arc(vertex.pos.x, vertex.pos.y, 15, 0, Math.PI*2);
     ctx.fillStyle = 'black';
     ctx.font = '13px Calibri';
     ctx.textAlign = 'center';
     ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y); 
     ctx.stroke();
     return vertex;
   });
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
    this.state.graph.getConnectedComponents();
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
