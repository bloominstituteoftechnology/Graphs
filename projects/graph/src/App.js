import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
 
const vertexRadius = 10;

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

    ctx.strokeStyle = 'black';
    ctx.fillStyle = 'blue';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    console.log("updating canvasa");
    console.log(this.props.graph.vertexes);

    console.log('edge ', this.props.graph.vertexes[0].edges[0]);

    //REMEMBER: Draw lines first!
    // let parentVert = this.props.graph.vertexes[0];
    // let debugEdge = this.props.graph.vertexes[0].edges[0];

    for (let parentVert of this.props.graph.vertexes) {
      for (let debugEdge of parentVert.edges) {
        ctx.moveTo(parentVert.pos.x, parentVert.pos.y);
        ctx.lineTo(debugEdge.destination.pos.x, debugEdge.destination.pos.y);
        ctx.stroke();
      }  
    }
    // we know our data is here :D
    // lets draw it!

    //let debugNode = this.props.graph.vertexes[0];
    //console.log(debugNode.pos.x);

    for (let vertex of this.props.graph.vertexes) {
      
      // draw node first, so make a circle
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, Math.PI * 2);
      ctx.stroke();

      //draw the fill
      ctx.fillStyle = 'white';
      ctx.fill();

      //draw the label or text
      ctx.fillStyle = 'black';
      ctx.textAlign = 'center';
      ctx.textBaseLine = 'middle';
      ctx.font = '10px Arial'; //TODO: Do we want stroke text or fill text?
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }
    








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
    // since our eventual goal is to implement randomiz here
    // this is probably a good place to try our test function and see
    // what happens and figure out how it works
    this.state.graph.randomize(5, 4, 150, 0.6);
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

