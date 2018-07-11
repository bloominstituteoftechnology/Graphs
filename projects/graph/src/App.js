import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;
const circleRadius = 15;

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
    // draw dummy vertex
    // ctx.fillStyle = "black";
    // ctx.beginPath();// picking up your pen
    // ctx.arc(10,10,10,0,2 * Math.PI);

    // ctx.stroke() //put your pen down and draw the stroke
    // ctx.arc(100,100,10,0,2 * Math.PI);

    ctx.stroke();
    // this.props.graph2.getConnectedComponents()
    
    function getRandomColor() {
      let letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
    const connectedComponents = new Graph();
    connectedComponents.getConnectedComponents();
    console.log("This is connectedComponents", connectedComponents);
    let clear = true;
    // for (let component of connectedComponents) {
    //   const curColor = getRandomColor();
    //   this.drawVerts(component, curColor, clear);
    //   clear = false;
    // }
    



    this.props.graph.vertexes.forEach((v,i) => {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fillStyle = "yellow";
      ctx.fill();
      let length = v.edges.length;
      for (let i = 0; length > i; i++) {
        // ctx.fillStyle = 'white';
      ctx.beginPath();
        // console.log("edge", v.edges[i].destination.pos);
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v.edges[i].destination.pos.x, v.edges[i].destination.pos.y);
        ctx.stroke();

      }
      // console.log("vertexes", v.pos,v.edges.length);
      ctx.font = '15px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle'
      ctx.fillStyle = 'black';
      // ctx.fillStyle = 'white';
      // ctx.beginPath();
      // ctx.moveTo(this.props.graph.vertexes[0].pos.x,this.props.graph.vertexes[0].pos.y);
      // ctx.lineTo(v.pos.x, v.pos.y);
      // ctx.stroke();
      ctx.fillText(v.value, v.pos.x, v.pos.y)
    });
    

  }
  drawVerts(vertexes, color, clear) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    ctx.fillStyle = 'gray';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    ctx.lineWidth = 1.5;
    ctx.strokeStyle = 'teal';

    // Draw the verts with lines
    for (let v of vertexes) {
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI, false);
      ctx.stroke();
    }

    // fill the verts
    for (let v of vertexes) {
      ctx.beginPath();
      ctx.fillStyle = 'black';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI, false);
      ctx.fill();
    }
    
    // Draw the vert names
    for (let v of vertexes) {
      ctx.beginPath();
      ctx.font = '14px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillStyle = 'white';
      ctx.fillText(v.value, v.pos.x, v.pos.y );
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
      graph: new Graph(),
      graph2: new Graph()
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    // const g = new Graph();

    this.setState({graph: this.state.graph.randomize(5, 4, 150, 0.6)}) ;
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} graph2={this.state.graph2}></GraphView>
      </div>
    );
  }
}

export default App;
