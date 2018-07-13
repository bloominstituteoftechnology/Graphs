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
  selectedVertexes = [];
  
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
      ctx.lineWidth = 1.5;

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
      ctx.lineWidth = 3;

      group.forEach(v => {
        v.color = color;
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

  selectVertex = e => {
    // Reference to canvas and click coordinates
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');
    const clickX = e.clientX - canvas.offsetLeft;
    const clickY = e.clientY - canvas.offsetTop + window.scrollY;
    let foundMatch = false;

    this.props.graph.vertexes.forEach(vertex => {
      // Check to see if click was within circle of vertex
      // Account for canvas offset and window scroll
      const xMatch = clickX > vertex.pos.x - circleRadius && clickX < vertex.pos.x + circleRadius;
      const yMatch = clickY > vertex.pos.y - circleRadius && clickY < vertex.pos.y + circleRadius;
      const duplicate = this.selectedVertexes.includes(vertex);
      
      // Cap target vertexes at 2 and check if duplicate
      if (xMatch && yMatch && !duplicate &&this.selectedVertexes.length < 2) {
        this.selectedVertexes.push(vertex);
        foundMatch = true;

        // Highlight selection
        ctx.strokeStyle = 'yellow';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, circleRadius - 2, 0, 2 * Math.PI);
        ctx.stroke();
      }
    });

    if (!foundMatch) {
      this.selectedVertexes = [];
      this.clearSelection();
    }
  }

  clearSelection() {
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');

    this.props.graph.vertexes.forEach(vertex => {
       // Outline/Fill vertex
       ctx.fillStyle = vertex.color;
       ctx.strokeStyle = 'black';
       ctx.beginPath();
       ctx.arc(vertex.pos.x, vertex.pos.y, circleRadius, 0, 2 * Math.PI);
       ctx.stroke();
       ctx.fill();

       // Fill text
       ctx.fillStyle = 'white';
       ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    });
  }

  path = () => {
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');
    const v1 = this.selectedVertexes[0];
    const v2 = this.selectedVertexes[1];

    if (this.selectedVertexes.length === 2) {
      const connection = this.props.graph.findShortestPath(v1, v2);
      
      // If vertexes are connected then
      if (connection) {
        // - Color vertexes and edges appropriately -
        // Edges
        ctx.strokeStyle = 'blue';
        ctx.lineWidth = 4;

        // Render connection with blue line
        connection.forEach(vertex => {
          vertex.edges.forEach(edge => {
            // Only color lines in connection route
            if (connection.includes(vertex) && connection.includes(edge.destination)) {
              ctx.beginPath();
              ctx.moveTo(vertex.pos.x, vertex.pos.y);
              ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
              ctx.stroke();
            }
          });
        });
      }
    }
    
    this.clearSelection();
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
          onClick={(e) => this.selectVertex(e)}>
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
