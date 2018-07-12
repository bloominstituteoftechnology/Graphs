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
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);


    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    const connectedComponents = this.props.graph.getConnectedComponents();

    const first = this.props.graph.vertexes[2];
    const last = this.props.graph.vertexes[10];
    if (this.selectedVertices().length === 2) {
      this.path = this.findGoldenPath(...this.selectedVertices());
    } else {
      this.path = [];
    }
    console.log(`path from ${first.value} to ${last.value}`);
    console.log("dfs: ", this.path);

    
    const colors = ['teal', 'green', 'crimson', 'blue', 'cyan', 'orange', 'yellow', 'olive', 'salmon'];
    connectedComponents.forEach(vertices => {
      const color = colors.shift();
      vertices.forEach(v1 => {
        v1.edges.forEach(e => {
          this.drawEdge(v1, e.destination, e, ctx);
        });
      });
      
      vertices.forEach(v => {
        this.drawVertex(v, color, ctx);
      });
    });
  }
  
  goldenEdges = (v1, v2) => {
    for (let i = 0; i < this.path.length - 1; i++) {
      if (this.path[i] === v1 && this.path[i + 1] === v2) {
        return true;
      }
      if (this.path[i] === v2 && this.path[i + 1] === v1) {
        return true;
      }
    }
    return false;
  }
  
  drawEdge = (v1, v2, e, ctx) => {
    if (this.goldenEdges(v1, v2)) {
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

    // Label the edge weights

    const midX = (v1.pos.x + v2.pos.x) / 2;
    const midY = (v1.pos.y + v2.pos.y) / 2;
    ctx.beginPath();
    ctx.arc(midX, midY, 12, 0, Math.PI * 2, true);
    ctx.fillStyle = 'white';
    ctx.fill();
    ctx.font = "12px Verdana";
    ctx.fillStyle = 'black';
    ctx.fillText(e.weight, midX - 2, midY + 5);
  }

  drawVertex = (v, color, ctx) => {
    if (v.selected) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, 25, 0, Math.PI * 2, true);
      ctx.fillStyle = "gold";
      ctx.fill();
    }
    ctx.beginPath();
    ctx.arc(v.pos.x, v.pos.y, 20, 0, Math.PI * 2, true);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.fillStyle = 'white';
    ctx.textAlign = 'center';
    ctx.font = "16px Verdana";
    ctx.fillText(v.value, v.pos.x, v.pos.y + 7);	
  }

  handleClick = (e) => {
    console.log(e);
    const selected = this.findSelectedVertex(this.props.graph, e.pageX, e.pageY, 20);
    if (selected) {
      if (selected.selected) {
        selected.selected = false;
        this.updateCanvas();
      } else if (this.selectedVertices().length < 2) {
        selected.selected = true;
        this.updateCanvas();
      }
    }
  }

  findGoldenPath = (v1, v2) => this.props.graph.dfs(v1, v2)

  selectedVertices = () => this.props.graph.vertexes.filter(v => v.selected)

  findSelectedVertex = (graph, x, y, radius) => {
    const distance = (vertex, x, y) => {
      const dx = Math.abs(x - vertex.pos.x);
      const dy = Math.abs(y - vertex.pos.y);
      return Math.sqrt(dx * dx + dy * dy);
    }

    return graph.vertexes.find(v => distance(v, x, y) < radius);
  }
  
  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} onClick={this.handleClick}></canvas>;
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
