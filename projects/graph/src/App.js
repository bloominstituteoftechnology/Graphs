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
const vRadius = 15;
const fontConf = '12px serif';

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

  drawVertex(ctx, vertex) {
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.moveTo(vertex.pos.x, vertex.pos.y);
    ctx.strokeStyle = 'black';
    ctx.arc(vertex.pos.x, vertex.pos.y, vRadius, 0, 2 * Math.PI, true);
    ctx.stroke();
    ctx.closePath();
    let connected = this.props.graph.bfs(vertex);
    // Use Random Color or Blue Color for Fill
    ctx.fillStyle = this.getRandomColor('#BBBBBB', '#EEEEEE');
    connected.forEach(connectedVertex => {
      ctx.beginPath();
      ctx.moveTo(connectedVertex.pos.x, connectedVertex.pos.y);
      ctx.arc(connectedVertex.pos.x, connectedVertex.pos.y, vRadius, 0, 2 * Math.PI, true);
      ctx.fill();
    });
  }

  writeVertexData(ctx, vertex) {
    // Write each Vertex Values
    ctx.fillStyle = 'black';
    ctx.font = fontConf;
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
  }

  selectVertex(ctx, vertex) {
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
    ctx.font = fontConf;
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

  drawEdge(ctx, vertex, edge) {
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
    ctx.font = fontConf;
    ctx.beginPath();
    ctx.moveTo(avgX, avgY);
    ctx.strokeText(edge.weight, avgX, avgY);
    ctx.fillText(edge.weight, avgX, avgY);
    ctx.lineWidth = 1;

  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Create a White Canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // --- GraphView is getting 'graph' as a prop from App.
    // --- accessible through 'this.props.graph'
    const connectedComponents = this.props.graph.getConnectedComponents();

    // DRAW EDGES
    // For each vertex inside the connected components array
    connectedComponents.forEach(vertex => {
      vertex.edges.forEach(edge => {
        this.drawEdge(ctx, vertex, edge);
      });
    })

    // DRAW VERTICES
    this.props.graph.vertexes.forEach(vertex => {
      this.drawVertex(ctx, vertex);
    })

    // DRAW VERTICES VALUES ON TOP
    this.props.graph.vertexes.forEach(vertex => {

      this.writeVertexData(ctx, vertex);
    });
  }

  /**
   * graphClicked: When the canvas gets clicked it handles the event
   */
  graphClicked = (event) => {
    // Helper function for figuring out where our canvas element
    // starts in the DOM x and y so we can later match it to our
    // current mouse position when the vertex are clicked
    const offset = (element) => {
      const rect = element.getBoundingClientRect(),
        scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
        scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      return { top: rect.top + scrollTop, left: rect.left + scrollLeft }
    }

    // Get canvas element DOM X and Y position
    // Stores itn in an object with top and left props
    let canvasPosition = offset(event.target);
    // Calculate our events mouse position in comparison
    // with our canvas position to find out where inside
    // the canvas we have clicked.
    let localXPos = event.clientX - canvasPosition.left;
    let localYPos = event.clientY - canvasPosition.top;

    const clicked = []; // An array of clicked vertices.

    this.props.graph.vertexes.forEach(vertex => {
      // subtract the larger of the 2 positions and calculate the difference
      // (Could use some absolute value here too)
      let xDif = localXPos > vertex.pos.x ? localXPos - vertex.pos.x : vertex.pos.x - localXPos;
      let yDif = localYPos > vertex.pos.y ? localYPos - vertex.pos.y : vertex.pos.y - localYPos;
      if (yDif < vRadius && xDif < vRadius) {
        // Redraw Vert with New Colors
        let ctx = event.target.getContext('2d'); // Get our canvas to use
        this.selectVertex(ctx, vertex);
        clicked.push(vertex); // Add our "clicked" vertex to the clicked array.

        // TODO: Implement Dijkstras Algo for routing from clicked[0] to clicked[1]
      }
    })
  }

  /**
   * Render
   */
  render() {
    return <canvas
      className='mainCanvas'
      ref="canvas"
      width={canvasWidth}
      height={canvasHeight}
      onClick={this.graphClicked}>
    </canvas>;
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
