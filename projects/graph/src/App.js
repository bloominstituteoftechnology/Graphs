import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

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
    
    ctx.fillStyle = 'white';

    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

//=============================================================
    // ---------------------
    //        DRAWING
    // ---------------------
    // ctx.fillStyle = '#00F0F0';
    // ctx.font = 'italic 40pt serif';
    // ctx.fillText('Circle', 190, 325);

    // Translating changes the orgin of the drawing surface
    // ctx.translate(150, 30);

    // ctx.moveTo(108, 0.0);
    // ctx.lineTo(141, 70);
    // ctx.lineTo(218, 78.3);
    // ctx.lineTo(162, 131);
    // ctx.lineTo(175, 205);
    // ctx.lineTo(108, 170);
    // ctx.lineTo(108, 0);
    // ctx.lineTo(75, 68);
    // ctx.lineTo(1, 78);
    // ctx.lineTo(55, 131);
    // ctx.lineTo(41.2, 205);

    //-Complete Star Code-

    // ctx.lineTo(41.2, 205);
    // ctx.lineTo(55, 131);
    // ctx.lineTo(1, 78);
    // ctx.lineTo(75, 68);
    // ctx.lineTo(108, 0);
    // ctx.fill();
//=============================================================
 

    // !!! IMPLEMENT ME
    // compute connected components



    // draw edges
    for (let v of this.props.graph.vertexes) {
      for (let e of v.edges) {
        ctx.moveTo(e.pos.x, e.pos.y);
        ctx.lineTo(e.pos.destination.pos.x, e.pos.destination.pos.y);
        ctx.stroke(); //draws the path defined w/ moveTo() & lineTo()
      }
    }


    // draw verts



    // draw vert values (labels)
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

    // !!! IMPLEMENT ME
    // use the graph randomize() method
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
      </div>
    );
  }
}

export default App;
