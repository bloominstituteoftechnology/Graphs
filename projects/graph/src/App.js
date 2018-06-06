import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 900;
const canvasHeight = 700;

const vertexSize = 12;
const vertexColor = 'purple';
const textColor = 'white';

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
    ctx.fillStyle = 'lightgray';
    ctx.fillRect(10, 10, canvasWidth, canvasHeight);

    console.log('in updateCanvas', this.props.graph.vertexes);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '12px Arial';


    for (let testVertices of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(testVertices.pos.x, testVertices.pos.y, vertexSize, 0, 2 * Math.PI);
      ctx.fillStyle = vertexColor;
      ctx.fill();
      ctx.stroke();

      
      ctx.fillStyle = textColor;
      ctx.fillText(testVertices.value, testVertices.pos.x, testVertices.pos.y);

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
    this.state.graph.testData();
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
