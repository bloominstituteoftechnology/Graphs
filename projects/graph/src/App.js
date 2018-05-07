import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

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
    ctx.fillStyle = 'lavender';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const vertexes = this.props.graph.vertexes;
    const radius = 10;

    let labels = [];

    for(let vertex in vertexes) {
      for(let edge of vertexes[vertex].edges) {
        ctx.beginPath();
        ctx.moveTo(vertexes[vertex].pos.x, vertexes[vertex].pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.strokeStyle = vertexes[vertex].color;
        ctx.stroke();

        let xaxis = (vertexes[vertex].pos.x + edge.destination.pos.x)/2;
        let yaxis = (vertexes[vertex].pos.y + edge.destination.pos.y)/2;

        // ctx.font = "50 px Arial";
        ctx.fillStyle = "black";
        ctx.textAlign = "end";
        let randomNum = Math.floor(Math.random() * 10)

        if (!labels.includes(xaxis+yaxis)) {
          ctx.fillText(randomNum, xaxis, yaxis);
          labels.push(xaxis + yaxis);
        }
      }
    }


    for(let vertex in vertexes) {

      ctx.beginPath();
      ctx.arc(vertexes[vertex].pos.x, vertexes[vertex].pos.y, radius, 0, 2*Math.PI);
      ctx.fillStyle = vertexes[vertex].color;
      ctx.fill();
      ctx.stroke();
      
      
      ctx.font = "30 px Arial";
      ctx.fillStyle = "black";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(vertexes[vertex].value, vertexes[vertex].pos.x, vertexes[vertex].pos.y);
    }

    // ctx.font = "30px Arial";
    // ctx.strokeText("CD/DVD",10,50);
    // ctx.beginPath();
    // for(let i = 0; i < 150; i++) {
    //   // ctx.fillStyle = getRndColor();
    //   ctx.arc(350,300,i+50,0,2*Math.PI);
    //   ctx.fill();
    //   ctx.closePath();
    // }
    // ctx.stroke();

  }

  vert = (event) => {
    // let xaxis = event.screenX;
    // console.log(xaxis);
    // let yaxis = event.screenY;
    // console.log(yaxis);
    // this.props.graph.vertexes.forEach(vert => {
    //   let posx = vert.pos.x;
    //   console.log(posx);
    //   let posy = vert.pos.y;
    //   if (xaxis >= (posx - 10) && xaxis <= (posx + 10)) {
    //     if (yaxis >= (posy - 10) && yaxis <= (posy + 10)) {
    //       console.log(vert);
    //     }
    //   }
      
    // });
  }
  
  /**
   * Render
   */
  render() {
  return (
    <div>
      <canvas ref="canvas" width={canvasWidth} height={canvasHeight} onClick={this.vert}></canvas>
    </div>
  );
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
    this.state.graph.randomize(5,4,150,0.6);
    this.state.graph.getConnectedComponents();
  }
  

  newGraph = () => {
    this.state.graph.randomize(5,4,150,0.6);
    this.state.graph.getConnectedComponents();
    this.setState(this);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <br />
        <button onClick={this.newGraph}>New Graph</button>
      </div>
    );
  }
}

export default App;
