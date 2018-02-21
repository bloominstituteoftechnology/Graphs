import React, { Component } from 'react';
import { Graph, Edge} from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
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
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

    // graph passed from the App class through this.props
    const { vertexes } = this.props.graph;
    console.log(vertexes[0].edges[0]);

    // step to drawing a simple line from one coordinate to the nexts   
 
    for (let i = 0; i < vertexes.length; i++) {
      // vertexes have position properties of x and y
      const x = vertexes[i].pos.x;
      const y = vertexes[i].pos.y;

      for (let j = 0; j < vertexes[i].edges.length; j++ ) {
        // destination has properties x and y as well 
        const x2 = vertexes[i].edges[j].destination.pos.x;
        const y2 = vertexes[i].edges[j].destination.pos.y;

        // use begin path inside for loop rather than outside of it.
        ctx.beginPath();
        // initial point 
        ctx.moveTo(x, y);
        // second point 
        ctx.lineTo(x2, y2);
        // draw the line itself 
        ctx.stroke();
      }
    }

    ctx.fillStyle = 'green';
    //let circle = new Path2D();
    for (let e of vertexes) {
      ctx.beginPath();
      ctx.arc(e.pos.x, e.pos.y, 10, 0, 2 * Math.PI);
      ctx.fill();
    }
    
    // x, y, radius, start angle, end angle, anticlockwise(defaults to clockwise)
  
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
   this.state.graph.randomize(5, 4, 150);
    //this.state.graph.dump();
   // console.log(this.state.graph.vertexes[2].edges[1])
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
