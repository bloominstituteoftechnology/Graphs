import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 1000;

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
    let circles = (x, y) => {
      ctx.beginPath();
      ctx.arc(x, y, 22, 0, 2 * Math.PI, false);
      ctx.fillStyle = "purple";
      ctx.fill();
      ctx.stroke();
    }
    let numbers = (x, y) => {
      ctx.beginPath();
      ctx.fillStyle = '#0FF';
      ctx.fill();
      ctx.font = "30px Georgia";
      ctx.fillText(index, x - 10, y + 10);
      ctx.strokeStyle = '#000';
      ctx.stroke();
    }
    let lines = (x, y, nX, nY) => {
      ctx.moveTo(x, y);
      ctx.lineWidth = 2;
      ctx.lineTo(nX, nY);
      ctx.stroke();
    }
    // Clear it
    ctx.fillStyle = 'yellow';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let v of this.props.graph.vertexes) {
      let x = v.pos.x;
      let y = v.pos.y;
      for (let w of v.edges) {
        let nX = w.weight.pos.x;
        let nY = w.weight.pos.y;
        lines(x, y, nX, nY);
      }
    }

    let index = 1;
    for (let v of this.props.graph.vertexes) {
      let x = v.pos.x;
      let y = v.pos.y;
      circles(x, y);
      numbers(x, y);
      index++;
    }



    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! this.state.graphs.vertexes for each vertex.pos.x & vertex.pos.y




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

    this.state.graph.randomize(5, 4, 150, 0.6);
    //console.log(this.state.graph.vertexes);
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
