import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

const canvasWidth = 860;
const canvasHeight = 720;

function getRandomColor() {
  const r = Math.round(Math.random() * 255);
  const g = Math.round(Math.random() * 255);
  const b = Math.round(Math.random() * 255);

  return `rgb(${r}, ${g}, ${b})`;
}

/**
 * GraphView
 */
class GraphView extends Component {
  constructor(props) {
    super(props);

    this.state = {
      components: null,
      hitCanvas: null,
      startV: null,
      endV: null,
      path: null,
      colorHash: {}
    };
  }

  async componentWillReceiveProps(nextProps) {
    await this.setState({
      components: nextProps.graph.getConnectedComponents(),
      startV: null,
      endV: null,
      path: null
    });
    this.setColorHash();
  }

  /**
   * On mount
   */
  async componentDidMount() {
    // Create a hidden canvas to eat the clicks and determine which vertex was clicked on
    const state = {
      components: this.props.graph.getConnectedComponents(),
      hitCanvas: document.createElement("canvas")
    };
    state.hitCanvas.setAttribute("height", canvasHeight);
    state.hitCanvas.setAttribute("width", canvasWidth);

    await this.setState(state);
    this.setColorHash();
    this.updateCanvas();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvas();
  }

  // colorHash is used to quickly look up which vertex was clicked. Click handler looks at colors
  // of vertexes on hidden canvas. Each vertex corresponds to a color in the hash.
  setColorHash = () => {
    const colorHash = {};
    this.state.components.forEach(c => {
      c.forEach(v => {
        while (true) {
          const colorKey = getRandomColor();
          if (!colorHash[colorKey]) {
            v.colorKey = colorKey;
            colorHash[colorKey] = v;
            break;
          }
        }
      });
    });
    this.setState({ colorHash });
  };

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");

    let hitCtx = this.state.hitCanvas.getContext("2d");

    // Clear it
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    hitCtx.fillStyle = "white";
    hitCtx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw edges
    for (let c of this.state.components) {
      if (!c.edgeColor) {
        c.edgeColor = getRandomColor();
      }
      const drawnLines = [];
      for (let v of c) {
        v.edges.forEach(e => {
          const xAvg = (v.pos.x + e.destination.pos.x) / 2;
          const yAvg = (v.pos.y + e.destination.pos.y) / 2;
          // Save midpoint of line to check if that edge has already been drawn
          // if it has, skip it.
          const midPoint = `${xAvg}, ${yAvg}`;
          if (drawnLines.indexOf(midPoint) === -1) {
            drawnLines.push(midPoint);
            ctx.beginPath();
            ctx.moveTo(v.pos.x, v.pos.y);
            ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
            ctx.strokeStyle = c.edgeColor;
            ctx.lineWidth = 3;
            ctx.stroke();

            // Put weight labels on edge, and position them relative to the line
            const xP = e.destination.pos.x - v.pos.x;
            const yP = e.destination.pos.y - v.pos.y;
            const normLen = ~~Math.sqrt(xP * xP + yP * yP);
            const xN = xP / normLen;
            const yN = yP / normLen;

            ctx.fillStyle = "black";
            ctx.font = "15px sans-serif";
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
            ctx.translate(xAvg + xN, yAvg + yN);
            ctx.rotate(Math.atan2(yP, xP));
            ctx.fillText(e.weight, 0, 0);
            ctx.resetTransform();
          }
        });
      }
    }

    if (this.state.path) {
      this.state.path.forEach((v, i, arr) => {
        if (i === arr.length - 1) {
          return;
        }
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(arr[i + 1].pos.x, arr[i + 1].pos.y);
        ctx.strokeStyle = "yellow";
        ctx.lineWidth = 5;
        ctx.stroke();
      });
    }

    // draw verts
    // draw vert values (labels)
    this.state.components.forEach(c => {
      c.forEach(v => {
        if (
          v === this.state.startV ||
          v === this.state.endV ||
          (this.state.path && this.state.path.includes(v))
        ) {
          ctx.beginPath();
          ctx.arc(v.pos.x, v.pos.y, 15, 0, 2 * Math.PI);
          ctx.strokeStyle = "yellow";
          ctx.stroke();
          ctx.fillStyle = "yellow";
          ctx.fill();
        } else {
          ctx.beginPath();
          ctx.arc(v.pos.x, v.pos.y, 15, 0, 2 * Math.PI);
          ctx.strokeStyle = "skyblue";
          ctx.stroke();
          ctx.fillStyle = "skyblue";
          ctx.fill();

          // Draw vertexes with unique colors to hidden hitCanvas.
          hitCtx.beginPath();
          hitCtx.arc(v.pos.x, v.pos.y, 15, 0, 2 * Math.PI);
          hitCtx.strokeStyle = v.colorKey;
          hitCtx.stroke();
          hitCtx.fillStyle = v.colorKey;
          hitCtx.fill();
        }

        ctx.fillStyle = "black";
        ctx.font = "12px sans-serif";
        ctx.fillText(v.value, v.pos.x, v.pos.y + 5);
      });
    });
  }

  handleClick = async e => {
    e.preventDefault();
    let canvasRect = this.refs.canvas.getBoundingClientRect();
    const mousePos = {
      x: e.clientX - canvasRect.left,
      y: e.clientY - canvasRect.top
    };

    // Get the color of the pixel that was clicked on in the hidden canvas, check colorHash
    // for that color and get the corresponding vertex.
    const hitCtx = this.state.hitCanvas.getContext("2d");
    const pixel = hitCtx.getImageData(mousePos.x, mousePos.y, 1, 1).data;
    const color = `rgb(${pixel[0]}, ${pixel[1]}, ${pixel[2]})`;
    const v = this.state.colorHash[color];

    if (v) {
      if (!this.state.startV) {
        await this.setState({ startV: v });
      } else if (!this.state.endV) {
        await this.setState({ endV: v });
      }
    }

    if (this.state.startV && this.state.endV) {
      let path = this.props.graph
        .dijkstraShortestPath(this.state.startV, this.state.endV)
        .reverse();

      path.unshift(this.state.startV);
      this.setState({ path });
    }
  };

  /**
   * Render
   */
  render() {
    return (
      <canvas
        ref="canvas"
        id="display-canvas"
        width={canvasWidth}
        height={canvasHeight}
        onClick={this.handleClick}
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
      graph: new Graph()
    };

    this.state.graph.randomize(7, 6, 110, 0.6);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
        <div
          className="random-button"
          onClick={() => {
            const newState = { graph: new Graph() };
            newState.graph.randomize(7, 6, 110, 0.6);
            this.setState(newState);
          }}
        >
          Randomize Graph
        </div>
      </div>
    );
  }
}

export default App;
