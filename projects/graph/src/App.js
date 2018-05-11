import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 500;
const canvasHeight = 500;

const getRandomColor = () => {
  let letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
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
    //let radius = 50;

    const color = getRandomColor();

    const grd = ctx.createLinearGradient(0, 0, 500, 0)
    grd.addColorStop(0, color);
    grd.addColorStop(1, 'black');


    // Clear it
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, 10, 0, 2 * Math.PI);
      ctx.fillStyle = color;
      ctx.fill();
      ctx.strokeStyle = 'black';
      ctx.stroke();


      ctx.fillStyle = 'black';
      ctx.font = "10px Arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
    }

    const vertexes = this.props.graph.vertexes;

    for (let component of this.props.connectedComponents) {
      ctx.strokeStyle = "black";
      ctx.lineWidth = 0.75;
      //Each vertex gets looped through
      for (let i = 0; i < component.length; i++) {
        const vertex = vertexes[component[i]];
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.stroke();
        }
      }

    }
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    // ctx.fillStyle = '#3BB9FF';
    // ctx.fillRect(0, 0, 500, 200);



    // ctx.fillStyle = 'yellow';
    // ctx.arc(800 / 2, 150 / 2, radius, 0, 2 * Math.PI, false); 
    // ctx.fill();


    // ctx.fillStyle = 'ivory';
    // ctx.fillRect(80, 150, 200, 200);

    // ctx.fillStyle = 'brown';
    // ctx.fillRect(100, 170, 50, 50);

    // ctx.fillStyle = 'brown';
    // ctx.fillRect(210, 170, 50, 50);

    // ctx.fillStyle = 'gray';
    // ctx.fillRect(153, 250, 50, 100);


    // let sWidth = 500;
    // let sHeight = 500;
    // let path=new Path2D();
    // path.moveTo((sWidth/2)+50,sHeight/2);
    // path.lineTo((sWidth/2),(sHeight/2)-50);
    // path.lineTo((sWidth/2)-50,sHeight/2);
    // ctx.fill(path);
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
      graph: new Graph(),
      connectedComponents: []
    };

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(4, 5, 120, 0.7);
    this.state.connectedComponents = this.state.graph.getConnectedComponents();
    this.generateNewGraph = this.generateNewGraph.bind(this);
  }

  generateNewGraph() {
      const state = {
        graph: new Graph()
      };
  
      state.graph.randomize(4, 5, 120, 0.7);
  
      this.setState(state);

  }

render() {
  return (
    <div className="App">
      <GraphView
        graph={this.state.graph}
        connectedComponents={this.state.connectedComponents} />{" "}
      <p>Click for a new graph</p>
      <button onClick={this.generateNewGraph}>
        Generate
      </button>
    </div>
  );
}
}

export default App;
