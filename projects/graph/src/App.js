import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const circleRad = 15;

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    console.log("GraphView CDM");
    this.updateCanvas();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    console.log("GraphView CDU");
    this.updateCanvas();
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    console.log("updateCanvas()\n");
    console.log("Canvas PROPS: ", this.props);
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
        
    // Clear it
    ctx.font = "13px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = "gray";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw vertices
    this.props.graph.vertexes.forEach((v) => {
      console.log("Vertex: ", v.value, v);
      ctx.beginPath();
      ctx.fillStyle = v.color;
      ctx.arc(v.pos.x, v.pos.y, circleRad, 0, 2*Math.PI);
      ctx.fill();
      
      // put text in vertex
      ctx.beginPath();
      ctx.fillStyle = "black";
      ctx.fillText(v.value, v.pos.x, v.pos.y);


      // draw edges between connected vertices
      if(v.edges.length > 0) {
        for(let i = 0; i < v.edges.length; i++) {
          ctx.beginPath();
          ctx.strokeStyle = v.color;
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(v.edges[i].destination.pos.x, v.edges[i].destination.pos.y);
          ctx.stroke();
        }
      }
    })
  }
  
  /**
   * Render
   */
  render() {
    console.log("GraphView Render");
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

    this.handleButton = () => {
      console.log("handleButton()");
      const graph = new Graph()
      graph.randomize(5, 4, 150, 0.6);
      // console.log("newGraph: ", graph);
      // this.setState({graph: new Graph ()});
      this.setState({graph: graph});
      // this.state.graph.randomize(5, 4, 150, 0.6);
      
      this.doBFS();
      console.log("new state: ", this.state.graph);
      // this.state.graph.randomize(5, 4, 150, 0.6);
      
    }

    this.doBFS = () => {
      console.log("doBFS()");
      for(let i = 0; i < this.state.graph.vertexes.length; i++) {
        if(this.state.graph.vertexes[i].color === 'white'){
          // color map all connected vertices
          console.log("doing bfs");
          this.state.graph.bfs(this.state.graph.vertexes[i]);
        }
      }
    }
    

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);
    console.log("Initial randomize complete.  Running Props: ", this.props);

    // search through the graph for any vertices that are not color mapped
    this.doBFS();
  }

  render() {
    console.log("App render");
    console.log("render state: ", this.state.graph);
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView><br/>
        <button onClick={() => this.handleButton()}>Re-Roll Graph</button>
      </div>
    );
  }
}

export default App;
