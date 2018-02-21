import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 750;
 const canvasHeight =  600;

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
    let array = this.props.graph.vertexes;
    for ( let i = 0; i < array.length; i++) {
        let pointX = array[i].pos.x;
        let pointY = array[i].pos.y;
        ctx.beginPath();
        ctx.arc(pointX, pointY, 5, 0, 2 * Math.PI, false);
        ctx.fillStyle = 'green';
        ctx.fill();
        ctx.lineWidth = 5;
        ctx.strokeStyle = '#003300';
        ctx.stroke();
        ctx.save();
        let edgy = array[i].edges;
        for (let j = 0; j < edgy.length; j++){
        ctx.beginPath();
        ctx.moveTo(pointX, pointY);
        console.log(edgy[j].weight);
        ctx.lineTo(edgy[j].destination.pos.x, edgy[j].destination.pos.y);
        ctx.lineWidth = 5;
        ctx.stroke();
        ctx.save();
        }
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
 const g = this.state.graph;
 g.randomize(5, 4, 150, 0.6);
  // !!! IMPLEMENT ME
    // use the graph randomize() method
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
