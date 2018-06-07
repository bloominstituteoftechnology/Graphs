import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
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

    // Vertex click event
    let start;
    let end;

    canvas.addEventListener(
      'click',
      e => {
        const x = e.pageX - canvas.offsetLeft;
        const y = e.pageY - canvas.offsetTop;
        let vertClick;

        for (let vertex of this.props.graph.vertexes) {
          if (
            Math.abs(vertex.pos.x - x) <= circleSize &&
            Math.abs(vertex.pos.y - y) <= circleSize
          ) {
            vertClick = vertex;
            if (!start) {
              start = vertClick;

              ctx.textAlign = 'center';
              ctx.textBaseline = 'middle';
              ctx.font = '16px Arial';
              ctx.fillStyle = 'black';

              ctx.fillText('START', vertex.pos.x, vertex.pos.y + 20);
            } else if (!end) {
              end = vertClick;
              ctx.textAlign = 'center';
              ctx.textBaseline = 'middle';
              ctx.font = '16px Arial';
              ctx.fillStyle = 'black';

              ctx.fillText('END', vertex.pos.x, vertex.pos.y + 20);
              console.log(`Start at: ${start.value} and End at: ${end.value}`);
            }
          }
        }
      },
      false
    );

    // Clear it
    ctx.fillStyle = 'rgb(0, 206, 209)';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    console.log('in updateCanvas', this.props.graph.vertexes);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.strokeStyle = vertex.fillColor;
        ctx.stroke();

        // Add edge weight.
        const xCenter = (vertex.pos.x + edge.destination.pos.x) / 2;
        const yCenter = (vertex.pos.y + edge.destination.pos.y) / 2;
        ctx.font = '25px Arial';
        ctx.fillStyle = 'black';
        if (edge.drawWeight === false) {
          ctx.fillText(edge.weight, xCenter + 8, yCenter + 8);
        } else {
          continue;
        }
      }
    }

    for (let vertex of this.props.graph.vertexes) {
      ctx.strokeStyle = vertex.fillColor;
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = vertex.fillColor;
      ctx.fill();
      ctx.fillStyle = 'black';
      ctx.font = '16px Arial';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.stroke();
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
    };
    // this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.getConnectedComponents();
  }

  handleClick() {
    const newGraph = { graph: new Graph() };
    newGraph.graph.randomize(5, 4, 150, 0.6);
    newGraph.graph.getConnectedComponents();
    this.setState(newGraph);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <div className="btnDiv">
          <div className="Button" onClick={() => this.handleClick()}>
            New Graph
          </div>
        </div>
      </div>
    );
  }
}

export default App;
