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
    ctx.fillStyle = "black";
    // ctx.beginPath();// picking up your pen
    // ctx.arc(10,10,10,0,2 * Math.PI);

    // ctx.stroke() //put your pen down and draw the stroke
    // ctx.arc(100,100,10,0,2 * Math.PI);

    ctx.stroke();
    // console.log("This is g", g.vertexes);
    this.props.graph.vertexes.forEach((v,i) => {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fillStyle = "yellow";
      ctx.fill();
      let length = v.edges.length;
      for (let i = 0; length > i; i++) {
        ctx.fillStyle = 'white';
      ctx.beginPath();
        console.log("edge", v.edges[i].destination.pos);
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v.edges[i].destination.pos.x, v.edges[i].destination.pos.y);
        ctx.stroke();

      }
      console.log("vertexes", v.pos,v.edges.length);
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
    // console.log('ctx.arg', ctx.arc);

    // Clear it
    // ctx.fillStyle = 'red';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);


    // !!! IMPLEMENT ME
    // compute connected components

    // draw edges
    // ctx.fillStyle = 'white';
    // ctx.beginPath();
    // ctx.moveTo(0, 0);
    // ctx.lineTo(100, 500);
    // ctx.stroke();
    // draw verts

    // draw vert values (labels)
    // ctx.fillStyle = 'blue';
    // ctx.beginPath();
    // ctx.arc(250, 160, 30, 0, 2 * Math.PI);
    // ctx.fill();
    //<<< >>> <<< >>> <<< >>>
    // ctx.fillStyle = 'white';
    // ctx.beginPath();
    // ctx.moveTo(0, 0);
    // ctx.lineTo(200, 1200);
    // ctx.stroke();
    // //<<< >>> <<< >>> <<< >>>
    // ctx.fillStyle = 'white';
    // ctx.beginPath();
    // ctx.moveTo(0, 0);
    // ctx.lineTo(250, 700);
    // ctx.stroke();
    // //<<< >>> <<< >>> <<< >>>

    // ctx.font = "30px Arial";
    // ctx.strokeText("Hello Canvas", canvas.width / 3 + 60, canvas.height / 3);
    // //<<< >>> <<< >>> <<< >>>
    // ctx.font = "30px Comic Sans MS";
    // ctx.fillStyle = "yellow";
    // ctx.textAlign = "center";
    // ctx.fillText("Hello Canvas", canvas.width / 2, canvas.height / 2);
    // //<<< >>> <<< >>> <<< >>>
    // for (var i = 0; i < 6; i++) {
    //   for (var j = 0; j < 6; j++) {
    //     ctx.fillStyle = 'rgb(' + Math.floor(255 - 42.5 * i) + ',' +
    //       Math.floor(255 - 42.5 * j) + ',0)';
    //     ctx.fillRect(j * 25, i * 25, 50, 50);
    //   }
    // }
    // //<<< >>> <<< >>> <<< >>>
    // var grd = ctx.createRadialGradient(75, 50, 5, 90, 60, 700);
    // grd.addColorStop(0, "yellow");
    // grd.addColorStop(1, "white");

    // // Fill with gradient
    // ctx.fillStyle = grd;
    // ctx.fillRect(300, 10, 360, 80);


    // //<<< >>> <<< >>> <<< >>>
    // ctx.beginPath();
    // ctx.moveTo(100, 20);           // Create a starting point
    // ctx.lineTo(200, 20);          // Create a horizontal line
    // ctx.arcTo(250, 20, 250, 70, 50); // Create an arc
    // ctx.lineTo(250, 120);         // Continue with vertical line
    // ctx.stroke();
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
    // const g = new Graph();
    this.setState({graph: this.state.graph.randomize(5, 4, 150, 0.6)}) ;
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
