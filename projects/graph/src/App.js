import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 750;
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
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");

    // Clear it
    ctx.fillStyle = '#66ccff';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    console.log("update canvas:", this.props.graph);

    this.props.graph.vertexes.map(vertex => {
      vertex.edges.map(edge => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        return edge;
      });
      return vertex;
    });
    
    for(let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2*Math.PI);
      ctx.fillStyle = "#ff99cc";
      ctx.fill();
      ctx.strokeStyle = "black";
      ctx.stroke();

      ctx.fillStyle = "black";
      ctx.font = "10px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }


    




    //example for adding the vertex 
    // let debugVertex = this.props.graph.vertexes[0];
    // console.log('in updateCanvas', this.props.graph.vertexes);
    // ctx.arc(debugVertex.pos.x, debugVertex.pos.y, 20, 0, 2 * Math.PI)
    // ctx.stroke;

    //  ctx.moveTo(0, 0);
    //  ctx.lineTo(200, 100);
    //  ctx.stroke();
     
    //  ctx.moveTo(0, 0);
    //  ctx.lineTo(300, 200);
    //  ctx.stroke();
     
     
     
    //  ctx.moveTo(0, 0);
    //  ctx.lineTo(400, 300);
    //  ctx.stroke();

    //  ctx.moveTo(0, 0);
    //  ctx.lineTo(500, 400);
    //  ctx.stroke();


    
    
   



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
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
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
    this.state.graph.debugCreateTestData();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
