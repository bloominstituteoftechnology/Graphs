import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleRadius = 15;

/**
 * GraphView
 */
class GraphView extends Component {
  targetVertexes = [];
  
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
  updateCanvas = () => {
    const graph = this.props.graph;
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    graph.vertexes = [];
    graph.randomize(5, 4, 150);

    // Clear it
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '13px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // !!! IMPLEMENT ME
    const getRandomInt = max => Math.floor(Math.random() * Math.floor(max));
    const getRandomColor = () => `rgb(${getRandomInt(256)}, ${getRandomInt(256)}, ${getRandomInt(256)})`;
    const groups = graph.getConnectedComponents();

    groups.forEach(group => {
      // compute connected components
      // draw edges
      ctx.strokeStyle = 'black';

      group.forEach(v => {
        v.edges.forEach(edge => {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();

          // draw edge weight
          const x = (v.pos.x + edge.destination.pos.x) / 2;
          const y = (v.pos.y + edge.destination.pos.y) / 2;
          const weight = getRandomInt(11) + 1

          ctx.fillStyle = 'white';
          ctx.fillRect(x - 8, y - 8, 16, 16);

          ctx.fillStyle = 'black';
          ctx.fillText(weight, x, y);
        });
      });

      // draw verts
      // draw vert values (labels)
      const color = getRandomColor();
      group.forEach(v => {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();
  
        // fill in the text
        ctx.fillStyle = 'white';
        ctx.fillText(v.value, v.pos.x, v.pos.y);
      });
    });
  }

  targetVertex = e => {
    // Reference to canvas and click coordinates
    const canvas = this.refs.canvas;
    const clickX = e.clientX - canvas.offsetLeft;
    const clickY = e.clientY - canvas.offsetTop + window.scrollY;
    let foundMatch = false;

    this.props.graph.vertexes.forEach(vertex => {
      // Check to see if click was within circle of vertex
      // Account for canvas offset and window scroll
      const xMatch = clickX > vertex.pos.x - circleRadius && clickX < vertex.pos.x + circleRadius;
      const yMatch = clickY > vertex.pos.y - circleRadius && clickY < vertex.pos.y + circleRadius;
      const duplicate = this.targetVertexes.includes(vertex);
      
      // Cap target vertexes at 2 and check if duplicate
      if (xMatch && yMatch && !duplicate &&this.targetVertexes.length < 2) {
        this.targetVertexes.push(vertex);
        foundMatch = true;
      }
    });

    if (!foundMatch) this.targetVertexes = [];
  }

  path = () => {
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');
    const v1 = this.targetVertexes[0];
    const v2 = this.targetVertexes[1];

    if (this.targetVertexes.length === 2) {
      const connected = this.props.graph.areConnected(v1, v2);
      
      // If vertexes are connected then
      if (connected) {
        // Find quickest path
        

        // Color vertexes and edges appropriately
        // Vertex 1
        ctx.fillStyle = 'green';
        ctx.beginPath();
        ctx.arc(v1.pos.x, v1.pos.y, circleRadius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();

        // fill in the text
        ctx.fillStyle = 'white';
        ctx.fillText(v1.value, v1.pos.x, v1.pos.y);

        // Vertex 2
        ctx.fillStyle = 'red';
        ctx.beginPath();
        ctx.arc(v2.pos.x, v2.pos.y, circleRadius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fill();

        // fill in the text
        ctx.fillStyle = 'white';
        ctx.fillText(v2.value, v2.pos.x, v2.pos.y);
      }
    }
    console.log(this.targetVertexes);
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas"
          width={canvasWidth}
          height={canvasHeight}
          onClick={(e) => this.targetVertex(e)}>
        </canvas>
        <button onClick={this.updateCanvas}>Generate New Graph</button>
        <button onClick={this.path}>Path</button>
      </div>
    )
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

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
