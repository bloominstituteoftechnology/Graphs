import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1200;
const canvasHeight = 900;
const circleRadius = 15;
const canvasStartX = 0;
const canvasStartY = 0;

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
    // this.props.graph.createDummyGraph();
    this.props.graph.randomize(8, 6, 150);
    this.props.graph.dump();

    // Clear it
    ctx.fillStyle = 'orange';
    ctx.fillRect(canvasStartX, canvasStartY, canvasWidth, canvasHeight);
    // ctx.fillRect(100, 100, canvas.width, canvas.height);

    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // !!! IMPLEMENT ME
    // compute connected components
    const checked = [];
    this.props.graph.vertexes.forEach(v => {
      const connected = [];

    })

    this.props.graph.vertexes.forEach(v => {
      ctx.strokeStyle = v.color;
      for (let j = 0; j < v.edges.length; j++) {
        ctx.moveTo(v.pos.x + canvasStartX, v.pos.y + canvasStartY);
        // draw edges
        ctx.lineTo(v.edges[j].destination.pos.x + canvasStartX, v.edges[j].destination.pos.y + canvasStartY);
        ctx.stroke();
      }
    })

    this.props.graph.vertexes.forEach(v => {
      ctx.beginPath();
      ctx.fillStyle = v.color;  //sets color for the circle
      ctx.strokeStyle = v.color;  //sets color for the circle's edge
      // draw verts
      ctx.arc(v.pos.x + canvasStartX, v.pos.y + canvasStartY, circleRadius, 0, 2 * Math.PI);  //(x,y) center of cicle, radius, arc of circle (in radians)
      ctx.fill();  //fills in the circle
      ctx.stroke();  //draws the circle

      // draw vert values (labels)
      ctx.fillStyle = 'black';  //sets color for the text
      ctx.fillText(v.value, v.pos.x + canvasStartX, v.pos.y + canvasStartY);  //fill in the text of v.value @ (x,y) of (v.pos.x, v.pos.y);
    })

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
  }

  // !!! IMPLEMENT ME
  // use the graph randomize() method
  randomize = () => {
    this.setState({ graph: new Graph() });
  }

  render() {
    return (
      <div className="App">
        <div>
          <GraphView graph={this.state.graph}></GraphView>
        </div>
        <div>
          <button onClick={this.randomize}>Random </button>
        </div>
      </div>
    );
  }
}

export default App;
