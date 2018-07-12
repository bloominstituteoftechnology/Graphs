import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 950;
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
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);


    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    const connectedComponents = this.props.graph.getConnectedComponents();
    
    const first = this.props.graph.vertexes[2];
    const last = this.props.graph.vertexes[10];
    const path = this.props.graph.dfs(first, last);
    console.log(`path from ${first.value} to ${last.value}`);
    console.log("dfs: ", path);

    const goldenEdges = (v1, v2) => {
      for (let i = 0; i < path.length - 1; i++) {
        if (path[i] === v1 && path[i + 1] === v2) {
          return true;
        }
        if (path[i] === v2 && path[i + 1] === v1) {
          return true;
        }
      }
      return false;
    }

    const colors = ['blue', 'teal', 'green', 'crimson', 'cyan', 'orange', 'yellow', 'olive', 'salmon'];
    connectedComponents.forEach(vertices => {
      const color = colors.shift();
      vertices.forEach(v1 => {
        v1.edges
          .map(e => e.destination)
          .forEach(v2 => {
            if (goldenEdges(v1, v2)) {
              ctx.strokeStyle = 'gold';
              ctx.lineWidth = 5;
            } else {
              ctx.strokeStyle = 'black';
              ctx.lineWidth = 2;
            }
            ctx.beginPath();
            ctx.moveTo(v1.pos.x, v1.pos.y);
            ctx.lineTo(v2.pos.x, v2.pos.y);
            ctx.stroke();
          });
      });

      vertices.forEach(v => {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(v.pos.x, v.pos.y, 25, 0, Math.PI * 2, true);
        ctx.fill();
        ctx.fillStyle = 'white';
        ctx.textAlign = 'center';
        ctx.font = "20px Verdana";
        ctx.fillText(v.value, v.pos.x, v.pos.y + 7);	
      });
    });
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
    console.log("randomizing");
    this.state.graph.randomize(6, 5, 150);
  }

  randomize = () => {
    const graph = new Graph();
    graph.randomize(6, 5, 150);
    this.setState({ graph });
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
	<button onClick={this.randomize}>Randomize</button>
      </div>
    );
  }
}

export default App;
