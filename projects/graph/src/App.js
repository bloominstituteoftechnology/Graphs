import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

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

  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
		var canvasGradient=ctx.createLinearGradient(0,0,750,600);
		canvasGradient.addColorStop(0,"lightcyan");
		canvasGradient.addColorStop(1,"skyblue");
    ctx.fillStyle = canvasGradient;
		ctx.fillRect(0, 0, canvasWidth, canvasHeight);
		
		this.props.graph.vertexes.map((vertex) => {

			vertex.edges.map((edge) => {

				let { x, y } = vertex.pos;
				let { x: destination_x, y: destination_y } = edge.destination.pos;
				ctx.beginPath();
				ctx.moveTo(x, y);
				ctx.lineTo(destination_x, destination_y);
				ctx.strokeStyle="black";
				ctx.stroke();

				return 0;
			});
			return 0;
		});
		
		this.props.graph.vertexes.map((vertex) => {

			let { x, y } = vertex.pos;
			let { value } = vertex, radius = vertexRadius;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2 * Math.PI);
			ctx.fillStyle="gainsboro";
			ctx.fill();
			ctx.stroke();
			
			ctx.strokeStyle="black";
			ctx.textAlign = "center";
			ctx.textBaseline = "middle";
			ctx.strokeText(value, x, y);

			return 0;
		});
  }
  
  render() {
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
  }
}


class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph()
    };

		let { graph } = this.state;
		graph.randomize(5, 4, 150);
		// this.state.graph.debugCreateDummyData();
		graph.getConnectedComponents();
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
