import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 10;
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

    ctx.fillStyle = 'rgba(0, 0, 0, 0';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
      ctx.fillStyle = 'green';
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle='black';
      ctx.font = '10px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }

    function getRandomColor() {
      var letters = '0123456789ABCDEF';
      var color = '#';
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }

    // Drawing psuedocode
      // for each subarray, 
        // generate a random color
        // loop through and draw the edges
        // loop through and draw the vertexes

    // !!! IMPLEMENT ME
    // compute connected components
    const connectedComponents = this.props.graph.getConnectedComponents();
    // draw edges
    connectedComponents.forEach(vertexArray => {
      let randomColor = getRandomColor();
      for (let vertex of vertexArray) {
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.strokeStyle = randomColor;
          ctx.stroke();
        }
      }
        for (let vertex of vertexArray) {
          ctx.beginPath();
          ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
          ctx.fillStyle = randomColor;
          ctx.fill();
          ctx.stroke();
          
          // draw vert values (labels)
          ctx.fillStyle = 'black';
          ctx.font = '10px Arial';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
        }
      })
    }
    
    // draw verts
  //   connectedComponents.forEach(vertexArray => {
  //     let randomVertexColor = getRandomColor();
  //     for (let vertex of vertexArray) {
  //       ctx.beginPath();
  //       ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
  //       ctx.fillStyle = randomVertexColor;
  //       ctx.fill();
  //       ctx.stroke();
        
  //       // draw vert values (labels)
  //       ctx.fillStyle = 'black';
  //       ctx.font = '10px Arial';
  //       ctx.textAlign = 'center';
  //       ctx.textBaseline = 'middle';
  //       ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
  //     }
  //   })
  // }

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
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);
  }

  // clickHandler = () => {
  //   this.setState({ graph: new Graph() });    
  // }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        {/* <button onClick={this.clickHandler()}>Generate New Graph</button> */}
      </div>
    );
  }
}

export default App;
