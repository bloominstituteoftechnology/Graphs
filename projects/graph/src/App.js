import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
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
  // updateCanvas() {
  //   let canvas = this.refs.canvas;
  //   let ctx = canvas.getContext('2d');

  //   let radius = 25;

  //   // Clear it
  //   ctx.fillStyle = '#cccccc';
  //   ctx.fillRect(0, 0, canvasWidth, canvasHeight);


  //   // !!! IMPLEMENT ME
  //   // compute connected components
  //   // console.log('graph: ', this.props.graph);

  //   // draw verts
  //   ctx.lineWidth = 1;
  //   ctx.strokeStyle = 'black';

  //   this.props.graph.vertexes.forEach(v => {
  //     // draw vert values (labels)

  //     // draw edges
  //     if (v.edges) {
  //       v.edges.forEach(e => {
  //         // console.log(e.destination);
  //         e.destination.edges.forEach(d => {
  //           ctx.moveTo(e.destination.pos.x, e.destination.pos.y);
  //           ctx.lineTo(d.destination.pos.x,d.destination.pos.y);
  //           ctx.stroke();
  //         })

  //       })
  //     }
  //     ctx.beginPath();
  //     ctx.stroke();
  //     ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
  //     ctx.fillStyle = 'purple';
  //     ctx.fill();
  //     ctx.font = "30px";
  //     ctx.fillStyle = 'white';
  //     ctx.fillText(v.value ,v.pos.x,v.pos.y);
  //   });
  // }

  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = '#7a9cd3';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    this.props.graph.vertexes.forEach((vertex) => {
      vertex.edges.forEach((edge) => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
      })
      ctx.lineWidth = 4;
      ctx.strokeStyle = '#FFFFFF';
      // ctx.shadowColor = '#999';
      // ctx.shadowBlur = 5;
      // ctx.shadowOffsetX = 5;
      // ctx.shadowOffsetY = 5;
      ctx.stroke();
    })
    this.props.graph.vertexes.forEach((vertex) => {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, Math.PI * 2, true);
      ctx.strokeStyle = '#324056'; // EB9D20
      ctx.stroke();
      ctx.fillStyle = '#FFFFFF';
      ctx.fill();
      ctx.beginPath();
      ctx.font = '16px Georgia';
      ctx.fontStyle = 'bold';
      ctx.fillStyle = '#324056';
      ctx.fillText(vertex.value, vertex.pos.x - 7, vertex.pos.y + 4);
      ctx.fill();
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);
    // this.state.graph.dump();
    this.state.graph.bfs();
  }

  handleRandomize = (e) => {
    console.log('randomize')
    this.state.graph.randomize(5, 4, 150, 0.6);
  }
  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        {/* <button onClick={this.handleRandomize}>Randomize</button> */}
      </div>
    );
  }
}

export default App;
