import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

// Get a random color
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

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
    
    const vertexes = this.props.graph.vertexes;
    const radius = 15;
    
    // draw all the edges first
    // loop over components and set a random color for each component
    for (let component of this.props.connectedComponents) {
      const color = getRandomColor();
      ctx.strokeStyle = color;
      ctx.lineWidth = 4;
      // loop through each vertex in the component
      for (let i = 0; i < component.length; i++) {
        const vertex = vertexes[component[i]];
        // draw its edges in the selected color
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        }
      }
      // draw all the vertexes second to hide edge overlap on vertexes
      // ctx.strokeStyle = 'black';
      ctx.lineWidth = 3;
      // for (let vertex of vertexes) {
      for (let i = 0; i < component.length; i++) {
        const vertex = vertexes[component[i]];
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2 * Math.PI);
        ctx.fillStyle = 'white';
        ctx.fill();
        ctx.stroke();
        
        ctx.font = 'bold 12px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'black';
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      }
    }
    
    
    
    /* MICKEY MOUSE!
    const midX = canvasWidth / 2;
    const midY = canvasHeight / 2;
    const pi = Math.PI;

    ctx.fillStyle = '#000000';
    // head
    ctx.beginPath();
    ctx.arc(midX, midY, 100, 0, 2 * pi);
    ctx.fill();
    ctx.stroke();
    // left ear
    ctx.beginPath();
    ctx.arc(midX - 100, midY - 110, 60, .43 * pi, .1 * pi);
    ctx.stroke();
    ctx.fill();
    // right ear
    ctx.beginPath();
    ctx.arc(midX + 100, midY - 110, 60, .9 * pi, .57 * pi);
    ctx.stroke();
    ctx.fill();
    // chin
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(midX, midY + 70, 50, 0, 2 * pi);
    ctx.stroke();
    ctx.fill();
    // left cheek
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX - 50, midY + 60, 65, 30, 1.20 * pi, 0, 2 * pi);
    ctx.stroke();
    ctx.fill();
    // right cheek
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX + 50, midY + 60, 65, 30, .8 * pi, 0, 2 * pi);
    ctx.stroke();
    ctx.fill();
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(midX, midY + 20, 50, 0, 2 * pi);
    ctx.fill();
    // chin fill to erase lines
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(midX, midY + 70, 50, 0, 2 * pi);
    ctx.fill();
    // left eye background
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX - 27, midY, 50, 85, 1.97 * pi, 0, 2 * pi);
    // ctx.stroke();
    ctx.fill();
    // right eye background
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX + 27, midY, 50, 85, .03 * pi, 0, 2 * pi);
    // ctx.stroke();
    ctx.fill();
    // left eye white
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX - 16, midY - 20, 10, 30, 1.98 * pi, 0, 2 * pi);
    ctx.stroke();
    ctx.fill();
    // right eye white
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX + 16, midY - 20, 10, 30, .02 * pi, 0, 2 * pi);
    ctx.stroke();
    ctx.fill();
    // left eye black
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(midX - 13, midY - 4, 7, 14, 0, 0, 2 * pi);
    ctx.stroke();
    ctx.fill();
    // right eye black
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(midX + 15, midY - 4, 7, 14, 0, 0, 2 * pi);
    ctx.stroke();
    ctx.fill();
    // above-nose arch
    ctx.beginPath();
    ctx.arc(midX, midY + 58, 50, 1.36 * pi, 1.64 * pi);
    ctx.stroke();
    // lower mouth
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(midX, midY + 42, 50, 65, 0, .15 * pi, .85 * pi);
    ctx.fill();
    // upper mouth
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX, midY + 20, 85, 60, 0, 0.075 * pi, 0.925 * pi);
    ctx.stroke();
    ctx.fill();
    // tongue left
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX - 12, midY + 98, 20, 10, .1 * pi, 0, 2 * pi);
    ctx.fill();
    // tongue right
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX + 16, midY + 99, 18, 10, .1 * pi, 0, 2 * pi);
    ctx.fill();
    // tongue cleft
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.ellipse(midX - 12, midY + 98, 20, 10, .1 * pi, 1 * pi, 1.75 * pi);
    ctx.stroke();
    // lower mouth outline
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(midX, midY + 42, 50, 65, 0, .15 * pi, .85 * pi);
    ctx.stroke();
    // nose
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.ellipse(midX, midY + 30, 25, 12, 0, 0, 2 * pi);
    ctx.fill();
    // left cheek arch
    ctx.beginPath();
    ctx.ellipse(midX - 78, midY + 38, 14, 5, 1.95 * pi, 1.1 * pi, 1.625 * pi);
    ctx.stroke();
    // right cheek arch
    ctx.beginPath();
    ctx.ellipse(midX + 78, midY + 38, 14, 5, .05 * pi, 1.325 * pi, 1.9 * pi);
    ctx.stroke();
    */
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
      graph: new Graph(),
      connectedComponents: [],
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.connectedComponents = this.state.graph.getConnectedComponents();
    // console.log(`Returned ${this.state.connectedComponents.length} connected components.`);
    // console.log(this.state.connectedComponents);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} connectedComponents={this.state.connectedComponents}></GraphView>
      </div>
    );
  }
}

export default App;
