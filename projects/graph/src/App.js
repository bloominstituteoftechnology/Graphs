import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const xCount = 8;
const yCount = 8;
const boxSize = 100;
const prob = 0.4;

const canvasWidth = xCount * boxSize;
const canvasHeight = yCount * boxSize;
const radius = boxSize / 7;

/**
 * GraphView
 */
class GraphView extends Component {
  componentWillMount() {
    const image = new Image();
    image.addEventListener('load', () => {
      this.setState({
        image: image
      });
    }, false);
    image.src = 'images/potato.png';
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
    if (this.state === null)
      return;
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    const cache = {};
    let chainCount = 0;

    const colors = [
      '#303868',
      '#9C6282',
      '#BB5343',
      '#49B5B3',
      '#2E80D0',
      '#C58239',
      '#86C13D',
      '#B14D80',
      '#47B779',
      '#8D4BB3',
      '#C7C037',
      '#36B8C8',
      '#CF2F32',
      '#9F25D9',
      '#2BD1D3',
      '#50C737',
      '#C44A3A',
      '#3273CC',
    ];

    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const drawConnections = (potato) => {

      if (cache[potato.value] === true)
        return;


      const drawpotato = (potato) => {
        ctx.beginPath();
        ctx.ellipse(potato.pos.x, potato.pos.y, radius, radius, 0, 0, 2 * Math.PI);
        // ctx.drawImage(this.state.image, potato.pos.x - 20, potato.pos.y - 25, 40, 50);
        ctx.fillStyle = colors[chainCount + 1] || colors[0];
        ctx.lineWidth = 3;
        ctx.strokeStyle = colors[chainCount];
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.textAlign="center";
        ctx.font = "12px Sans-serif"
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 4;
        ctx.strokeText(potato.value, potato.pos.x, potato.pos.y + 5);
        ctx.fillStyle = 'white';
        ctx.fillText(potato.value, potato.pos.x, potato.pos.y + 5);
        ctx.stroke();
      };

      const connectpotatos = (potato1, potato2) => {
        ctx.beginPath();
        ctx.moveTo(potato1.pos.x, potato1.pos.y);
        ctx.lineTo(potato2.pos.x, potato2.pos.y);
        ctx.strokeStyle = colors[chainCount];
        ctx.lineWidth = 4;
        ctx.stroke();
      }

      const drawEdges = (potato) => {
        if (cache[potato.value] === true)
          return false;
        cache[potato.value] = true;
        if (!potato.isConnected()) {
          drawpotato(potato);
          return true;
        }
        potato.edges.forEach((edge) => {
          connectpotatos(potato, edge.destination);
          drawEdges(edge.destination);
          drawpotato(potato);
          drawpotato(edge.destination);
        });
        return true;
      }

      if (drawEdges(potato)) {
        if (++chainCount >= colors.length)
          chainCount = 0;
      }

    };

    for (let potato of this.props.graph.potatices)
      drawConnections(potato);
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
  }
}


/**
 * App
 */
class App extends Component {
  componentWillMount() {
    const graph = new Graph();
    graph.randomize(xCount, yCount, boxSize, prob);
    this.setState({
      graph: graph
    })
  }

  render() {
    return (
      <div className="App">
        <GraphView ref="graph" graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
