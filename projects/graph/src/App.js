import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
let canvasWidth = 0;
let canvasHeight = 0;
const nodeSize = 15;
const randomizeFuncWidth = 5;
const randomizeFuncHeight = 5;
const randomizeFuncPxBox = 150;
const randomizeFuncProbability = 0.6;

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

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //
    // ─────────────────────────────────────────── FIBONACCI STUFF ─────

    ////////////////
    // Mod of Art //
    ////////////////
    // function fibonacci(num, memo) {
    //   memo = memo || {};

    //   if (memo[num]) return memo[num];
    //   if (num <= 1) return 1;

    //   return (memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo));
    // }

    // let points = [];
    // for (let i = 1; i <= 50; i++) {
    //   points.push(fibonacci(i));
    // }

    // let a = 0;
    // let c = 10;
    // for (let x = 0; x < canvasWidth; x += 10) {
    //   for (let y = 0; y < canvasHeight; y += 10) {
    //     if (a === 10) a = 0;
    //     if (c === 0) c = 10;
    //     const r = Math.sqrt(y * (x / 20)) % 255;
    //     const g = (Math.cos(x * y + Math.sin(y)) * 100) % 255;
    //     const b = (r * (y / (Math.PI * r)) + g) % 255;
    //     ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    //     ctx.fillRect(x, y, points[a++], points[c--]);
    //   }
    // }
    ////////////
    // MOD END//
    ////////////

    // ////////////////
    // // Fib Design //
    // ////////////////
    // let i = 0,
    //   j = 0,
    //   flag = true;
    // for (let x = 0; x < canvasWidth; x += 10) {
    //   for (let y = 0; y < canvasHeight; y += 10) {
    //     if (flag === true) {
    //       if (i > 40) i = 0;
    //       const r = points[i] % 250;
    //       const g = points[i + 1] % 250;
    //       const b = points[i + 2] % 255;
    //       ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    //       ctx.fillRect(x, y, points[i + 1] % 100, points[i + 2] % 100);
    //       i++;
    //     } else {
    //       const r = points[i + 2] % 255;
    //       const g = points[i + 1] % 255;
    //       const b = points[i] % 255;
    //     }
    //     j++;
    //     if (j > 50) {
    //       flag = !flag;
    //       j = 0;
    //     }
    //   }
    // }
    // ////////////
    // //FIB END//
    // ////////////
    // ─────────────────────────────────────────────────────── END ─────
    //

    //
    // ───────────────────────────────────────────── BEAUTIFUL ART ─────
    // for (let x = 0; x < canvasWidth; x++) {
    //   for (let y = 0; y < canvasHeight; y++) {
    //     const r = Math.sqrt(y * (x / 20)) % 255;
    //     const g = (Math.cos(x * y + Math.sin(y)) * 100) % 255;
    //     const b = (r * (y / (Math.PI * r)) + g) % 255;
    //     ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    //     ctx.fillRect(x, y, 1, 1);
    //   }
    // }
    // ─────────────────────────────────────────────────────── END ─────
    //

    //
    // ───────────────────────────────────────────────── SPACE ART ─────
    // ctx.beginPath();
    // for(let x = 0; x < canvasWidth; x++) {
    //   for(let y = 0; y < canvasHeight; y++) {
    //     const r = Math.cos((Math.sqrt(y)*Math.tan(x)*-x)) % 255;
    //     const b = Math.tan((Math.sqrt(y)*Math.tan(x)*x)) % 255;
    //     const g = (b + (r + (Math.PI/2))) % 255;

    //     ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
    //     ctx.fillRect(x, y, 1, 1);
    //   }
    // }

    // ctx.beginPath();
    // for(let i = 0; i < 50; i++) {
    //   ctx.strokeStyle = 'white';
    //   let x = (Math.cos(i)*canvasWidth);
    //   let y = (i)*10;
    //   x++;
    //   y++;
    //   const r = Math.cos((Math.sqrt(y)*Math.tan(x)*-x)) % 255;
    //   const g = 0;
    //   const b = 0;
    //   ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';

    //   ctx.arc((Math.cos(i)*canvasWidth), (i)*10, i, 0, Math.PI * 2);
    //   ctx.fill();
    //   ctx.stroke();
    //   ctx.closePath();
    // }
    // ─────────────────────────────────────────────────────── END ─────
    //

    //
    // ────────────────────────────────────────────── GET RANDOM COLORS ─────
    let connectedComponents = this.props.graph.getConnectedComponents();
    let colors = [];
    let r, g, b;
    for (let i = 0; i < connectedComponents.length; i++) {
      r = Math.floor(Math.random() * 155) + 100;
      g = Math.floor(Math.random() * 155) + 100;
      b = Math.floor(Math.random() * 155) + 100;
      colors.push({ r, g, b });
    }
    // ────────────────────────────────────────────── DRAW LINES ─────
    for (let [i, vertexGroup] of connectedComponents.entries()) {
      for (let vertex of vertexGroup) {
        if (vertex.edges.length) {
          for (let j = 0; j < vertex.edges.length; j++) {
            ctx.beginPath();
            ctx.moveTo(vertex.pos.x, vertex.pos.y);
            ctx.lineTo(
              vertex.edges[j].destination.pos.x,
              vertex.edges[j].destination.pos.y
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
            ctx.arc(xWeightPos, yWeightPos, nodeSize / 2, 0, Math.PI * 2);
            ctx.fillStyle = 'white';
            ctx.fill();
            ctx.fillStyle = 'black';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(vertex.edges[j].weight, xWeightPos, yWeightPos);
            console.log(vertex.edges[j].weight);
          }
        }
      }
    }
    // ──────────────────────────────────────────────── DRAW NODES ─────
    for (let [i, vertexGroup] of connectedComponents.entries()) {
      for (let vertex of vertexGroup) {
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, nodeSize, 0, Math.PI * 2);
        ctx.fillStyle =
          'rgb(' + colors[i].r + ', ' + colors[i].g + ', ' + colors[i].b + ')';
        ctx.fill();

        ctx.strokeStyle = 'black';
        ctx.stroke();

        ctx.fillStyle = 'black';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      }
    }
  }
  // ────────────────────────────────────────────────────────────────────── END ─────
  //

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

    this.state.graph.randomize(
      randomizeFuncWidth,
      randomizeFuncHeight,
      randomizeFuncPxBox,
      randomizeFuncProbability
    );
  }

  randomize = () => {
    this.state.graph.randomize(
      randomizeFuncWidth,
      randomizeFuncHeight,
      randomizeFuncPxBox,
      randomizeFuncProbability
    );
    this.setState({ reRender: !this.state.reRender });
  };

  render() {
    // Dump console data
    //this.state.graph.dump();

    // Find the required canvas size
    canvasWidth = 0;
    canvasHeight = 0;
    for (let vertex of this.state.graph.vertexes) {
      if (vertex.pos.x > canvasWidth) canvasWidth = vertex.pos.x;
      if (vertex.pos.y > canvasHeight) canvasHeight = vertex.pos.y;
    }
    canvasWidth += nodeSize * 3;
    canvasHeight += nodeSize * 3;

    return (
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
        className="App"
      >
        <div style={{ width: canvasWidth }}>
          <GraphView graph={this.state.graph} />
        </div>
        <button style={{ width: canvasWidth }} onClick={this.randomize}>
          Randomize
        </button>
      </div>
    );
  }
}

export default App;
