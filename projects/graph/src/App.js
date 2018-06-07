import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 1000; 
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
    // this.props.graph.bfs(this.props.graph.vertexes[0]);
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
    
    console.log('in updateCanvas', this.props.graph.vertexes);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';
    
    function makeDarkerBlue(colorString) {
      let split = colorString.split(",");
      let colors = [];
      
      // Parse color string 
      for (let i = 0; i < split.length; i++) {
        let color = '';
        for (let k = 0; k < split[i].length; k++) {
          if (!isNaN(parseInt(split[i][k], 10))) {
            color += split[i][k];
          }
        }
        colors.push(color);
      } 
      colors = colors.map(color => Math.floor(color -= color * .35));
      return "rgb(" + colors[0] + ", " + colors[1] + ", " + colors[2] + ")"; 
    }

    this.props.graph.vertexes.forEach(vertex => {
      let darkerBlueColor = makeDarkerBlue(vertex.color); 
      if (vertex.edges.length > 0) {
        // console.log("Edges: ", vertex.edges);
        vertex.edges.forEach(edge => {
          ctx.beginPath();
          ctx.lineWidth = 2.5;
          ctx.strokeStyle = darkerBlueColor;
          ctx.moveTo(edge.origin.x, edge.origin.y);
          ctx.lineTo(edge.destination.x, edge.destination.y);
          ctx.stroke();
        });
      }
    });

    this.props.graph.vertexes.forEach(vertex => {
      let darkerBlueColor = makeDarkerBlue(vertex.color);
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 15, 0, 2 * Math.PI)
      ctx.fillStyle = vertex.color;
      ctx.fill();
      ctx.strokeStyle = darkerBlueColor;
      ctx.stroke();
      ctx.fillStyle = darkerBlueColor;
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
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
    // this.state.graph.debugCreateTestData();
  }

  render() {
    this.state.graph.randomize(5, 4, 125, 0.6);
    this.state.graph.getConnectedComponents();
    
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={() => this.setState({ graph: new Graph() })}>New Graph</button>
      </div>
    );
  }
}

export default App;
