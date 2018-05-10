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
  randomColor() {
    // Random hex generator borrowed from https://stackoverflow.com/questions/1484506/random-color-generator
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    // console.log(color);
    return color;
  };
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

    const radius = 10;
    // console.time('draw')
    const drawEdges = (edge, start, color) => {
      let { x, y } = edge.destination.pos;
      ctx.strokeStyle = color;
      ctx.shadowColor = color;
      ctx.shadowBlur = 1;
      ctx.beginPath();
      ctx.moveTo(start.x, start.y);
      ctx.lineTo(x, y);
      ctx.stroke();
      
      // if (edge.destination.edges.length > 0) {
      //   mapEdges(edge.destination.edges, '', 'black');
      // }
    };
    const mapEdges = (edges, start, color) => {
        edges.forEach((edge) => {
          drawEdges(edge, start, color);
        });
    };
    const drawNode = (value, pos, color) => {
      const ep = Math.PI * 2;
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.strokeStyle = color;
      ctx.arc(pos.x, pos.y, radius, 0, ep, false);
      ctx.fill();
      ctx.stroke();

      // Text
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '12px sans-serif';
      ctx.fillStyle = 'white';
      ctx.fillText(value, pos.x, pos.y);
    };
    const draw = (vert, type, color) => {
      // todo - generate random color to execute each time this is called
      if (type === 'single') {
        drawNode(vert.value, vert.pos, color);
      } else {
        // console.log(vert);
        vert.forEach((vertex, i) => {
          mapEdges(vertex.edges, vertex.pos, color);
        });

        vert.forEach((edge, i) => {
          // console.log(edge);
          drawNode(edge.value, edge.pos, color);
        });
      }
    };
    // console.timeEnd('draw')
    this.props.graph.vertexes.forEach((vertex) => { 
      if (vertex.edges.length === 0) {
        draw(vertex, 'single', this.randomColor());
      } else {
        const connectedArr = this.props.graph.getConnectedComponents(vertex);
        // console.log(connectedArr)
        draw(connectedArr, 'arr', this.randomColor());
      }
    });
    console.log(this.props.graph.count);
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

    this.state.graph.randomize(8, 8, 100, .5);
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
