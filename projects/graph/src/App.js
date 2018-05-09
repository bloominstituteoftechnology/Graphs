import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

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
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
    grd.addColorStop(0, '#ffffff');
    grd.addColorStop(0.1, '#3c0045');
    grd.addColorStop(0.2, '#fe008d');
    grd.addColorStop(0.3, '#ff6a00');
    grd.addColorStop(0.4, '#fffc00');
    grd.addColorStop(0.5, '#70ff00');
    grd.addColorStop(0.6, '#00ff2e');
    grd.addColorStop(0.7, '#00b7ff');
    grd.addColorStop(0.8, '#9b0004');
    grd.addColorStop(0.9, '#cc7274');
    grd.addColorStop(1, '#ffffff');

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    let seen = [];

    //two edges create conflicting weights being written
    //
    function includes(arr,el) {
      for(let i = 0; i < arr.length; i++) {
        if(arr[i][0] === el[0] && arr[i][1] === el[1]) return true;
      }
      return false;
    }

    
    


    // Draw Edges
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let vertex = this.props.graph.vertexes[i];
      if (vertex.edges.length) {
        let edge = vertex.edges[0].destination.position;
        let midpoint = [(edge.x + vertex.position.x) / 2, (edge.y + vertex.position.y) / 2];
        if (includes(seen, midpoint) === false) {
          ctx.beginPath();
          ctx.moveTo(vertex.position.x, vertex.position.y);
          ctx.lineTo(edge.x, edge.y);
          ctx.stroke();
          //*Broken* Draw Weights
          let weight = vertex.edges[0].weight;
          ctx.strokeStyle = 'white';
          ctx.font = '15px Arial';
          ctx.fillStyle = 'black';
          ctx.fillText(weight, (edge.x + vertex.position.x) / 2, (edge.y + vertex.position.y) / 2);
          seen.push(midpoint);
          ctx.stroke();
        }
      }
    }

    
    


    // Draw Vertices
    for (let i = 0; i < this.props.graph.vertexes.length; i++) {
      let vertex = this.props.graph.vertexes[i];
      ctx.beginPath();
      ctx.arc(vertex.position.x, vertex.position.y, 10, 0, 2 * Math.PI);
      ctx.fillStyle = 'black';
      ctx.fill();
      ctx.stroke();
      ctx.strokeStyle = 'white';
      ctx.font = '10px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = 'white';
      ctx.fillText(vertex.value, vertex.position.x, vertex.position.y);
      ctx.stroke();
      ctx.closePath();
      console.log("Vertex: " + vertex.edges.destination);
    }
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
      foundConnections: '',
    };

    // this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.foundConnections = this.state.graph.bfs(this.state.graph.vertexes);
  }

  refreshPage() {
    window.location.reload();
  }

  render() {
    let style = {
      color: 'red',
      background: 'black',
      width: 200,
      height: 50,
      fontSize: 20,
    };

    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
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
