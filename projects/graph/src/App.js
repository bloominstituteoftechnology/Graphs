import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

let canvasWidth = window.innerWidth;
let canvasHeight = window.innerHeight;
// !!! IMPLEMENT ME

/**
 * GraphView
 */
class GraphView extends Component {
  state = {
    canvasWidth: window.outerWidth,
    canvasHeight: window.outerHeight,
  };
  updateSize = (() => {
    setTimeout(
      window.addEventListener('resize', () => {
        this.setState({
          canvasWidth: window.outerWidth,
          canvasHeight: window.outerHeight,
        });
      }),
      500
    );
  })();
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
    // Clear it

    var gradient = ctx.createLinearGradient(
      canvasWidth / 2,
      0,
      canvasWidth / 2,
      canvasHeight
    );
    gradient.addColorStop(0, '#a18cd1');
    gradient.addColorStop(1, '#fbc2eb');

    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, this.state.canvasWidth, this.state.canvasHeight);

    const radius = 20;
    // console.time('draw')
    const drawEdges = (edge, start, color) => {
      let { x, y } = edge.destination.pos;
      ctx.strokeStyle = color;
      ctx.beginPath();
      ctx.moveTo(start.x, start.y);
      ctx.lineTo(x, y);
      ctx.stroke();
      if (edge.destination.edges.length > 0) {
        mapEdges(edge.destination.edges);
      }
    };
    const mapEdges = (edges, pos, color) => {
      if (pos !== undefined) {
        edges.forEach((edge) => {
          drawEdges(edge, pos, color);
        });
      }
    };
    const drawNode = (vertex, color) => {
      const ep = Math.PI * 2;
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, ep, false);
      ctx.fill();
      ctx.stroke();

      // Text
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '12px sans-serif';
      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    };
    const draw = (vert, type) => {
      // todo - generate random color to execute each time this is called
      if (type === 'single') {
        drawNode(vert, color);
      } else {
        vert.forEach((vertex, i) => {
          mapEdges(vertex.edges, vertex.pos, color)
        });
        vert.forEach((vertex, i) => {
          drawNode(vertex, color);
        });
      }
    };
    // console.timeEnd('draw')
    this.props.graph.vertexes.forEach((vertex) => {
      if (vertex.edges.length === 0) {
        draw(vertex, 'single');
        this.props.graph.visited.push(vertex.value);
        console.log(this.props.graph.visited)
      }
      else this.props.graph.getConnectedComponents(vertex)/*, 'arr', 'blue'*/;
    });
  }

  /**
   * Render
   */
  render() {
    return (
      <canvas
        ref="canvas"
        width={this.state.canvasWidth}
        height={this.state.canvasHeight}
      />
    );
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
    this.state.graph.randomize(5, 4, 200, 0.3);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
