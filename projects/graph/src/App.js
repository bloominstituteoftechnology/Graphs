import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;

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
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;


    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'green';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.fillStyle = 'purple';

    ctx.fillRect(10, 10, 100, 100);

    ctx.fillStyle = 'blue';
    ctx.fillRect(60, 60, 300, 300);

    ctx.lineWidth = 5;



    //// line 
    ctx.beginPath();
    ctx.moveTo(80, 80);
    ctx.lineTo(499, 300);
    ctx.lineTo(450, 100);
    ctx.lineTo(20, 20);
    ctx.lineTo(20, 300)
    ctx.strokeStyle = "yellow"
    ctx.closePath();
    ctx.fill();
    ctx.stroke();


    //////////////////////////

    for (let i = 0; i < 100; i++) {

      let x = Math.random() * window.innerWidth;
      let y = Math.random() * window.innerHeight;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(900, 300);
      ctx.strokeStyle = "purple";
      ctx.closePath();
      ctx.stroke();
    }


    //////// arc 



    ctx.fillStyle = "white";
    ctx.font = "60px Helvetica";
    ctx.fillText("Hello Word", 300, 400);




    let bill = setInterval(function () {
      for (let i = 0; i < 20; i++) {
        let x = Math.random() * window.innerWidth;
        let y = Math.random() * window.innerHeight;
        ctx.beginPath();
        ctx.arc(x, y, 30, 0, Math.PI * 2, false);
        ctx.strokeStyle = "red";
        ctx.fillStyle = "teal"
        ctx.fill();
        ctx.stroke();

      }


    }, 1000)

    setInterval(function () {
      clearInterval(bill);
      ctx.fillStyle = "yellow";
      ctx.fillText("Bye Bye....", 300, 400)
      ctx.font = "200px Helvetica";
    }, 20000)








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
    return (<canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>);
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

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
