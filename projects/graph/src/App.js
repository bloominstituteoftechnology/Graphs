import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

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

  getRandomColor() {
    let color = '#';
    let letters = 'ABCDEF0123456789';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // // Clear it
    // ctx.fillStyle = '#42d1f4';
    // ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    // // drawing edges and vertices
    // this.props.graph.vertexes.map(vertex => {
    //   // vertex.color = this.state.graph.getRandomColor();
    //   vertex.edges.map(edge => {
    //     //draw line from center of vertex to center of other vertex
    //     ctx.moveTo(vertex.pos.x, vertex.pos.y);
    //     ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
    //     // ctx.strokeStyle = this.getRandomColor();
    //     ctx.stroke();
    //     // edge.color = this.state.graph.getRandomColor();
    //     return edge;
    //   });

    //   ctx.moveTo(vertex.pos.x, vertex.pos.y);
    //   ctx.arc(vertex.pos.x, vertex.pos.y, 15, 0, Math.PI * 2);
    //   ctx.fillStyle = 'black';
    //   ctx.font = '13px Calibri';
    //   ctx.textAlign = 'center';
    //   ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    //   // ctx.strokeStyle = this.getRandomColor();
    //   ctx.stroke();
    //   return vertex;
    // });

    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const connectedGroups = this.props.graph.getConnectedComponents();

    // !!! IMPLEMENT ME
    this.props.graph.dump();
    connectedGroups.forEach(group => {
      const groupColor = this.getRandomColor();
      group.forEach(vert => {
        vert.edges.forEach(edge => {
          ctx.beginPath();
          ctx.moveTo(vert.pos.x, vert.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y)
          ctx.strokeStyle = groupColor;
          ctx.stroke();
        })
      })
      
      group.forEach(vert => {
        ctx.beginPath();
        ctx.arc(vert.pos.x, vert.pos.y, 10, 0, 2 * Math.PI);
        ctx.fillStyle = groupColor;
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.stroke();
  
        ctx.fillStyle = 'black';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vert.value, vert.pos.x, vert.pos.y);
      });

    });

    
  }

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
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(4, 5, 150);
    this.state.graph.getConnectedComponents();
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
