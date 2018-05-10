import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

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
    ctx.fillStyle = '#303030';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const colors = ['CadetBlue', 'BurlyWood', 'SeaGreen', 'DarkCyan', 'DarkOrchid', 'HotPink', 'OliveDrab', 'SlateGray', 'YellowGreen'];

    this.props.graph.connectedComponents.forEach((vertexes, i) => {
          ////draw line
      for(let v of vertexes){
        const vx = v.pos.x;
        const vy = v.pos.y;
        // draw edges
        for(let e of v.edges){
          const dx = e.destination.pos.x;
          const dy = e.destination.pos.y;
          ctx.moveTo(vx, vy);
          ctx.lineTo(dx, dy);
          ctx.strokeStyle = colors[i];
          ctx.stroke();
        }
      }

      //draw circle
      for(let v of vertexes){
        const vx = v.pos.x;
        const vy = v.pos.y;
        ctx.fillStyle = colors[i];
        // draw verts
        ctx.beginPath();
        ctx.arc(vx, vy, 15, 0, 2*Math.PI);
        ctx.stroke();
        ctx.fill();
        // draw vert values (labels)
        ctx.font = "13px Comic Sans MS";
        ctx.fillStyle = "blue";
        ctx.textAlign= "center";
        ctx.textBaseline="middle";
        ctx.fillText(v.value, vx, vy);
        }
      });
    // !!! IMPLEMENT ME
    // compute connected components

  }
  
  /**
   * Render
   */
  render() {
    return (<div>
      <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
      <button onClick={()=>{this.props.generateGraph()}}>Generate Graph</button>
      </div>);
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
    this.state.graph.getConnectedComponents();
  }

  generateGraph = ()=>{
    const graph = new Graph();
    graph.randomize(5, 4, 150, 0.6);
    graph.getConnectedComponents();
    this.setState({graph});
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} generateGraph={this.generateGraph}></GraphView>
      </div>
    );
  }
}

export default App;
