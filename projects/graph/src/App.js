import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
// Figure out the canvas size
const xCount = 5;
const yCount = 5;
const boxSize = 135;
const probability = 0.6;

// Figure out the canvas size
const canvasWidth = boxSize * xCount;
const canvasHeight = boxSize * yCount;
const radius = boxSize / 8;

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

  drawVerts(vertexes, color='red', clear=true) {
    // let canvas = this.refs.canvas;
    // let ctx = canvas.getContext('2d');
    // ctx.fillStyle = 'gray';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    
    // ctx.lineWidth = 1.5;
    // ctx.strokeStyle = 'teal';

    // // Draw the verts with lines
    // for (let v of vertexes) {
    //   ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
    //   ctx.stroke();
    // }

    // // fill the verts
    // for (let v of vertexes) {
    //   ctx.beginPath();
    //   ctx.fillStyle = 'black';
    //   ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
    //   ctx.fill();
    // }
    
    // // Draw the vert names
    // for (let v of vertexes) {
    //   ctx.beginPath();
    //   ctx.font = '14px sans-serif';
    //   ctx.textAlign = 'center';
    //   ctx.fillStyle = 'white';
    //   ctx.fillText(v.value, v.pos.x, v.pos.y );
    // }

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    if (clear) {
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }

    // Draw the edges
    ctx.lineWidth = 2;
    ctx.strokeStyle = color;




    for (let v of vertexes) { // From this vert   like --
      for (let e of v.edges) { // To all these verts
        const v2 = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v2.pos.x, v2.pos.y);
        ctx.stroke();
      }
    }

    // Draw the verts on top
    ctx.fillStyle = 'black'; // light blue

    for (let v of vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.stroke();
      ctx.fill();
    }

    // // Draw the vert names
    ctx.font = '14px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillStyle = 'white';

    for (let v of vertexes) {
      ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
    }
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    function getRandomColor() {
      let letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
    const connectedComponents = this.props.graph.getConnectedComponents();
    let clear = true;
    for (let component of connectedComponents) {
      const curColor = getRandomColor();
      this.drawVerts(component, curColor, clear);
      clear = false;
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
    // Create a graph with 20 nodes in a grid (5*4), with a 150x150px jitter
    // box for each of them. The canvas size should be 750x600 to hold this
    // graph (5*150=750, 4*150=600). The probability of any edge of the grid
    // existing is 0.6.
    this.state.graph.randomize(xCount, yCount, boxSize, probability);
  }
  refreshPage(){ 
    window.location.reload(); 
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <input type="button" value="Reload Page" onClick={ this.refreshPage }/>
      </div>
    );
  }
}

export default App;