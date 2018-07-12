import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleRadius = 15;

/**
 * GraphView
 */
const buttonStyle = {
  backgroundColor: 'yellow',
  border: 'none',
    color: 'black',
    cursor:'pointer',
    padding: '7px 20px',
    textAlign: 'center',
    textDecoration: 'none',
    display: 'inline-block',
    fontSize: 12
}
class GraphView extends Component {
  constructor() {
    super()
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
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    this.props.graph.randomize(5, 4, 150, 0.6);
    function getRandomColor() {
      let letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
    const connectedComponents = this.props.graph.getConnectedComponents()
    for (let component of connectedComponents) {
      const curColor = getRandomColor();
      component.forEach((v, i) => {
        ctx.beginPath();
        ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
        ctx.fillStyle = curColor;
        ctx.fill();
        let length = v.edges.length;
        for (let i = 0; length > i; i++) {
          ctx.beginPath();
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(v.edges[i].destination.pos.x, v.edges[i].destination.pos.y);
          ctx.strokeStyle = curColor;
          ctx.stroke();
        }
        ctx.font = '15px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle'
        ctx.fillStyle = 'white';
        ctx.fillText(v.value, v.pos.x, v.pos.y)
      });
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
      graph: new Graph(),
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
  
  }
reload = () => {
  window.location.reload()
}
  render() {
    return (
      <div className="App">
      <button style={buttonStyle} onClick={this.reload}><h4>Reload</h4></button>
        <GraphView graph={this.state.graph} ></GraphView>
      </div>
    );
  }
}

export default App;
