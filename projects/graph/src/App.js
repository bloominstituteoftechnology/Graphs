import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
 const canvasWidth = 750;
 const canvasHeight =  600;
 const randomColor = () => {
  return '#'+Math.floor(Math.random()*16777215).toString(16);
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
    
    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    let array = this.props.graph.connected;
    for ( let i = 0; i < array.length; i++) {
      let innerArray = array[i];
      let color = randomColor();
      for (let j = 0; j < innerArray.length; j++) {
        let here = innerArray[j];
        let pointX = here.pos.x;
        let pointY = here.pos.y;
        ctx.beginPath();
        ctx.arc(pointX, pointY, 5, 0, 10 * Math.PI, false);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.lineWidth = 1;
        ctx.strokeStyle = 'black';
        ctx.stroke();
        ctx.save();
      

         let edgy = innerArray[j].edges;
         console.log(edgy);
            for (let q = 0; q < edgy.length; q++){
          ctx.beginPath();
          ctx.moveTo(pointX, pointY);
          ctx.lineTo(edgy[q].weight.pos.x, edgy[q].weight.pos.y);
          ctx.lineWidth = 3;
          ctx.lineJoin = 'round';
          ctx.stroke();
          ctx.save();
          }
      }
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
 const g = this.state.graph;
 g.randomize(5, 4, 150, 0.6);
 const connected_comps = g.getConnectedComponents();
 g.connected = connected_comps;
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
