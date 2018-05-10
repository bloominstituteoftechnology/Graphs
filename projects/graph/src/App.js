import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
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
    function rando() {
      let code = '#3';
      for (let i = 0; i < 5; i++) {
          code += Math.floor(Math.random() * 9);
      }
      return code;
    }
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
    grd.addColorStop(0, '#c07a7a');
    grd.addColorStop(0.1, '#b17ac0');
    grd.addColorStop(0.2, '#c07a7a');
    grd.addColorStop(0.3, '#667ee4');
    grd.addColorStop(0.4, '#c07a7a');
    grd.addColorStop(0.5, '#b17ac0');
    grd.addColorStop(0.6, '#c07a7a');
    grd.addColorStop(0.7, '#667ee4');
    grd.addColorStop(0.8, '#c07a7a');
    grd.addColorStop(0.9, '#b17ac0');
    grd.addColorStop(1, '#c07a7a');

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    let connections = this.props.foundConnections;

    connections.forEach((connection, index) => {
      let color = rando();
      //Draw Edges
      connection.forEach((vert) => {
        vert.edges.forEach((edge) => {
          ctx.beginPath();
          ctx.strokeStyle = color;
          ctx.moveTo(vert.position.x, vert.position.y);
          ctx.lineTo(edge.destination.position.x, edge.destination.position.y);
          ctx.stroke();
        });
      });
      //Draw Vertices
      connection.forEach((vert) => {
        ctx.beginPath();
        ctx.arc(vert.position.x, vert.position.y, 12, 0, 2 * Math.PI);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.strokeStyle = color;
        ctx.stroke();
        ctx.fillStyle = 'white';
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vert.value, vert.position.x, vert.position.y);
      });
    });
  }

  /**
   * Render
   */
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
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
      foundConnections: [],
    };

    this.state.graph.randomize(5, 4, 150, 0.6);
    for (let i = 0; i < this.state.graph.vertexes.length; i++) {
      if (this.state.graph.vertexes[i].edges.length > 0) {
        let result = this.state.graph.bfs(this.state.graph.vertexes[i]);
        if (result) {
          this.state.foundConnections.push(result);
        }
      } else {
        this.state.foundConnections.push([this.state.graph.vertexes[i]]);
      }
    }
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} foundConnections={this.state.foundConnections} />
      </div>
    );
  }
}

export default App;
