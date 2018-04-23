import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';
import './graph';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
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
    ctx.fillStyle = "grey";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight); // (x, y, width, height) origin -- top left
//     ctx.moveTo(0,0);
//     ctx.lineTo(200,100);
//     ctx.moveTo(200,100);
//     ctx.lineTo(130,480);
//     ctx.lineTo(320,75);
//     ctx.stroke();
//
//     ctx.beginPath();
//     ctx.arc(95,50,40,0,2*Math.PI);
//     ctx.stroke();
//
//     // Create gradient
//     var grd=ctx.createLinearGradient(300,300,150,0);
//     grd.addColorStop(0,"red");
//     grd.addColorStop(1,"white");
//
// // Fill with gradient
//     ctx.fillStyle=grd;
//     ctx.fillRect(300,100,150,80);
//
//     for(var i = 0; i < 300; i++) {
//       ctx.moveTo(2*i, 20);
//       ctx.lineTo(3*i, 250);
//       let r = i+100;
//       let g = 30*i*i;
//       let b = i * 10;
//       ctx.strokeStyle= `rgb(${r},${g},${b})`;
//       ctx.stroke();
//     }
//     ctx.beginPath();
//     ctx.arc(95,50,40,0,2*Math.PI);
//     ctx.lineTo(200, 150);
//     for (let i = 0; i < canvasWidth; i++) {
//       ctx.lineTo(22 * i, 50);
//       ctx.lineTo(1000 / i, 500);
//       let r = Math.floor(Math.random() * 8) * i + 50;
//       let g = Math.floor((Math.random() * 2)) * i;
//       let b = Math.floor(Math.random() * i);
//       ctx.strokeStyle = `rgb(${r}, ${g}, ${b})`;
//       ctx.stroke();
//     }

    // test
    console.log("updating canvas");
    console.log(this.props.graph.vertexes);

    console.log("edge", this.props.graph.vertexes[0].edges[0]);
    // REMEMBER: Draw lines first!
    //let parentVert = this.props.graph.vertexes[0];
    //let debugEdge = this.props.graph.vertexes[0].edges[0];
    for (let vertex of this.props.graph.vertexes)
    {
      for (let edge of vertex.edges)
      {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }
    //we know our data is here :D
    // let's draw it!

    //var debugNode = this.props.graph.vertexes[0];
    // iterate over vertex array to draw them
    for (let vertex of this.props.graph.vertexes)
    {
      // draw the circle
      ctx.moveTo(vertex.pos.x,  vertex.pos.y);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, Math.PI * 2);
      ctx.stroke();

      // fill node white
      ctx.fillStyle = "white";
      ctx.fill();
      //draw text on screen
      ctx.font = "10px Arial"; // TODO: Do we want stroke
      ctx.fillStyle = "black";
      ctx.textBaseline = "middle";
      ctx.textAlign = "center";
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
    this.randomizeGraph = this.randomizeGraph.bind(this);
    this.state.graph.randomize(5, 4, 150, 0.6);
    // this.state.graph.debugCreateTestData();
  }

  randomizeGraph() {
    const newGraph = new Graph();
    newGraph.randomize(5, 4, 150, 0.6);
    this.setState({graph: newGraph});
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
