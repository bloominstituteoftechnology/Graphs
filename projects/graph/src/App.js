import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = window.innerWidth;
const canvasHeight = window.innerHeight - 8;

/**
 * GraphView
 */
class GraphView extends Component {
  constructor(props) {
    super();
    this.graph = new Graph(canvasWidth, canvasHeight);
    this.graph.randomize(8, 8);
    this.connected = this.graph.bfs(this.graph.vertexes[0]);
    this.graph.dump();
    console.log("#No. of Verts: " + this.connected.length);

  }
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
  
  randomHEX() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
  }

  randomRGB() {
    return `rgb(${((Math.random() * 255) + 1) | 0}, ${((Math.random() * 255) + 1) | 0}, ${((Math.random() * 255) + 1) | 0}`;
  }

  randomRGBA(r, g, b, a) {
    return `rgba(${!!r ? r : ((Math.random() * 255) + 1) | 0}, ${!!g ? g : ((Math.random() * 255) + 1) | 0}, ${!!b ? b : ((Math.random() * 255) + 1) | 0}, ${!!a ? a : Math.random().toFixed(2) }`;
  }


  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = document.getElementById('LS');//this.ref.canvas;       
    let c = canvas.getContext('2d');
    
    // Clear it
    c.fillStyle = '#112';
    c.fillRect(0, 0, canvasWidth, canvasHeight);

    // const root = this.props.graph.vertexes;
    // console.log(root.pos);
    // console.log(root);
    let x = 0;
    let y = 0;

    for (let j = 0; j < this.connected.length; j++) {

      x = this.connected[j].pos.x; 
      y = this.connected[j].pos.y; // this.connected[j].pos.y * 

      c.beginPath();
      c.arc(x, y, 40, 0, Math.PI * 2);
      c.closePath();
      c.fillStyle = this.randomRGBA(0,0,0,0.2);
      c.fill();

      this.connected[j].edges.forEach(edge => {
        c.moveTo(x, y);
        c.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        c.strokeStyle = c.fillStyle;
        c.closePath();
        c.stroke();
      });

      c.font = "10px Arial";
      c.strokeStyle = 'black';
      c.textAlign = "center";
      c.textBaseline = "middle";
      c.moveTo(x, y);
      c.beginPath();
      c.strokeText(this.connected[j].value, x, y);
      c.stroke(); 

    }
  }
  
  /**
   * Render
   */
  render() {
    return <canvas id="LS" ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}


/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = { graph: new Graph() };
  }

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    componentDidMount() {
      this.state.graph = this.state.graph.randomize(2, 2);
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
