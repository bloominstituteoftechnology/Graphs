import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750; 
const canvasHeight = 600;
let circleSize = 15;
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
    this.props.graph.randomize(5, 4, 150);
    ctx.fillStyle = 'lightgrey';
    ctx.fillRect(0,0, canvasWidth, canvasHeight);
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let vertex = this.props.graph.vertexes[i];
      for (let j = 0; j < vertex.edges.length; j++){
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(vertex.edges[j].destination.pos.x, vertex.edges[j].destination.pos.y);
        ctx.stroke();
      }

    }
    
    // const checkedVerts = new Array(this.props.graph.vertexes.length);
    // checkedVerts.fill(false);

    const checkedVerts = {};
    for (let i = 0; i < this.props.graph.vertexes.length; i++){
      checkedVerts[this.props.graph.vertexes[i].value] = false;
    }
    console.log(checkedVerts);
    const toBeChecked = [];

    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
    //for (let i = 0; i < 1; i++) {
      if (!checkedVerts[this.props.graph.vertexes[i].value]){
        let color = '#'+(Math.random()*0xFFFFFF<<0).toString(16);
        let currentNode = this.props.graph.vertexes[i];
        toBeChecked.push(currentNode);
        checkedVerts[currentNode.value] = true;
        let count = 0;
        while (toBeChecked.length > 0) {
          for (let j = 0; j < currentNode.edges.length; j++) {
            if (!checkedVerts[currentNode.edges[j].destination.value]) {
              checkedVerts[currentNode.edges[j].destination.value] = true;
              toBeChecked.push(currentNode.edges[j].destination);  
            }
          }
          let vertex = toBeChecked.shift();
          ctx.beginPath(vertex.pos.x, vertex.pos.y);
          ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2*Math.PI);
          ctx.fillStyle = color;
          ctx.fill();
          ctx.stroke();

          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.font = '15px Arial';
          ctx.fillStyle = 'black';
          ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
          currentNode = toBeChecked[0];
        }
      }
    }
    
    // My beautiful artwork below
    // ctx.fillStyle = 'lightgrey';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // ctx.fillStyle = 'goldenrod';
    // ctx.fillRect(100, 0, 100, 800);

    // ctx.fillRect(350, 0, 40, 800);

    // ctx.strokeStyle = 'red';
    // for (let i = 2; i < 1000; i+=8){
    //   ctx.beginPath();
    //   ctx.arc(i*i/2000,i*i/1000,50, 0, Math.PI * 2);
    //   ctx.stroke();
    // }

    // ctx.moveTo(4/2000, 4/1000);
    // ctx.lineTo(1000*1000/2000, 1000*1000/1000);
    // ctx.stroke();

    // for (let i = 0; i < 250; i+=.5) {
    //   ctx.strokeStyle = 'black';
    //   ctx.beginPath();
    //   ctx.arc(250,300,i, i, .75*Math.PI + i);
    //   ctx.stroke();
    // }
    // for (let i = 0; i < 150; i++) {
    //   ctx.strokeStyle = 'green';
    //   ctx.beginPath();
    //   ctx.arc(400,150,i, i*Math.PI, .75*Math.PI + i);
    //   ctx.stroke();
    // }
    // for (let i = 0; i < 100; i++) {
    //   ctx.strokeStyle = 'blue';
    //   ctx.beginPath();
    //   ctx.arc(100,650,i, i*Math.PI, .75*Math.PI + i);
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
  }

  reload() {
    console.log('clicked');
    window.location.reload();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={() => this.reload()}>Refresh</button>
      </div>
    );
  }
}

export default App;
