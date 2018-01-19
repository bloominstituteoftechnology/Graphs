import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 1000;

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

  // adopted from https://stackoverflow.com/questions/1484506/random-color-generator
  randomColor() {
    return "#" + ('00000'+(Math.random()*(1<<24)|0).toString(16)).slice(-6);
  }

  // adopted from https://stackoverflow.com/questions/12043187/how-to-check-if-hex-color-is-too-black
  isDark(color) {
    const c = color.substring(1);
    const rgb = parseInt(c, 16);  
    const r = (rgb >> 16) & 0xff; 
    const g = (rgb >>  8) & 0xff; 
    const b = (rgb >>  0) & 0xff;
    const luma = 0.2126 * r + 0.7152 * g + 0.0722 * b;
    return luma < 125;
  }

  // used to determine the start and end coordinates of edges
  findPosition = (startX, startY, endX, endY) => {
    const deltaX = endX - startX;
    const deltaY = endY - startY;
    const radians = Math.atan2(deltaY, deltaX);
    const distance = 23;
    const posX = distance * Math.cos(radians) + startX;
    const posY = distance * Math.sin(radians) + startY;
    return [posX, posY];
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    ctx.font = "20px serif";
    ctx.textAlign = "center";
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
 
    const connectedComponents = this.props.graph.getConnectedComponents();

    // set each vertex's color
    for(let i = 0; i < connectedComponents.length; i++) {
      const color = this.randomColor();
      for(let j = 0; j < connectedComponents[i].length; j++) {
        connectedComponents[i][j].color = color;
      }
    }

    const midpoints = []; 

    for(let i = 0; i < this.props.graph.vertexes.length; i++) {
      const color = this.props.graph.vertexes[i].color;
      ctx.beginPath();
      // draw vertex
      ctx.fillStyle = color;
      ctx.arc(this.props.graph.vertexes[i].pos.x, this.props.graph.vertexes[i].pos.y, 25, 0, 2*Math.PI);
      ctx.fill();
      // draw vertex's value
      ctx.strokeStyle = color;
      ctx.stroke();
      ctx.fillStyle = this.isDark(this.props.graph.vertexes[i].color) ? 'white' : 'black';
      ctx.fillText(this.props.graph.vertexes[i].value, this.props.graph.vertexes[i].pos.x, this.props.graph.vertexes[i].pos.y); 
      // draw edges between this vertex and its neighbors
      for(let j = 0; j < this.props.graph.vertexes[i].edges.length; j++) {
        ctx.beginPath();
        const start = this.findPosition(this.props.graph.vertexes[i].pos.x, this.props.graph.vertexes[i].pos.y, this.props.graph.vertexes[i].edges[j].destination.pos.x, this.props.graph.vertexes[i].edges[j].destination.pos.y);
        const end = this.findPosition(this.props.graph.vertexes[i].edges[j].destination.pos.x, this.props.graph.vertexes[i].edges[j].destination.pos.y, this.props.graph.vertexes[i].pos.x, this.props.graph.vertexes[i].pos.y);
        const xAverage = (end[0] + start[0]) / 2;
        const yAverage = (end[1] + start[1]) / 2;
        if(!midpoints.includes(JSON.stringify({x: xAverage, y: yAverage}))) { // only draw 1 edge between connected vertexes
          // draw edge
          ctx.moveTo(start[0], start[1]);
          ctx.lineTo(end[0], end[1]);
          ctx.strokeStyle = color;
          ctx.stroke();

          // draw weight
          const xDifference  = end[0] - start[0];
          const yDifference  = end[1] - start[1];  
          midpoints.push(JSON.stringify({x: xAverage, y: yAverage}));
          ctx.fillStyle = "black";
          ctx.textBaseline = "bottom";
          ctx.translate(xAverage, yAverage);
          if(xDifference < 0){
            ctx.rotate(Math.atan2(yDifference, xDifference) - Math.PI); // make sure weight isn't upside down
          }
          else {
            ctx.rotate(Math.atan2(yDifference, xDifference));
          }
          ctx.fillText(this.props.graph.vertexes[i].edges[j].weight, 0, 0);
          ctx.resetTransform();
        }   
      }
    }
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

    this.randomizeGraph = this.randomizeGraph.bind(this);

    this.state.graph.randomize(5, 4, 150, 0.5);
  }

  randomizeGraph() {
    const newGraph = new Graph();
    newGraph.randomize(5, 4, 150, 0.5);
    this.setState({graph: newGraph});
  }

  render() {
    return (
      <div className="App" >
        <p onClick={this.randomizeGraph}>Click here to randomize graph</p>
        <GraphView graph={this.state.graph} ></GraphView>
      </div>
    );
  }
}

export default App;
