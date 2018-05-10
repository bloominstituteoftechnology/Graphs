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
      let code = '#2';
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

    // Draw Edges
    //     for (let i = 0; i < this.props.graph.vertexes.length; i++) {
    //       let vertex = this.props.graph.vertexes[i];
    //       if (vertex.edges.length) {
    //         let edge = vertex.edges[0].destination.position;
    //         let midpoint = [(edge.x + vertex.position.x) / 2, (edge.y + vertex.position.y) / 2];
    //         if (includes(seen, midpoint) === false) {
    //           ctx.beginPath();
    //           ctx.moveTo(vertex.position.x, vertex.position.y);
    //           ctx.lineTo(edge.x, edge.y);
    //           ctx.stroke();
    //           //*Broken* Draw Weights
    //           let weight = vertex.edges[0].weight;
    //           ctx.strokeStyle = 'white';
    //           ctx.font = '15px Arial';
    //           ctx.fillStyle = 'black';
    //           ctx.fillText(weight, (edge.x + vertex.position.x) / 2, (edge.y + vertex.position.y) / 2);
    //           seen.push(midpoint);
    //           ctx.stroke();
    //         }
    //       }
    //     }
    // midpoints graphed already so two are not written
    let seen = [];

    //two edges create conflicting weights being written
    function includes(arr, el) {
      for (let i = 0; i < arr.length; i++) {
        if (arr[i][0] === el[0] && arr[i][1] === el[1]) return true;
      }
      return false;
    }

    connections.forEach((connection, index) => {
      let color = rando();
      //Draw Edges
      connection.forEach((vert) => {
        vert.edges.forEach((edge) => {
          let destination = edge.destination.position;
          let midpoint = [(destination.x + vert.position.x) / 2, (destination.y + vert.position.y) / 2];
          if (includes(seen, midpoint) === false) {
            ctx.beginPath();
            ctx.strokeStyle = color;
            ctx.moveTo(vert.position.x, vert.position.y);
            ctx.lineTo(destination.x, destination.y);
            ctx.stroke();

            let x = Math.abs(destination.x - vert.position.x);
            let y = Math.abs(destination.y - vert.position.y);

            edge.weight = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)).toFixed(1);
            ctx.strokeStyle = 'white';
            ctx.font = '15px Arial';
            ctx.fillStyle = 'black';
            ctx.fillText(
              edge.weight,
              (destination.x + vert.position.x) / 2,
              (destination.y + vert.position.y) / 2
            );
            seen.push(midpoint);
            ctx.stroke();
          }
        });
      });
      //Draw Vertices
      connection.forEach((vert) => {
        ctx.beginPath();
        ctx.arc(vert.position.x, vert.position.y, 10, 0, 2 * Math.PI);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.strokeStyle = color;
        ctx.stroke();
        ctx.fillStyle = 'white';
        ctx.font = '10px Arial';
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

  refreshPage() {
    window.location.reload();
  }

  render() {
    let style = {
      color: 'lightblue',
      background: 'purple',
      width: 200,
      height: 50,
      fontSize: 20,
    };

    return (
      <div className="App">
        <GraphView graph={this.state.graph} foundConnections={this.state.foundConnections} />
        <div>
          <button type="button" style={style} onClick={this.refreshPage}>
            Refresh{' '}
          </button>
        </div>
      </div>
    );
  }
}

export default App;
