import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const randomizeHeight = 4;
const randomizeWidth = 5;
const boxSize = 150;
const canvasWidth = boxSize * randomizeWidth;
const canvasHeight = boxSize * randomizeHeight;

const vertexRadius = 10;
/**
 * GraphView
 */
class GraphView extends Component {
  state = {
    update: true,
  };
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

  isIntersect = (point, connectedComponents) => {
    for (let vertexGroup of connectedComponents) {
      for (let vertex of vertexGroup) {
        if (
          Math.sqrt(
            (point.x - vertex.pos.x) ** 2 + (point.y - vertex.pos.y) ** 2,
          ) < vertexRadius
        )
          return vertex.value;
      }
    }
    return false;
  };

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = '#e8ebef';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    var grd = ctx.createLinearGradient(0, 500, 0, 0);
    grd.addColorStop(0, '#000000');
    grd.addColorStop(1, '#028187');

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    let connectedComponents = this.props.graph.getConnectedComponents();
    let colors = [];
    let r, g, b;
    for (let i = 0; i < connectedComponents.length; i++) {
      r = Math.floor(Math.random() * 155);
      g = Math.floor(Math.random() * 155);
      b = Math.floor(Math.random() * 155);
      colors.push({ r, g, b });
    }

    for (let [i, vertexGroup] of connectedComponents.entries()) {
      for (let vertex of vertexGroup) {
        if (vertex.edges.length) {
          for (let j = 0; j < vertex.edges.length; j++) {
            ctx.beginPath();
            ctx.moveTo(vertex.pos.x, vertex.pos.y);
            ctx.lineTo(
              vertex.edges[j].destination.pos.x,
              vertex.edges[j].destination.pos.y,
            );
            ctx.strokeStyle =
              'rgb(' +
              colors[i].r +
              ', ' +
              colors[i].g +
              ', ' +
              colors[i].b +
              ')';
            ctx.lineWidth = vertex.edges[j].weight * 0.5;
            ctx.stroke();

            ctx.beginPath();
            let xWeightPos =
              (vertex.pos.x + vertex.edges[j].destination.pos.x) / 2;
            let yWeightPos =
              (vertex.pos.y + vertex.edges[j].destination.pos.y) / 2;
            ctx.arc(xWeightPos, yWeightPos, vertexRadius / 2, 0, Math.PI * 2);
            ctx.fillStyle = 'white';
            ctx.fill();
            ctx.fillStyle = 'black';
            ctx.font = '8px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(vertex.edges[j].weight, xWeightPos, yWeightPos);
          }
        }
      }
    }

    for (let [i, vertexGroup] of connectedComponents.entries()) {
      for (let vertex of vertexGroup) {
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, Math.PI * 2);
        ctx.fillStyle =
          'rgb(' + colors[i].r + ', ' + colors[i].g + ', ' + colors[i].b + ')';
        ctx.fill();

        ctx.strokeStyle = 'white';
        ctx.lineWidth = 1;
        ctx.stroke();

        ctx.fillStyle = 'white';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      }
    }

    canvas.addEventListener('click', e => {
      const x = e.clientX - canvas.offsetLeft;
      const y = e.clientY - canvas.offsetTop;
      const mousePoint = { x, y };

      let clickedVertex = this.isIntersect(mousePoint, connectedComponents);
      if (clickedVertex) {
        console.log('SUCCESS: ', clickedVertex);
      }
    });

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
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
      reRender: true,
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(randomizeWidth, randomizeHeight, boxSize);
  }
  randomize = () => {
    this.state.graph.randomize(randomizeWidth, randomizeHeight, boxSize);
    this.setState({ reRender: !this.state.reRender });
  };

  render() {
    this.state.graph.dump();
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <button style={{ width: canvasWidth }} onClick={this.randomize}>
          Randomize
        </button>
      </div>
    );
  }
}

export default App;
