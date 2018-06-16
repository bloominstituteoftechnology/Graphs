import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';
import Refresh from './button';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

const circleSize = 15;
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
    ctx.fillStyle = '#E91E63';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // console.log('in updateCanvas', this.props.graph.vertexes);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '14px Arial';

    for (let vertex of this.props.graph.vertexes){
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let vertex of this.props.graph.vertexes) {
    ctx.beginPath();      
    ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
    ctx.fillStyle = vertex.color; // can make variable
    ctx.fill();
    ctx.fillStyle = 'black';
    ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    ctx.stroke();   
    }

    // let debugVertex = this.props.graph.vertexes[0];  changed variable to vertex

    
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges lines
    // draw verts shapes
    // draw vert values (labels)
        
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
    this.state.graph.randomize(5, 4, 150, 0.6);
    // this.state.graph.debugCreateTestData(); 

    // test bfs
    this.state.graph.getConnectedComponents();
  }

  handleClick = () => {
    const graph = window.location.reload();
    this.setState({ graph })
    console.log(this.state)
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <Refresh onClick={this.handleClick}/>
      </div>
    );
  }
}

export default App;
