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
    let startVertex;
    let endVertex;

    // Clear it

    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

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
        for (let edge of vertex.edges) {
          let randomWeight = Math.floor((Math.random() * 10) + 1);
          let middleX = (vertex.pos.x + edge.destination.pos.x) / 2;
          let middleY = (vertex.pos.y + edge.destination.pos.y) / 2;
          ctx.beginPath();
          ctx.arc(middleX, middleY, vertexRadius, 0, 2 * Math.PI);
          ctx.fillStyle = 'white';
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = 'black';
          ctx.font = '10px Arial';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(randomWeight, middleX, middleY);
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
          canvas.addEventListener('click', (e) => {
            const pos = {
              x: e.clientX - 150,
              y: e.clientY
            };
          if (isIntersect(pos, vertex.pos)) {
            console.log('clicked on circle: ', vertex.value);
            if (!startVertex) {
              startVertex = vertex;
              console.log('starting vertex: ', startVertex);
            } else if (endVertex){
              console.log('already selected a starting and ending vertex!!');
            } else {
              endVertex = vertex;
              console.log('ending vertex: ', endVertex);
            }
          }
          })
        }

        function isIntersect(cursorPos, circlePos) {
          return Math.sqrt((cursorPos.x - circlePos.x) ** 2 + (cursorPos.y - circlePos.y) ** 2) < vertexRadius;
        }
      })
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
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);
  }  


  clickHandler = () => {
    const newGraph = {
      graph: new Graph(),
    }
    newGraph.graph.randomize(5, 4, 150, 0.6);
    this.setState(newGraph);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.clickHandler}>Generate New Graph</button>
      </div>
    );
  }
}

export default App;
