import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 600;
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
		var canvasGradient=ctx.createLinearGradient(0,0,200,200);
		canvasGradient.addColorStop(0,"yellow");
		canvasGradient.addColorStop(1,"skyblue");
    ctx.fillStyle = canvasGradient;
		ctx.fillRect(0, 0, canvasWidth, canvasHeight);
		
		console.log({'this.props.graph': this.props.graph})	
		// for (let vertex of this.props.graph.vertexes) {
		this.props.graph.vertexes.map((vertex) => {

			vertex.edges.map((edge) => {
				ctx.beginPath();
				ctx.moveTo(vertex.pos.x, vertex.pos.y);
				ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
				ctx.strokeStyle="black";
				ctx.stroke();
			})
			ctx.beginPath();
			ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2*Math.PI);
			ctx.fillStyle="gainsboro";
			ctx.fill();
			ctx.stroke();
			
			ctx.strokeStyle="black";
			ctx.textAlign = "center";
			ctx.textBaseline = "middle";
			ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);

			// if (vertex.pos !== undefined) {
			
			// }
		});
		// }
    // compctx.arcute connected components
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

		this.state.graph.debugCreateDummyData();
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
