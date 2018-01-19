import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const xCount = 9;
const yCount = 9;
const boxSize = 100;
const prob = 0.6;

const canvasWidth = xCount * boxSize;
const canvasHeight = yCount * boxSize;
const radius = boxSize / 12;

const STOP_AFTER_BFS = false; // false to keep restarting on new graphs

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
    const index = (Math.random() * this.props.graph.vertexes.length)|0;
    this.startNode = this.props.graph.vertexes[index];
  }

  /**
   * Start the interval timer
   */
  start() {
    // If we're not animating, start the animation
    if (!this.intervalHandle) {

      // This gets called every animation frame (interval)
      let onAnimEvent = () => {

        if (this.props.graph.bfsStep(this.startNode)) {

          // bfsStep() returns true if we're done with the BFS

          if (STOP_AFTER_BFS) {
            this.stop();

          } else {
            // Notify parent component that we're done
            this.props.onDone();

            // Reset the starting node
            this.resetBFS();
          }
        } else {
          // If we're not done, we want to set startNode to null for subsequent
          // calls to bfsStep() (so that it doesn't restart the BFS every time)
          this.startNode = null;
        }

        // And now draw everything
        this.updateCanvas();
      };

      // Fire off a draw command every so many ms
      this.intervalHandle = setInterval(onAnimEvent, 20);
    }
  }

  /**
   * Stop the interval timer
   */
  stop() {
    clearInterval(this.intervalHandle);
    this.intervalHandle = null;

    // Reset the starting node for the next time the interval timer fires up
    this.resetBFS();
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
      ctx.fillStyle = v.color;

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

    this.onDone = this.onDone.bind(this);
    this.onRandomButton = this.onRandomButton.bind(this);
  }

  /**
   * Callback when the GraphView has finished animating
   */
  onDone() {
    this.state.graph.randomize(xCount, yCount, boxSize, prob);
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
        <GraphView ref="graphView" graph={this.state.graph} onDone={this.onDone}></GraphView>
        <div>
          <button onClick={this.onRandomButton}>Random</button>
        </div>
      </div>
    );
  }
}

export default App;
