import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = window.innerWidth; // 750;
const canvasHeight = window.innerHeight; // 600;
const circleRadius = 25;

/* GraphView */
class GraphView extends Component {
  /* On mount */
  componentDidMount() {
    this.updateCanvas();
  }

  /* On state update */
  componentDidUpdate() {
    this.updateCanvas();
  }

  /* Render the canvas */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = "23px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    ctx.strokeStyle = "white";
    this.props.graph.vertexes.forEach(v => {
      v.edges.forEach(e => {
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
        ctx.stroke();
        ctx.fill();
      });
    });

    ctx.strokeStyle = "transparent";
    this.props.graph.vertexes.forEach(v => {
      const x = v.pos.x, y = v.pos.y;

      const gradient = ctx.createRadialGradient(x, y, 0, x, y, circleRadius);
      gradient.addColorStop(0.0, "white");
      gradient.addColorStop(0.3, "yellow");
      gradient.addColorStop(0.8, "skyblue");
      gradient.addColorStop(1.0, "transparent");

      ctx.beginPath();
      ctx.fillStyle = gradient;
      ctx.arc(x, y, circleRadius, 0, Math.PI*2);
      ctx.stroke();
      ctx.fill();

      ctx.fillStyle = "black";
      ctx.fillText(v.value, x, y);
    });
  }
  
  /* Render */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}


/* App */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph(),
      box: canvasHeight < canvasWidth ? canvasHeight/5 : canvasWidth/5
    };

    this.state.graph.randomize(5, 4, canvasHeight/5, 0.6);
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
