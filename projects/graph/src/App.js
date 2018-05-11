import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 750;
 const canvasHeight = 600;
 const vertexRadius = 10;

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
    ctx.fillStyle = 'green';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    /** Get random color
  */
  function getRandomColor() {
    let color = "#";
    let letters = 'ABCDEF0123456789';
    for(let i = 0 ; i < 6; i++){
      color += letters[Math.floor(Math.random() * 16)];
    }
    console.log("color");
    console.log(color);
    return color;
  }
  //   this.props.graph.vertexes.map(vertex => {
  //     vertex.edges.map(edge => {
  //       ctx.moveTo(vertex.pos.x, vertex.pos.y);
  //       ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
  //       ctx.stroke();
  //       return edge;
  //     });
  //     return vertex;
    

  //   // for(let vertex of this.props.graph.vertexes) {
  //   //   ctx.beginPath();
  //     ctx.moveTo(vertex.pos.x, vertex.pos.y);
  //     ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius,0,2*Math.PI);
  //     ctx.fillStyle = getRandomColor();
  //     ctx.fill();
  //     ctx.strokeStyle = getRandomColor();
  //     ctx.stroke();

  //     ctx.fillStyle = this.getRandomColor();
  //     ctx.font = '10px Arial';
  //     ctx.textAlign = 'center';
  //     ctx.textBaseline = 'middle';
  //     ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y); 
  //   //}
  // });
    /**
   
 */ 
      
const connectedGroups = this.props.graph.getConnectedComponents();
this.props.graph.dump();
    connectedGroups.forEach(group => {
      const groupColor = getRandomColor();
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
      })

    })


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
    //this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5,4,150);
    this.state.graph.getConnectedComponents();
  }

 getNew = () => {
    const graph = new Graph();
    graph.randomize(4,3,150);
    this.setState({graph});
  };

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.getNew}>Refresh</button>
      </div>
    );
  }
}

export default App;
