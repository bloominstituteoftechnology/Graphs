import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleRadius = 15;

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
    // const canvas = this.refs.canvas;
    // const ctx = canvas.getContext('2d');
    
    // // Vertex click event
    // let start;
    // let end;

    // canvas.addEventListener(
    //   'click',
    //   e => {
    //     const x = e.pageX - canvas.offsetLeft;
    //     const y = e.pageY - canvas.offsetTop;
    //     let vertClick;

    //     for (let vertex of this.props.graph.vertexes) {
    //       if (
    //         Math.abs(vertex.pos.x - x) <= circleRadius &&
    //         Math.abs(vertex.pos.y - y) <= circleRadius
    //       ) {
    //         vertClick = vertex;
    //         if (!start) {
    //           start = vertClick;

    //           ctx.textAlign = 'center';
    //           ctx.textBaseline = 'middle';
    //           ctx.font = '8px Arial';
    //           ctx.fillStyle = 'black';

    //           ctx.fillText('START', vertex.pos.x, vertex.pos.y + 20);
    //         } else if (!end) {
    //           end = vertClick;
    //           ctx.textAlign = 'center';
    //           ctx.textBaseline = 'middle';
    //           ctx.font = '8px Arial';
    //           ctx.fillStyle = 'black';

    //           ctx.fillText('END', vertex.pos.x, vertex.pos.y + 20);
    //           console.log(`Start at: ${start.value} and End at: ${end.value}`);
    //         }
    //       }
    //     }
    //   },
    //   false
    // );
      let canvas = this.refs.canvas;
      let ctx = canvas.getContext('2d');

      // Clear it
      ctx.fillStyle = 'rgb(0, 206, 209)';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);

      console.log('in updateCanvas', this.props.graph.vertexes);

      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.font = '16px Arial';

      for (let vertex of this.props.graph.vertexes) {
        for (let edge of vertex.edges) {
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        }
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, circleRadius, 0, 2 * Math.PI);
        ctx.fillStyle =
          'rgb(' +
          Math.floor(Math.random() * 256) +
          ',' +
          Math.floor(Math.random() * 256) +
          ',' +
          Math.floor(Math.random() * 256) +
          ')'; // TODO: make variable?
        ctx.fill();
        ctx.fillStyle = 'black';
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
        ctx.stroke();
      }

    // Clear it
    ctx.fillStyle = 'rgb(58, 49, 79)';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.font = '10px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        ctx.fillText(edge.weight, (vertex.pos.x + edge.destination.pos.x) / 2, (vertex.pos.y + edge.destination.pos.y) / 2);
      
        // Add edge weight.
        // const xCenter = (vertex.pos.x + edge.destination.pos.x) / 2;
        // const yCenter = (vertex.pos.y + edge.destination.pos.y) / 2;
        // ctx.font = '12px Arial';
        // ctx.fillStyle = 'purple';
        // if (edge.drawWeight === false) {
        //   ctx.fillText(edge.weight, xCenter + 8, yCenter + 8);
        // } else {
        //   continue;
        // }
      }
    }

    // Draw our dummy vertex
    this.props.graph.vertexes.forEach((v) => {
      ctx.beginPath();
      ctx.fillStyle = '#cd5360';
      ctx.arc(v.pos.x, v.pos.y, circleRadius, 0, 2 * Math.PI);
      // ctx.lineCap="square";
      // // ctx.moveTo(200, 20);
      // ctx.lineTo(300, 20);
      ctx.fill();
      ctx.stroke();

      // fill in the text
      ctx.fillStyle = '#ffffff';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });

    // Set up the gradient
    // let grd = ctx.createLinearGradient(400, 50, 50, 90, 60, 100);
    // grd.addColorStop(0, '#932fa3');
    // grd.addColorStop(1, '#259ec6');

    // Fill with gradient
    // ctx.fillStyle = grd;
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Create circles in a loop
    // ctx.strokeStyle = '#dce5e8';
    // for (let i = 0; i < canvas.width; i += 18) {
    //   for (let j = 0; j < canvas.height; j += 10) {
    //     ctx.beginPath();
    //     ctx.arc(i, j, 40, 0, 2 * Math.PI);
    //     ctx.stroke();
    //   }
    // }

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
    this.state.graph.randomize(5, 4, 150, 0.6);
    this.state.graph.getConnectedComponents();
  }

  handleClick() {
    const newGraph = { graph: new Graph() };
    newGraph.graph.randomize(5, 4, 150, 0.6);
    newGraph.graph.getConnectedComponents();
    this.setState(newGraph);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        {/* <div className="btnDiv">
          <div className="Button" onClick={() => this.handleClick()}>
            Random Graph
          </div>
        </div> */}
      </div>
    );
  }
}

export default App;
