import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
// Sizing the Graph
const xsize = 5;
const ysize = 4;
const jitter = 150;
// Sizing the Vertices
const vRadius = 20;

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

  // Get random color from a range.
  getRandomColor(start, end) {
    let min = parseInt(start.replace("#", ""), 16);
    let max = parseInt(end.replace("#", ""), 16);
    return "#" + Math.floor((Math.random() * (max - min) + min)).toString(16).toUpperCase();
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
    // --- GraphView is getting 'graph' as a prop from App.
    // --- accessible through 'this.props.graph'

    const connectedComponents = this.props.graph.getConnectedComponents();
    // console.log('Connected Components:', connectedComponents);

    // draw edges
    // For each vertex inside the connected components array
    connectedComponents.forEach(vertex => {
      vertex.edges.forEach(edge => {
        ctx.lineWidth = 2;
        ctx.beginPath(); // Begin Drawing Line
        ctx.moveTo(vertex.pos.x, vertex.pos.y); // Move to Origin Vertex
        ctx.strokeStyle = 'black';
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y)
        ctx.stroke(); // Stroke the line out
        ctx.closePath() // Reset the Cursor Back to Initial Vertex
        // Draw in Weights AFTER THE EDGES ARE DRAWN IN
        let avgX = (vertex.pos.x + edge.destination.pos.x) / 2;
        let avgY = (vertex.pos.y + edge.destination.pos.y) / 2;
        ctx.fillStyle = 'black';
        ctx.lineWidth = 6;
        ctx.strokeStyle = 'white';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.font = '14px serif';
        ctx.beginPath();
        ctx.moveTo(avgX, avgY);
        ctx.strokeText(edge.weight, avgX, avgY);
        ctx.fillText(edge.weight, avgX, avgY);
        ctx.lineWidth = 1;
      });
    })
    // draw verts
    this.props.graph.vertexes.forEach(vertex => {
      ctx.beginPath();
      ctx.lineWidth = 2;
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      ctx.strokeStyle = 'black';
      ctx.arc(vertex.pos.x, vertex.pos.y, vRadius, 0, 2 * Math.PI, true);
      ctx.stroke();
      ctx.closePath();
      // Fill them In White
      // ctx.fillStyle = 'white';
      // ctx.beginPath();
      // ctx.moveTo(vertex.pos.x, vertex.pos.y);
      // ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, 2 * Math.PI, true);
      // ctx.fill();
      // Change the Color of the Connected Ones
      let connected = this.props.graph.bfs(vertex);
      ctx.fillStyle = this.getRandomColor('#BBBBBB', '#EEEEEE');
      connected.forEach(connectedVertex => {
        ctx.beginPath();
        ctx.moveTo(connectedVertex.pos.x, connectedVertex.pos.y);
        ctx.arc(connectedVertex.pos.x, connectedVertex.pos.y, vRadius, 0, 2 * Math.PI, true);
        ctx.fill();
      });
    })
    this.props.graph.vertexes.forEach(vertex => {
      // Write each Vertex Values
      ctx.fillStyle = 'black';
      ctx.font = '14px serif';
      ctx.beginPath();
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.moveTo(vertex.pos.x, vertex.pos.y);
      // Stroke and Fill the Text In
      ctx.lineWidth = 3;
      ctx.strokeStyle = 'white'
      ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.lineWidth = 1;
      ctx.strokeStyle = 'black'
      ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    });
  }
  /* WHEN CANVAS IS CLICKED!*/
  graphClicked = (event) => {
    // function for figuring out where our canvas starts in the DOM x and y
    function offset(el) {
      const rect = el.getBoundingClientRect(),
        scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
        scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      return { top: rect.top + scrollTop, left: rect.left + scrollLeft }
    }
    let canvasPosition = offset(event.target);
    let localXPos = event.clientX - canvasPosition.left;
    let localYPos = event.clientY - canvasPosition.top;

    //console.log("top: ", canvasPosition.top, "left: ", canvasPosition.left);
    //console.log("Mouse x: ", localXPos, "Mouse y: ", localYPos);
    this.props.graph.vertexes.forEach(vertex => {
      // if localXPos > vertex.pos.x subtract localXPos - vertex.pos.x
      // if localXPos < vertex.pos.x subtract vertex.pos.x - localXPos
      let xDif = localXPos > vertex.pos.x ? localXPos - vertex.pos.x : vertex.pos.x - localXPos;
      let yDif = localYPos > vertex.pos.y ? localYPos - vertex.pos.y : vertex.pos.y - localYPos;
      if (yDif < vRadius && xDif < vRadius) {
        // Redraw Vert with New Colors
        let ctx = event.target.getContext('2d'); // Get our canvas to use
        // Draw Our Outline
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.strokeStyle = 'black';
        ctx.arc(vertex.pos.x, vertex.pos.y, vRadius, 0, 2 * Math.PI, true);
        ctx.stroke();
        ctx.closePath();
        // Draw our Fill
        ctx.fillStyle = `rgb(0, 75, 136)`;
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.arc(vertex.pos.x, vertex.pos.y, vRadius, 0, 2 * Math.PI, true);
        ctx.fill();
        // Draw Vertex Values
        ctx.fillStyle = 'black';
        ctx.font = '14px serif';
        ctx.beginPath();
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        // Stroke and Fill the Text In
        ctx.lineWidth = 3;
        ctx.strokeStyle = 'white'
        ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);
        ctx.lineWidth = 1;
        ctx.strokeStyle = 'black'
        ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
        console.log(`${vertex.value} was clicked!`);
      }
    })
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} onClick={this.graphClicked}></canvas>;
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
    this.state.graph.randomize(xsize, ysize, jitter);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <div className='refreshWrapper'>
          <div className="refreshButton" onClick={() => window.history.go("/")}>REFRESH ME</div>
        </div>
      </div>
    );
  }
}

export default App;
