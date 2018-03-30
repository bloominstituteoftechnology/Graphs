import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 25;

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
    const colors = ["black", "green", "blue", "red", "yellow", "purple", "teal", "SteelBlue", "SpringGreen", "RebeccaPurple"];
    const fillColors = ["Beige", "AliceBlue", "Lavender", "Linen", "MistyRose", "PowderBlue", "Thistle","SandyBrown","Salmon","SaddleBrown"];
    ctx.strokeStyle =`${colors[Math.floor( Math.random() * 10 )]}`;
    ctx.lineWidth = 10;
    ctx.fillStyle = "lightgrey";
    ctx.fillRect(0,0, canvasWidth, canvasHeight);
   
    for (let parentVert of this.props.graph.vertexes) {
      for(let debugEdge of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(debugEdge.destination.pos.x, debugEdge.destination.pos.y);
        ctx.stroke();
      }
    }
   

    for(let vertex of this.props.graph.vertexes) {
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, Math.PI * 2);
      ctx.stroke();
      
      ctx.fillStyle = `${fillColors[Math.floor( Math.random() * 10 )]}`;
      ctx.fill();
    //draw lable
      ctx.fillStyle = "Black";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.font = "20px Comic Sans MS";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
    // Clear it
  }
  
  /**
   * Render
   */
  render() {
    return <div>
            <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
            
            </div>;
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
    this.updateGraph = this.updateGraph.bind(this);
    // !!! IMPLEMENT ME
    // use the graph randomize() method
    
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.bfs(this.state.graph.vertexes[0])
  }
  updateGraph() {
    const newState = {
      graph: new Graph()
    }
    newState.graph.randomize(5, 4, 150, 0.6);
    this.setState(newState);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.updateGraph}>New Graph</button>
      </div>
    );
  }
}

export default App;



