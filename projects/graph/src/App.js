import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 900;
const circleRadius = 16;

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

     console.log('this.props.graph: ', this.props.graph);
     // call our dummy function
     this.props.createDummyGraph();
     console.log('called createDummyGraph');

     // Clear it 
      ctx.fillStyle = 'grey';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);

      ctx.font = '14px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      // draw our dummy vertex
      this.props.graph.vertextes.forEach((v) => {
        ctx.beginPath();
        ctx.fillStyle = 'white';
        ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
        
        // fill in the text
        ctx.fillStyle = 'black';
        ctx.fillText(v.value, v.pos.x, v.pos.y);
      });


      // ctx.beginPath();
      // ctx.arc(10, 10, 10, 0, Math.PI * 2);
      // ctx.stroke();
      // console.log('called ctx.arc');

  //   roundedRect(ctx, 150, 80, 800, 500, 9);
  //   roundedRect(ctx, 220, 180, 120, 70, 10);
  //   roundedRect(ctx, 220, 420, 180, 50, 6);
  //   roundedRect(ctx, 750, 180, 140, 33, 10);
  //   roundedRect(ctx, 750, 400, 70, 120, 10);

  //   ctx.fillStyle = 'yellow';
  //   ctx.beginPath();
  //   ctx.arc(200, 120, 20, Math.PI / 7, -Math.PI / 7, false);
  //   ctx.lineTo(200, 120);
  //   ctx.fill();

  //   ctx.beginPath();
  //   ctx.arc(605, 320, 20, Math.PI / 7, -Math.PI / 7, false);
  //   ctx.lineTo(605, 320);
  //   ctx.fill();

  //   ctx.beginPath();
  //   ctx.arc(324, 520, 20, Math.PI / 7, -Math.PI / 7, false);
  //   ctx.lineTo(324, 520);
  //   ctx.fill();

  //   ctx.fillStyle = 'black';
  //   for (var i = 0; i < 18; i++) {
  //     ctx.fillRect(220 + i * 40, 118, 4, 4);
  //   }

  //   for (i = 0; i < 12; i++) {
  //     ctx.fillRect(520, 100 + i * 40, 4, 4);
  //   }

  //   for (i = 0; i < 18; i++) {
  //     ctx.fillRect(220 + i * 40, 318, 4, 4);
  //   }

  //   for (i = 0; i < 8; i++) {
  //     ctx.fillRect(220 + i * 40, 518, 4, 4);
  //   }

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
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}

// function roundedRect(ctx, x, y, width, height, radius) {
//   ctx.beginPath();
//   ctx.moveTo(x, y + radius);
//   ctx.lineTo(x, y + height - radius);
//   ctx.arcTo(x, y + height, x + radius, y + height, radius);
//   ctx.lineTo(x + width - radius, y + height);
//   ctx.arcTo(x + width, y + height, x + width, y + height - radius, radius);
//   ctx.lineTo(x + width, y + radius);
//   ctx.arcTo(x + width, y, x + width - radius, y, radius);
//   ctx.lineTo(x + radius, y);
//   ctx.arcTo(x, y, x, y + radius, radius);
//   ctx.stroke();
// }


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
