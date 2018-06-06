import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 800;
 const canvasHeight = 600;
// let dx = Math.random() + 4 * 1.1;
 let x = 5;
 let y = 4;
 let bxSize = 150;
 let probability = 0.6;
 //let dy = Math.random() + 4 * 1.1;
 const radius = 10;
 
 
 


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
  getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  

  updateCanvas() {

    const connectedComponents = this.props.graph.getConnectedComponents();

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;
    
    
    // Clear it
    ctx.fillStyle = 'rgb(0, 206, 209)';
    ctx.fillRect(20, 20, canvasWidth, canvasHeight);
   
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    
    //let vertexes = this.props.graph.vertexes;
    //ctx.strokeStyle = 'red';
    //ctx.arc(vertex1.pos.x, vertex1.pos.y, radius, 0, Math.PI * 2, false);
    //ctx.stroke();
    // draw vert values (labels)

    
    for( let conComponent of connectedComponents){

      for(let vertex of conComponent) {
        for (let edge of vertex.edges){
          ctx.strokeStyle = 'black';
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        }
      }

      for (let vertex of conComponent) {
          ctx.fillStyle = this.getRandomColor();
          ctx.beginPath();
          ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2 * Math.PI);
          ctx.fill();
          ctx.strokeStyle = 'black';
          ctx.stroke();
        
          ctx.fillStyle = this.getRandomColor();
          ctx.font = "11px Arial";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      }
    }
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
    this.state.graph.randomize(x, y, bxSize, probability);
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
