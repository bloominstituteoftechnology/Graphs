import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
// const canvasWidth = 
// const canvasHeight = 
const canvasWidth = window.innerHeight;
const canvasHeight = window.innerWidth;
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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    // !!! IMPLEMENT ME
    
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    for (let parentVert of this.props.graph.vertexes){
      for (let parentEdges of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(parentEdges.destination.pos.x, parentEdges.destination.pos.y);    
        ctx.stroke();
      }
    }

    for (const parentVert of this.props.graph.vertexes) {
      ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
      ctx.beginPath();
      ctx.arc(parentVert.pos.x, parentVert.pos.y, vertexRadius, 0, 2*Math.PI);  
      ctx.stroke();
      ctx.fillStyle = parentVert.fillColor;
      ctx.fill();
      ctx.font = "12px Arial";
      ctx.fillStyle = "black"
      ctx.textBaseline = "middle";
      ctx.textAlign = "center"
      ctx.fillText(parentVert.value, parentVert.pos.x, parentVert.pos.y);
     
    }
  }
//     let matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()";
    
    

//     let font_size = 10;
//     let columns = canvasWidth/font_size; 
//     let drops = [];


//     for( let x = 0; x < columns; x++)
//       drops[x] = 1;


//     function draw() {
//     ctx.fillStyle = "rgba(0, 0, 0, 0.04)"; 
//     ctx.fillRect(0, 0, canvasWidth, canvasHeight); 

//     ctx.fillStyle = "#0F0"; 
//     ctx.font = font_size + "px arial";


//     for(let i = 0; i < drops.length; i++) {
//     let text = matrix[Math.floor(Math.random()*matrix.length)]; 
//     ctx.fillText(text, i*font_size, drops[i]*font_size); 


//     if(drops[i]*font_size > canvasHeight && Math.random() > 0.975)
//         drops[i] = 0;
//     drops[i]++; 
//     }
// }

// setInterval(draw, 35);
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
    this.state.graph.randomize(3, 3, 80, .45);
    let ans = this.state.graph.dfs(this.state.graph.vertexes[0]);
    if (ans.length < this.state.graph.vertexes.length) {
      for (let vertex of this.state.graph.vertexes) {
        if (vertex.fillColor === "white") {
          ans = this.state.graph.dfs(vertex);
        }
      }
    }

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
