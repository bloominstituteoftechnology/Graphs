import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// graph size
const xCount = 5;
const yCount = 5;
const boxSize = 100;
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
    this.updateCanvas(this.props.graph.vertexes, 'blue' );
    // this.props.graph.bfs(this.props.graph.vertexes[0]);
    // this.props.graph.getConnectedComponents();
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
  updateCanvas(vertexes, color) {
    let colors = ['red', 'green', 'orange', 'black', 'blue', 'yellow', 'purple', 'green']
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Draw the edges
    ctx.lineWidth = 1;
    // ctx.strokeStyle = color;
    ctx.fillStyle = 'green';
    ctx.font = '10px sans-serif';
    ctx.textAlign = 'center';

    let comps = this.props.graph.getConnectedComponents();
    // console.log(comps);
    for (let comp of comps) {
      // console.log(comp);
      ctx.strokeStyle = colors.shift();
      for (let v of comp) { // From this vert
        for (let e of v.edges) { // To all these verts
          const v2 = e.destination;
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(v2.pos.x, v2.pos.y);
          ctx.stroke();
        }
        // color in vertexes
        ctx.beginPath();
        ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
        ctx.stroke();
        ctx.fill();
        
        // ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
      }
    }



    // for (let v of vertexes) { // From this vert
    //   for (let e of v.edges) { // To all these verts
    //     const v2 = e.destination;
    //     ctx.beginPath();
    //     ctx.moveTo(v.pos.x, v.pos.y);
    //     ctx.lineTo(v2.pos.x, v2.pos.y);
    //     ctx.stroke();
    //   }
    // }

    // Draw the verts
    // ctx.fillStyle = 'green'; // light blue

    // for (let v of vertexes) {
    //   ctx.beginPath();
    //   ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
    //   ctx.stroke();
    //   ctx.fill();
    // }

    // // Draw the vert names
    // ctx.font = '10px sans-serif';
    // ctx.textAlign = 'center';
    // ctx.fillStyle = 'white';

    // for (let comp in comps) {
    //   for (let v of comp) {
    //     ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
    //   }
    // }

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

    this.state.graph.randomize(xCount, yCount, boxSize, probability);
    // this.state.graph.components = this.state.graph.getConnectedComponents();
    this.state.graph.bfs(this.state.graph.vertexes[0]);
  }

  handleClick() {
    // console.log('yooooo');
    this.updateCanvas(this.props.graph.vertexes, 'blue');
  }

  render() {
    return (
      <div className="App">
        <button onClick={this.handleClick}>refresh</button>
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
