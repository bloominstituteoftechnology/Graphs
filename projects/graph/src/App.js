import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// const canvasWidth = 750;
// const canvasHeight = 600;
const canvasWidth = 400;
const canvasHeight = 400;
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
    let c = canvas.getContext('2d');
    
    c.fillStyle = 'white';
    c.fillRect(0, 0, canvasWidth, canvasHeight);
    // !!! IMPLEMENT ME
    
  let w = 50;
  let h = 50;
  let rot = .05;
  
    function Circle(x, y, dx, dy, rad, randomColor, RC2) {
      this.x = x;
      this.y = y;
      this.dx = dx;
      this.dy = dy;
      this.rad = rad;
      this.randomColor = randomColor;
      this.RC2 = RC2;
      
      this.draw = function() {
          c.beginPath();
          c.arc(this.x, this.y, this.rad,0, 2 * Math.PI);
          c.lineWidth = 5;
          // c.fill();
          c.stroke();
          // c.closePath();
      }
      this.update = function() {
          if (this.x + this.rad > canvasWidth || this.x - this.rad < 0) {
            (this.dx = -this.dx) && (c.strokeStyle=this.randomColor);
          }
          if (this.y + this.rad > canvasHeight || this.y - this.rad < 0) {
            (this.dy = -this.dy) // && (c.strokeStyle=this.randomColor);
          }
          this.x += this.dx;
          this.y += this.dy;
          this.draw();
      }
    }

    let circleArray = [];

    for(let i = 0; i < 3; i++) {
      let rad = 20
      let x = Math.random() * (canvasWidth - rad * 2) + rad;
      let y = Math.random() * (canvasHeight - rad * 2) + rad;
      let dx = (Math.random() - .5) * 10;
      let dy = (Math.random() - .5) * 10;
      let randomColor = ('rgb(' + parseInt(Math.random() * 255, 10)
              + ',' + parseInt(Math.random() * 255, 10) + ',' + parseInt(Math.random() * 255, 10) + ')');
      let RC2 = ('rgb(' + parseInt(Math.random() * 255, 10)
              + ',' + parseInt(Math.random() * 255, 10) + ',' + parseInt(Math.random() * 255, 10) + ')');

      circleArray.push(new Circle(x,y,dx,dy,rad,randomColor, RC2));
    }


      function animate() {
        requestAnimationFrame(animate);
        c.clearRect(0,0, canvasWidth, canvasHeight);
        for(let i = 0; i < circleArray.length; i++) {
          circleArray[i].update();
        }
      }
      function lineToAngle(c, x1, y1, length, angle) {

        angle *= Math.PI / 4;
    
        var x2 = x1 + length * Math.cos(angle),
            y2 = y1 + length * Math.sin(angle);
      
        c.moveTo(x1, y1);
        c.lineTo(x2, y2);
    
        return {x: x2, y: y2};
    }
    let length = 5; 
    let angle = 0;
    let dlt = .1;

      function rotate() {
        requestAnimationFrame(rotate)
        c.clearRect(0,0, canvasWidth, canvasHeight);

        c.beginPath();
        lineToAngle(c, x, y, length, angle);
        c.fillRect(0,0,canvasWidth,canvasHeight);
        c.lineWidth = 35;
        c.stroke();
        
    
        angle += dlt;
        // if (angle < -90) dlt = -dlt;
    }

      // animate();
      rotate();

    /*
    ctx.beginPath();
    ctx.arc(50, 50, 15, 0, 2 * Math.PI);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(300, 300, 15, 0, 2 * Math.PI);
    ctx.moveTo(300, 300);
    ctx.lineTo(50, 50);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(500, 150, 15, 0, 2 * Math.PI);
    ctx.moveTo(500, 150);
    ctx.lineTo(300, 300);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(20,100);
    ctx.lineTo(100, 100);

    ctx.moveTo(100,20);
    ctx.lineTo(100, 100);
    ctx.stroke();
    */

    // console.log("this.props.graph: ", this.props.graph);
    // this.props.graph.createDummyGraph();
    // console.log("call createDummyGraph: ");


    // ctx.font = '15px Arial';
    // ctx.textAlign = 'center';
    // ctx.textBaseline = 'middle';
 
    // for (let vertex of this.props.graph.vertexes) {
    //   for ( let edge of vertex.edges) {
    //     ctx.beginPath();
    //     ctx.moveTo(vertex.pos.x, vertex.pos.y);
    //     ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
    //     ctx.stroke();
    //   }
    // }

    // // this.props.graph.vertexes.forEach((v) => {
    //   for (let v of this.props.graph.vertexes) {
    //   ctx.beginPath();
    //   ctx.fillStyle = 'white';
    //   ctx.arc(v.pos.x, v.pos.y, 15, 0, 2 * Math.PI);
    //   ctx.fill();
    //   ctx.stroke();

    //   ctx.fillStyle = 'black';
    //   ctx.fillText(v.value, v.pos.x, v.pos.y);
    // }
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
    this.state.graph.randomize(5, 4, 150, 0.6);
    // this.state.graph.createDummyGraph();
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
