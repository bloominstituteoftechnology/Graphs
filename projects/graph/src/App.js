import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750
const canvasHeight = 600

const invertColor = (hex) => {
  if (hex.indexOf('#') === 0) {
      hex = hex.slice(1);
  }
  if (hex.length === 3) {
      hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
  }
  if (hex.length !== 6) {
      throw new Error('Invalid HEX color.');
  }
  var r = (255 - parseInt(hex.slice(0, 2), 16)).toString(16),
      g = (255 - parseInt(hex.slice(2, 4), 16)).toString(16),
      b = (255 - parseInt(hex.slice(4, 6), 16)).toString(16);
  return '#' + padZero(r) + padZero(g) + padZero(b);
}

const padZero = (str, len) => {
  len = len || 2;
  var zeros = new Array(len).join('0');
  return (zeros + str).slice(-len);
}


/**
 * GraphView
 */
class GraphView extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph(),
      hover: null
    };
    
    this.state.graph.randomize(5, 4, 150, 0.6)
    console.log(this.state.graph)
  }
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
    const graph = this.state.graph
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    ctx.font="20px Georgia";
    ctx.textAlign = "center";
    
    

    const connectedGraph = graph.getConnectedComponents()
    ctx.lineWidth = 2;
    for (let i = 0; i < connectedGraph.length; i++) {
      const getRandomColor = () => {
        var letters = '0123456789ABCDEF';
        var color = '#';
        for (var i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
      }
      let color = getRandomColor()
      let color2 = invertColor(color)
      for (let x = 0; x < connectedGraph[i].length; x++) {
        ctx.strokeStyle = color
        let vertex = connectedGraph[i][x];
        for (let y = 0; y < vertex.edges.length; y++) {
          const findPos = (startX, startY, endX, endY, distance = 0) => {
            const deltaX = endX - startX;
            const deltaY = endY - startY;
            if (distance === 0) {
              distance = Math.sqrt((deltaX * deltaX) + (deltaY + deltaY)) / 2
            }
            const rad = Math.atan2(deltaY, deltaX);
            const posX = (distance) * Math.cos(rad) + startX
            const posY = (distance) * Math.sin(rad) + startY
            return [posX, posY]
          }
          
          let edge = vertex.edges[y].destination;
          let start = findPos(vertex.pos.x, vertex.pos.y, edge.pos.x, edge.pos.y, 20)
          let end = findPos(edge.pos.x, edge.pos.y, vertex.pos.x, vertex.pos.y, 20)
          let weightXY = [(vertex.pos.x + edge.pos.x)/2, (vertex.pos.y + edge.pos.y)/2]
          ctx.beginPath();
          
          ctx.moveTo(start[0], start[1]);
          ctx.lineTo(end[0], end[1]);
          ctx.stroke();

          ctx.beginPath();
          ctx.fillStyle = color
          ctx.ellipse(weightXY[0], weightXY[1], 8, 8,  2*Math.PI, 2*Math.PI,  0,  2*Math.PI)
          ctx.fill()
          ctx.stroke()
          ctx.font="12px Monospace";
          ctx.fillStyle = color2
          ctx.fillText(vertex.edges[y].weight, weightXY[0], weightXY[1] + 4);
          ctx.fillStyle = color
        }
        ctx.beginPath()
        
        ctx.arc(vertex.pos.x, vertex.pos.y, 20, 0, 2*Math.PI)
        ctx.fillStyle = color2
        ctx.fill()
        ctx.stroke()
        ctx.fillStyle = color
        ctx.strokeStyle = color
        ctx.font="20px Georgia";
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y + 6);
        ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y + 6);
      }
    }
  }
  
  handleButton() {
    let newGraph = new Graph()
    newGraph.randomize(5, 4, 150, 0.6)
    this.setState({
      graph: newGraph
    })
  }

  handleMouse(e) {
    let vertexes = this.state.graph.vertexes
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    let posX = (e.pageX - ((window.outerWidth - 750) / 2) + 49)
    let posY = e.pageY
    //if posX > nodeX-15 && posX < nodeX15
    for (let i = 0; i < vertexes.length; i++) {
      let vertex = vertexes[i];
      let x = vertex.pos.x
      let y = vertex.pos.y
      if (posX > x - 15 && posX < x + 15 && posY > y - 15 && posY < y + 15) {
        this.setState({
          hover: vertex
        })
      }
    }
  }
  /**
   * Render
   */
  render() {
    return(
      <div>
        <canvas onMouseMove={this.handleMouse.bind(this)} ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
        <button onClick={this.handleButton.bind(this)}>new graph!</button>
      </div>
    )
  }
}


/**
 * App
 */
class App extends Component {



  render() {
    
    return (
      <div className="App">
        <GraphView></GraphView>
      </div>
    );
  }
}

export default App;
