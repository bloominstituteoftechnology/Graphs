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
    //console.log(vertexes[0].edges[0]);
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

    for (let i of vertexes) {
      ctx.font = '20px serif';
      ctx.fillText(i.value, i.pos.x, i.pos.y-10);
    }
    
   
   // const graphClass = new Graph();
   // graphClass.bfs(vertexes);
    let queue = [];

    let startVert = vertexes[0];
    ctx.fillStyle = 'grey';
    ctx.beginPath();
    ctx.arc(startVert.pos.x, startVert.pos.y, 10, 0, 2 * Math.PI);
    ctx.fill();
    queue.push(startVert);
    //console.log(queue[0].edges[0].destination.pos.x);
    //console.log(vertexes[1]);
    

  while(queue.length !== 0) {
    //console.log(startVert.edges[0].destination.color);
    console.log(queue[0])
    let u = queue[0]
    console.log(u.edges.length);
      for (let i = 0; i < u.edges.length; i++) {
        if (u.edges[i].destination.color === 'white'){

            const x = queue[0].edges[i].destination.pos.x;
            const y = queue[0].edges[i].destination.pos.y;
            ctx.fillStyle = 'grey';
            ctx.beginPath();
            ctx.arc(x, y, 10, 0, 2 * Math.PI);
            ctx.fill();
            u.edges[i].destination.color = 'grey';
           // queue.push(queue[0].edges[i].destination);
            for (let j = 0; j < vertexes.length; j++) {
              if (vertexes[j].value === u.edges[i].destination.value && u.edges[i].destination.color !== 'black') {
               // console.log("hello")
               // console.log(vertexes[j].value)
                queue.push(vertexes[j])
              }
            }
        }
      }
      ctx.fillStyle = 'black';
      ctx.beginPath();
      ctx.arc(queue[0].pos.x, queue[0].pos.y, 10, 0, 2 * Math.PI);
      ctx.fill();
      queue[0].color = 'black';
    queue.shift();
  }
 // console.log(queue[0].pos.x)
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
   //this.state.graph.bfs('start');
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
