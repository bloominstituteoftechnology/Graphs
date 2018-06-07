import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 900;
const canvasHeight = 1000;
const circleSize = 20;

/**
 * GraphView
 */
class GraphView extends Component {
  state = {
    originClick: null,
    destinationClick: null,
  }
  /**
   * On mount
   */
  componentDidMount() {
    this.props.graph.randomize(10, 10, 80);
    this.props.graph.getConnectedComponents();
    this.updateCanvas();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvas();
  }

  /**f
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'white  ';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //function to determin midpoint of edge
    const midpoint = (pointA, pointB) => {
      const x = ((pointA.x + pointB.x)/2);
      const y = ((pointA.y + pointB.y)/2);
      return {x, y};
    }
    ctx.beginPath();
    this.props.graph.vertexes.forEach((vertex, index, array) => {
      vertex.edges.forEach(edge => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        const weightPosition = midpoint(vertex.pos, edge.destination.pos);
        ctx.textAlign = 'right';
        ctx.textBaseline = 'top';
        ctx.font = '14px Arial';
        ctx.fillStyle = 'blue';
        ctx.fillText(edge.weight, weightPosition.x, weightPosition.y);
      });
    });
    ctx.closePath();

    this.props.graph.vertexes.forEach((vertex, index, array) => {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = vertex.color || 'white';
      ctx.fill();
      ctx.stroke();
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '16px Arial';
      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.closePath();
    });
  }

  clickHandler(event) {
    const canvasPosition = this.refs.canvas.getBoundingClientRect();
    const clickPosition = { x: event.clientX - canvasPosition.left, y: event.clientY - canvasPosition.top }
    const clickedVertex = this.props.graph.vertexes.find(vertex => {
      return Math.abs(vertex.pos.x - clickPosition.x) < circleSize && Math.abs(vertex.pos.y - clickPosition.y) < circleSize;    
    });
    if (!clickedVertex) return;
    if (!this.state.originClick || this.state.destinationClick) {
      this.setState({
        originClick: clickedVertex,
        destinationClick: null,
      });
    } else if (!this.state.destinationClick){
      this.setState({
        destinationClick: clickedVertex,
      });
      console.log('Origin: ', this.state.originClick.value, 'Destination ', clickedVertex.value);
    }
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
        <button onClick={() => this.componentDidMount()}
          style = {{
            position: 'absolute',
            top: 850,
            right: 600,
            height: '50px'
          }}
          >Create New Graph</button>
        <canvas onClick={this.clickHandler.bind(this)} ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
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
