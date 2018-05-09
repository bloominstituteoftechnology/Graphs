import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
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

  getRandomColor() {
    const r = Math.floor(Math.random() * 155) + 100;
    const g = Math.floor(Math.random() * 155) + 100;
    const b = Math.floor(Math.random() * 155) + 100;
    const color = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    return color;
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

    const connectedGroups = this.props.graph.getConnectedComponents();

    // !!! IMPLEMENT ME
    this.props.graph.dump();
    connectedGroups.forEach(group => {
      const groupColor = this.getRandomColor();
      group.forEach(vert => {
        vert.edges.forEach(edge => {
          ctx.beginPath();
          ctx.moveTo(vert.pos.x, vert.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y)
          ctx.strokeStyle = groupColor;
          ctx.stroke();
        })
      })
      
      group.forEach(vert => {
        ctx.beginPath();
        ctx.arc(vert.pos.x, vert.pos.y, 10, 0, 2 * Math.PI);
        ctx.fillStyle = groupColor;
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.stroke();
  
        ctx.fillStyle = 'black';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vert.value, vert.pos.x, vert.pos.y);
      })

    })
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 5, 100);
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
