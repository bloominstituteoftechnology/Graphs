import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';


// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 650;

const circleRadius = 15;

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
   * 
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
    ctx.fillStyle = 'teal';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font= '15px Ariel';
    ctx.textAlign = 'center';
    ctx.textBaseline= 'middle';

    const components = this.props.graph.getConnectedComponents();
    components.forEach((component) => {
      this.drawVertexes(ctx, component, this.generateRandomColor());
    });
  }
    drawVertexes(ctx, vertexes, color) {
      //draw the lines between vertexes
      ctx.strokeStyle = color;
    
    // draw the line between vertexes
    for(let vertex of vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
      }
    }

    for (let v of vertexes) {
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
      ctx.fill();
      ctx.stroke();

      //fill in the text
      ctx.fillStyle = 'black';
      ctx.fillText(v.value, v.pos.x, v.pos.y)
    }
  }

    //draw dummy vertex
    // this.props.graph.vertexes.forEach((v) => {
    //   ctx.beginPath();
    //   ctx.fillStyle ='red';
    //   ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2*Math.PI);
    //   ctx.fill();
    //   ctx.stroke();

    //   ctx.fillStyle = 'black';
    //   ctx.fillText(v.value, v.pos.x, v.pos.y)
    // });

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  generateRandomColor() {
    const letters = '01234567890ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++){
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
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
  }

  randomize = () => {
    const state = {
      graph: new Graph()
    };

    state.graph.randomize(5, 4, 150, 0.6);
    this.setState(state);
  };

  render() {
    return (
      <div className="App">
      
        <GraphView graph={this.state.graph}></GraphView>
        <div>
        <button onClick={this.randomize}> Rando! </button>
        </div>
      </div>
    );
  }
}

export default App;
