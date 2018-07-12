import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 1000; 
 const canvasHeight = 900;
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
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    ctx.font = "13px Arial";
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = 'white';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y);

      // v.edges.forEach((l) => {
      //   ctx.beginPath();
      //   ctx.moveTo(v.pos.x, v.pos.y);
      //   ctx.lineTo(l.destination.pos.x, l.destination.pos.y);
      //   ctx.stroke();
      // })
    })
    function randomColor(max) {
      let r = Math.floor(Math.random() * Math.floor(max));
      let g = Math.floor(Math.random() * Math.floor(max));
      let b = Math.floor(Math.random() * Math.floor(max));
      let ran = "rgb(" + r + "," + g + "," + b + ")";
      return ran.toString();
    }
    let lines = this.props.graph.getConnectedComponents(this.props.graph.vertexes);
    console.log("lines:\n", lines)

    lines.forEach((obj) => {
      let color = randomColor(255);
      ctx.fillStyle = color;
      ctx.strokeStyle = color;
      obj.forEach((v) => {
        ctx.beginPath();
        ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
        ctx.fill();
        ctx.stroke();
        v.edges.forEach((e) => {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
          ctx.stroke();
        })
      })
    })


    // ctx.fillStyle = 'red';
    // ctx.strokeStyle = 'red';
    // let change = this.props.graph.bfs(this.props.graph.vertexes[0]);
    // change.forEach((v) => {
    //   ctx.beginPath();
    //   // ctx.fillStyle = 'red';
    //   ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
    //   ctx.fill();
    //   ctx.stroke();
    //   v.edges.forEach((l) => {
    //     ctx.beginPath();
    //     ctx.moveTo(v.pos.x, v.pos.y);
    //     ctx.lineTo(l.destination.pos.x, l.destination.pos.y);
    //     ctx.stroke();
    //   })
    // })
    console.log('vertexes:\n', this.props.graph.getConnectedComponents(this.props.graph.vertexes));
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
    this.state.graph.randomize(4, 3, 50, 0.6);
    //console.log("props", this.props)
    console.log("state:\n", this.state)
    // use the graph randomize() method
    
  }

  render() {
    return (
      <div className="App">
        <Update graph={this.state.graph}/>
        <div>
        <GraphView graph={this.state.graph}></GraphView>
        </div>
      </div>
    );
  }
}
function Update(props) {
    return (
    <button 
    onClick={reloader}
    >Update</button>
    )
}
function reloader() {
  window.location.reload();
}

export default App;
