import React, {
  Component
} from 'react';
import {
  Graph
} from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 850
const canvasHeight = 600

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


    // Clear it

    // Create gradient
    var grd = ctx.createLinearGradient(0, 0, 200, 400);
    grd.addColorStop(0, "yellow");
    grd.addColorStop(1, "green");


    // Fill with gradient
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //Images
    ctx.font = '38pt Arial';

    ctx.fillStyle = 'cornflowerblue';
    ctx.strokeStyle = 'blue';

    ctx.fillText("Hey CS8!", canvas.width / 2 - 150,
      canvas.height / 2 + 25);

    ctx.strokeText("Hey CS8!", canvas.width / 2 - 150,
      canvas.height / 2 + 25);








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
    return <canvas ref = "canvas"
    width = {
      canvasWidth
    }
    height = {
      canvasHeight
    } > < /canvas>;
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
  }

  render() {
    return ( <
      div className = "App" >
      <
      GraphView graph = {
        this.state.graph
      } > < /GraphView> < /
      div >
    );
  }
}

export default App;