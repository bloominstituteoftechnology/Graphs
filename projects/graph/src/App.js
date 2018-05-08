import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

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
    let radius = 50;


const grd = ctx.createLinearGradient(0, 0, 500, 0)
    grd.addColorStop(0, "purple");
    grd.addColorStop(1, "pink");


    // Clear it
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 10, 0, 2 * Math.PI);
      ctx.fillStyle = 'lightpink';
      ctx.fill();
      ctx.strokeStyle = 'blue';
      ctx.stroke();


      ctx.fillStyle = 'black';
      ctx.font = "10px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    // ctx.fillStyle = '#3BB9FF';
    // ctx.fillRect(0, 0, 500, 200);

    

    // ctx.fillStyle = 'yellow';
    // ctx.arc(800 / 2, 150 / 2, radius, 0, 2 * Math.PI, false); 
    // ctx.fill();


    // ctx.fillStyle = 'ivory';
    // ctx.fillRect(80, 150, 200, 200);
    
    // ctx.fillStyle = 'brown';
    // ctx.fillRect(100, 170, 50, 50);
    
    // ctx.fillStyle = 'brown';
    // ctx.fillRect(210, 170, 50, 50);

    // ctx.fillStyle = 'gray';
    // ctx.fillRect(153, 250, 50, 100);

    
    // let sWidth = 500;
    // let sHeight = 500;
    // let path=new Path2D();
    // path.moveTo((sWidth/2)+50,sHeight/2);
    // path.lineTo((sWidth/2),(sHeight/2)-50);
    // path.lineTo((sWidth/2)-50,sHeight/2);
    // ctx.fill(path);
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
      connectedComponents: []
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(4, 5, 200, 0.5);
    this.state.connectedComponents = this.state.graph.getConnectedComponents();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} connectedComponents={this.state.graph.getConnectedComponents}></GraphView>
      </div>
    );
  }
}

export default App;
