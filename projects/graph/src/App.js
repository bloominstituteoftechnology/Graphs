import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
let canvasWidth = 750;
let canvasHeight = 600;
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
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');
    this.props.graph.randomize(5, 4, 150, 0.6);
    
    console.log('this.props.graph: ', this.props.graph);
    // call the dummy graph function to test
    this.props.graph.createDummyGraph();
    console.log('called dummy graph'); 

    // Base Layer
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '13px Arial';
    ctx.textAlign = 'center'; 
    ctx.textBaseline = 'middle'; 

    // ---- Canvas Practice Phase 1 day 2 -----
    // draw dummy vertex 1
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.lineCap='square';
      // ctx.lineTo(100,50); 
      ctx.fill();
      ctx.stroke();
      
      // fill in the text
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);

      // iterate over the vertecies and connect the edges with lines
      if(v.edges.length >= 0) {
        for(let i = 0; i < v.edges.length; i++) {
          ctx.beginPath(); // start path
          ctx.moveTo(v.pos.x, v.pos.y); // move position 
          ctx.lineTo(v.edges[i].destination.pos.x, v.edges[i].destination.pos.y); // draw connecting line 
          ctx.strokeStyle = 'black';
          ctx.stroke();
        }
      }
    })

    // draw dummy graph:
    // ctx.arc(10, 10, 10, 0, 2 * Math.PI); // define an arc path
    // ctx.stroke(); // follow the path and draw it
    // ctx.beginPath(); // begin new path
    // ctx.arc(100, 100, 10, 0, 2 * Math.PI); // define an arc path
    // ctx.stroke();

    // ---- Canvas Practice Phase 2 day 1 -----
    // ctx.fillStyle = 'white';
    // ctx.fillRect(80, 80, 340, 340);

    // ctx.fillStyle = 'grey';
    // ctx.fillRect(150, 150, 200, 200);

    // Top Left
    // ctx.fillStyle = 'red';
    // ctx.fillRect(0, 0, 70, 70);

    // ctx.fillStyle = 'orange';
    // ctx.fillRect(0, 0, 60, 60);

    // ctx.fillStyle = 'yellow';
    // ctx.fillRect(0, 0, 50, 50);

    // ctx.fillStyle = 'green';
    // ctx.fillRect(0, 0, 40, 40);

    // ctx.fillStyle = 'blue';
    // ctx.fillRect(0, 0, 30, 30);

    // ctx.fillStyle = 'indigo';
    // ctx.fillRect(0, 0, 20, 20);

    // ctx.fillStyle = 'violet';
    // ctx.fillRect(0, 0, 10, 10);

    // Top Right
    // ctx.fillStyle = 'red';
    // ctx.fillRect(430, 0, 70, 70);

    // ctx.fillStyle = 'orange';
    // ctx.fillRect(440, 0, 60, 60);

    // ctx.fillStyle = 'yellow';
    // ctx.fillRect(450, 0, 50, 50);

    // ctx.fillStyle = 'green';
    // ctx.fillRect(460, 0, 40, 40);

    // ctx.fillStyle = 'blue';
    // ctx.fillRect(470, 0, 30, 30);

    // ctx.fillStyle = 'indigo';
    // ctx.fillRect(480, 0, 20, 20);

    // ctx.fillStyle = 'violet';
    // ctx.fillRect(490, 0, 10, 10);
    
    // // Bottom Left
    // ctx.fillStyle = 'red';
    // ctx.fillRect(0, 430, 70, 70);

    // ctx.fillStyle = 'orange';
    // ctx.fillRect(0, 440, 60, 60);

    // ctx.fillStyle = 'yellow';
    // ctx.fillRect(0, 450, 50, 50);

    // ctx.fillStyle = 'green';
    // ctx.fillRect(0, 460, 40, 40);

    // ctx.fillStyle = 'blue';
    // ctx.fillRect(0, 470, 30, 30);

    // ctx.fillStyle = 'indigo';
    // ctx.fillRect(0, 480, 20, 20);

    // ctx.fillStyle = 'violet';
    // ctx.fillRect(0, 490, 10, 10);

    // // Bottom Right
    // ctx.fillStyle = 'red';
    // ctx.fillRect(430, 430, 70, 70);

    // ctx.fillStyle = 'orange';
    // ctx.fillRect(440, 440, 60, 60);

    // ctx.fillStyle = 'yellow';
    // ctx.fillRect(450, 450, 50, 50);

    // ctx.fillStyle = 'green';
    // ctx.fillRect(460, 460, 40, 40);

    // ctx.fillStyle = 'blue';
    // ctx.fillRect(470, 470, 30, 30);

    // ctx.fillStyle = 'indigo';
    // ctx.fillRect(480, 480, 20, 20);

    // ctx.fillStyle = 'violet';
    // ctx.fillRect(490, 490, 10, 10);
    
    // // Center
    // ctx.fillStyle = 'red';
    // ctx.fillRect(215, 215, 70, 70);

    // ctx.fillStyle = 'orange';
    // ctx.fillRect(220, 220, 60, 60);

    // ctx.fillStyle = 'yellow';
    // ctx.fillRect(225, 225, 50, 50);

    // ctx.fillStyle = 'green';
    // ctx.fillRect(230, 230, 40, 40);

    // ctx.fillStyle = 'blue';
    // ctx.fillRect(235, 235, 30, 30);

    // ctx.fillStyle = 'indigo';
    // ctx.fillRect(240, 240, 20, 20);

    // ctx.fillStyle = 'violet';
    // ctx.fillRect(245, 245, 10, 10);



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

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
