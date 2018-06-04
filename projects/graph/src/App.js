import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1905;
const canvasHeight = 1015;

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
    ctx.fillStyle = '#222222';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)


    ctx.strokeStyle = 'red';

    for(let i = 0; i < 35; i ++){
      ctx.strokeStyle = 'rgb(255' + ',' + (225) + ', ' + (250) + ',' + 1000 + ')';
    
    ctx.beginPath();
    ctx.arc(949.95, 400, 1535 - i * 45, 0, 2 * Math.PI);
    ctx.stroke();

    }

    ctx.strokeStyle = 'white';
    ctx.fillStyle = '#C8C8C8';
    ctx.beginPath();
    ctx.arc(1700, 900, 500, 0, Math.PI * 2);
    ctx.stroke();
    ctx.fill();

    for(let i = 0; i < .5; i++){
     for(let j=0; j < 270; j++){


      ctx.strokeStyle = 'rgb(230, ' + Math.ceil(55 + i / 10) + ', ' + 
      Math.ceil(255 - j / 1) + ')';
      ctx.beginPath();
      ctx.arc(949.95, 400 , 1360 - j * 5, 50, Math.PI * 1, true);
      ctx.stroke();


    //   ctx.beginPath();
    //   let x = j * 20;
    //   let y = 8.5 * j;
    //   let radius = 70;
    //   let startAngle = 350;
    //   // let endAngle = Math.PI + (Math.PI * j) / 2;
    //   let endAngle = 25;
    //   // var anticlockwise = i % 2 !== 0;

    //   ctx.arc(x, y, radius, startAngle, endAngle);{

      
    //     ctx.stroke();
    //  }



      // ctx.beginPath();
      // let x = j * 20;
      // let y = 8.5 * j;
      // let radius = 20;
      // let startAngle = 0;
      // let endAngle = Math.PI + (Math.PI * j) / 2;
      // var anticlockwise = i % 2 !== 0;

      // ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise);

      // if (i > 1) {
      //   ctx.fill();
      // } else {
      //   ctx.stroke();
      // }

      }



    }

    
    for(let i = 0; i < 5000; i++){
      ctx.strokeStyle = 'red';
      ctx.moveTo(1200, 1200);
      ctx.lineTo(20 * i, 0);
      ctx.closePath();
      ctx.stroke();
      // for(let j = 0; j < 3000; j++){
      //   ctx.strokeStyle = 'rgb(80, 20, 225)';
      //   ctx.moveTo(500, 1200);
      //   ctx.lineTo(200 * j, 0);
      //   ctx.radius = 1000;
      //   ctx.stroke();
      //   }
      
      }

    for(let i = 0; i < 5000; i++){
      

      ctx.strokeStyle = 'rgb(' + Math.floor(255 - i)  + ',' + (255 - 5 * i) + ',' + 15 + ')';
      ctx.moveTo(30, 1200);
      ctx.lineTo(45 * i, 0);
      ctx.closePath();
      ctx.stroke();
      
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
