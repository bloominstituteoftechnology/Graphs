import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME (Phase 1)
const canvasWidth = 750;
const canvasHeight = 600;
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
  updateCanvas = () => {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

//randomize feature moved and props implemented to give 'onClick' functionality to my button for updating to a new random graph
    this.props.graph.vertexes = [];
    this.props.graph.randomize(5, 4, 150, 0.6);

    // Clear it
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    this.drawVertexes(ctx);
  }

  drawVertexes(ctx) {
    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // draw the lines between vertexes
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let v of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();

      // fill in the text
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    }
  }

    // DUMMY GRAPH--------------------------------------------
    // console.log('this.props.graph: ', this.props.graph);
    // //call our dummy function
    // this.props.graph.createDummyGraph();
    // console.log('called createDummyGraph');
    // DUMMY GRAPH--------------------------------------------  
  
  /**
   * Render
   */
render() { 
  return (
  <div>
    <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
    {/* Added button to populate new graph at random */}
    <button onClick={this.updateCanvas}>Update Graph</button>
  </div>
    )
    // console.log(this.updateCanvas);
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

    // !!! IMPLEMENT ME (Phase 4)
    // use the graph randomize() method
    // this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.getConnectedComponents();
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
