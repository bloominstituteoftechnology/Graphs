import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 950;
const canvasHeight = 800;

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
    const connectedComponents = this.props.graph.getConnectedComponents();
    console.log(connectedComponents);

    const colors = ['blue', 'teal', 'green', 'cyan', 'orange', 'yellow'];
    connectedComponents.forEach(vertices => {
      const color = colors.shift();
      vertices.forEach(v => {
	v.edges.forEach(e => {
	  ctx.beginPath();
	  ctx.moveTo(v.pos.x, v.pos.y);
	  ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
	  ctx.stroke();
	});
      });

      vertices.forEach(v => {
	ctx.fillStyle = color;
	ctx.beginPath();
	ctx.arc(v.pos.x, v.pos.y, 25, 0, Math.PI * 2, true);
	ctx.fill();
	ctx.fillStyle = 'white';
	ctx.strokeStyle = 'black';
	ctx.textAlign = 'center';
	ctx.font = "20px Verdana";
	ctx.fillText(v.value, v.pos.x, v.pos.y + 5);	
      });
    });
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
    console.log("randomizing");
    this.state.graph.randomize(6, 5, 150);
  }

  randomize = () => {
    const graph = new Graph();
    graph.randomize(6, 5, 150);
    this.setState({ graph });
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
	<button onClick={this.randomize}>Randomize</button>
      </div>
    );
  }
}

export default App;
