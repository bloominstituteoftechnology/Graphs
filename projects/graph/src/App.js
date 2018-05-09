import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 700;
 const canvasHeight = 700;
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
    ctx.fillStyle = '#653333';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    console.log("update canvas:", this.props.graph);

    this.props.graph.vertexes.map(vertex => {
      vertex.edges.map(edge => {
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        return edge;
      });
      return vertex;
    });

    for(let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius,0,2*Math.PI);
      ctx.fillStyle = "green";
      ctx.fill();
      ctx.strokeStyle = 'black';
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.font = '10px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y); 
    }
  

    // // !!! IMPLEMENT ME
    // let color = ['green','white','yellow','blue'];
    // for(let i=0; i<2; i++) {
    //   setInterval(function() {
    //     for(let j=0; j < 10; j++){
    //         ctx.strokeStyle = color[j%4];
    //         ctx.arc(500,500,50,10,1);
    //         ctx.stroke();
    //     }
    //     ctx.rotate(2);
    //   }, 1000);
    // }
      

   

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
    this.state.graph.debugCreateTestData();
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
