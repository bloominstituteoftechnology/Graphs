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

  draw(vertexes, color, clear = true) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    if (clear) {
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    }

    // draw edges
    for (let v of vertexes) {
      for (let e of v.edges) {
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
        ctx.stroke(); //draws the path defined w/ moveTo() & lineTo()
      }
    }
    
    // draw verts
    for (let v of vertexes) {
      ctx.moveTo(v.pos.x, v.pos.y);
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, 20, 0, 10);//creates an arc/curve
      ctx.closePath();
      ctx.fillStyle = color;
      ctx.fill();
      ctx.stroke();

      //Text for graph
      ctx.fillStyle = 'black';
      ctx.textAlign = 'center';
      ctx.font = '14px sans-serif';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    }

  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    function ranColor() {
      let letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }

    let clear = true;
    let connectedComponents = this.props.graph.getConnectedComponents();
    // console.log('Connected Components: ', connectedComponents)
    for (let c of connectedComponents) {
      const color = ranColor();
      console.log('APP ', c, color);
      this.draw(c, color, clear);
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



  }

  random = () => {
    const graph = new Graph();
    graph.randomize(5, 4, 150, 0.6);
    for (let vertex of graph.vertexes) {
      if (!vertex.color) {
        graph.bfs(vertex);
      }
    }
    this.setState({ graph });
  };

  render() {
    return (
      <div className="App">
        <div>
          <GraphView graph={this.state.graph}></GraphView>
        </div>
        <button onClick={this.random}>Randomize</button>
      </div>
    );
  }
}

export default App;
