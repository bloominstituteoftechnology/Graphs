import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
const canvasHeight = 600;
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
   * see https://www.w3schools.com/graphics/canvas_intro.asp for tutorial
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.strokeStyle = "black"
    ctx.fillStyle = "lightgray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log(this.props.graph.vertexes);
    console.log("edge", this.props.graph.vertexes[0].edges[0]);

    //draw the edge
    for (let parentVert of this.props.graph.vertexes) {
      //let parentVert = this.props.graph.vertexes[0];
      //let debugEdge = this.props.graph.vertexes[0].edges[0];
      for (let debugEdge of parentVert.edges) {
        console.log("debug line is ", debugEdge);
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(debugEdge.destination.pos.x, debugEdge.destination.pos.y);
        ctx.stroke();
      }
      
    }

    // now that we have the vertex test data lets draw it
    //let debugNode = this.props.graph.vertexes[0];
    
    for  (let vertex of this.props.graph.vertexes ) {
      //draw circle
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fillStyle = "white";
      ctx.fill();

      // draw the label
      ctx.fillStyle = "black";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.font = "10px arial";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
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
    return <canvas ref="canvas" width={400} height={500}></canvas>;
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
    // we can use our test data here to see if it's working before 
    // using randomize 
    //this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5,4,150,0.6);
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
