import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const xCount = 9;
const yCount = 9;
const boxSize = 100;
const prob = 0.6;

const canvasWidth = xCount * boxSize;
const canvasHeight = yCount * boxSize;
const radius = boxSize / 8;

const colors = [];

const genColorWidth = 192;
const genColorOffset = 32;

// Make as many colors as we might need
for (let i = 0; i < xCount * yCount; i++) {
  let r = (Math.random() * genColorWidth + genColorOffset)|0;
  let g = (Math.random() * genColorWidth + genColorOffset)|0; // |0 (bitwise-OR with 0) converts to integer
  let b = (Math.random() * genColorWidth + genColorOffset)|0;
  colors.push(`rgb(${r},${g},${b})`);
}

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.resetBFS();
    this.start();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.resetBFS();
    this.start();
  }

  /**
   * Reset the BFS to start over on the next pass
   */
  resetBFS() {
    /*
    const index = (Math.random() * this.props.graph.vertexes.length)|0;
    this.startNode = this.props.graph.vertexes[index];
    */
   this.resetGraph = true;
   this.startNodeIndex = 0;
   this.ccColorIndex = 0;
  }

  /**
   * Start the interval timer
   */
  start() {
    // If we're not animating, start the animation
    if (!this.intervalHandle) {
      let firstPass = true;

      // This gets called every animation frame (interval)
      let onAnimEvent = (() => {

        let startNode = this.props.graph.vertexes[this.startNodeIndex];

        let component = this.props.graph.bfsStep(firstPass? startNode: null, this.resetGraph);

        this.resetGraph = false; // Don't do this again

        if (component !== null) {

          console.log(component);
          // bfsStep() returns true if we're done with the BFS

          this.stop();

          // At this point, we have the connected component in component. Loop
          // through and set the colors for each node.
          for (let i = 0; i < component.length; i++) {
            let v = component[i];
            v.drawColor = colors[this.ccColorIndex];
          }
          this.ccColorIndex++;

          this.updateCanvas();

        } else {
          // If we're not done, we want to set startNode to null for subsequent
          // calls to bfsStep() (so that it doesn't restart the BFS every time)
          firstPass = false;
        }

        // And now draw everything
        this.updateCanvas();
      });//.bind(this);

      // Fire off a draw command every so many ms
      this.intervalHandle = setInterval(onAnimEvent, 40);
    }
  }

  /**
   * Stop the interval timer
   */
  stop() {
    clearInterval(this.intervalHandle);
    this.intervalHandle = null;

    let foundWhite = false;
    let g = this.props.graph;

    // Search through the verts for anything else that is white. If found, BFS
    // on it. This is the part that effectively colors connected components
    // differently.
    for (let i = this.startNodeIndex + 1; i < g.vertexes.length && !foundWhite; i++) {
      if (g.vertexes[i].color === 'white') {
        this.startNodeIndex = i;
        this.start();

        foundWhite = true; // stop iterating in the loop
      }
    }

    if (!foundWhite) {
      // We're all done. Reset the color
      this.ccColorIndex = 0;
      this.resetGraph = true;
    }
  }

  /**
   * Clear the canvas
   */
  clearCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
  }

  /**
   * Render the canvas
   */
  updateCanvas(timeStamp) {

    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    this.clearCanvas();

    // Edge context
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#00f';

    // Draw edges
    for (let v of this.props.graph.vertexes) {
      for (let e of v.edges) {
        let v2 = e.destination;
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v2.pos.x, v2.pos.y);
        ctx.stroke();
      }
    }

    //ctx.fillStyle = '#bbf';

    // Draw verts
    for (let v of this.props.graph.vertexes) {
      // Color the verts based on their current BFS color (white, gray, black)
      //ctx.fillStyle = v.color;
      let fillColor;

      if (v.drawColor === undefined) {
        fillColor = v.color;
      } else {
        fillColor = v.drawColor;
      }

      ctx.fillStyle = fillColor;
      ctx.strokeStyle = '#00f';
      ctx.lineWidth = 1;

      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
      ctx.stroke();
      ctx.fill();
    }

    // Draw vert values
    ctx.font = "9px sans-serif";
    ctx.textAlign = 'center';
    //ctx.fillStyle = 'black';

    for (let v of this.props.graph.vertexes) {
      // Set the color of the text based on the color of the vert
      ctx.fillStyle = v.color === 'white'? 'black': 'white';
      ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
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
      graph: new Graph()
    };

    // use the graph randomize() method
    this.state.graph.randomize(xCount, yCount, boxSize, prob);

    this.onRandomButton = this.onRandomButton.bind(this);
  }

  /**
   * When the Random button is hit
   */
  onRandomButton() {
    this.refs.graphView.stop();
  
    const state = {
      graph: new Graph()
    };

    state.graph.randomize(xCount, yCount, boxSize, prob);

    this.setState(state);
  }

  /**
   * Render
   */
  render() {
    return (
      <div className="App">
        <GraphView ref="graphView" graph={this.state.graph}></GraphView>
        <div>
          <button onClick={this.onRandomButton}>Random</button>
        </div>
      </div>
    );
  }
}

export default App;
