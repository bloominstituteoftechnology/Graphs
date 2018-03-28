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
   
    // console.log(this.props.graph.vertexes[0].edges)

    // let parentVert = this.props.graph.vertexes[0];
    // let debugEdge = this.props.graph.vertexes[0].edges[0];
    for (let parentVert of this.props.graph.vertexes) {
      for(let debugEdge of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(debugEdge.destination.pos.x, debugEdge.destination.pos.y);
        ctx.stroke();
      }
    }
   

    // var debugNode = this.props.graph.vertexes[0]
    // console.log(debugNode.pos.x)
    // ctx.moveTo(debugNode.pos.x, debugNode.pos.y);
    // ctx.beginPath();
    // ctx.arc(debugNode.pos.x, debugNode.pos.y, vertexRadius, 0, Math.PI * 2);
    // ctx.stroke();
    
    // //draw lable
    // ctx.font = "10px Arial";
    // ctx.fillStyle = "black";
    // ctx.textAlign = "center";
    // ctx.textBaseline = "middle";
    // ctx.fillText(debugNode.value, debugNode.pos.x, debugNode.pos.y);
    // function RandColor(colors) {
      
    // }
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
    // ctx.moveTo(80,80);
    // for (var i = 0; i < 100; i++) {
    //   for (var j = 0; j < 100; j++) {
    //     for (var p = 0; p < 100; p++) {
    //     ctx.fillStyle = `rgb(${Math.floor(255 - 10.5 * i)}, ${Math.floor(255 - 10.5 * j)}, ${Math.floor(255 - 10.5 * p)})`;
    //     ctx.fillRect(j * 25, i * 25, 25, 25);
    //     }
    //   }
    // }
    // for (var i = 0; i < 20; i++) {
    //   if (ctx.lineWidth > 10) {
    //     ctx.lineWidth = 1;
    //   } else {
    //     ctx.lineWidth = 1 + i;
    //   }
    //   ctx.beginPath();
    //   ctx.moveTo(1 + i + 20, i + 1);
    //   ctx.lineTo(1 + i * 80, 500);
    //   ctx.stroke();
    // }
    
  


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
    // console.log(this.state.graph)
    this.state.graph.randomize(100, 12, 50, 0.6);
    // this.state.graph.debugCreateTestData();
   
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


//BSF()
