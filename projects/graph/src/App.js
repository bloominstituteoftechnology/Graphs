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
		
		console.log({'this.props.graph': this.props.graph})	

		this.props.graph.vertexes.map((vertex) => {

			vertex.edges.map((edge) => {

				ctx.beginPath();
				ctx.moveTo(vertex.pos.x, vertex.pos.y);
				ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
				ctx.strokeStyle="black";
				ctx.stroke();

				return edge;
			});
			return vertex;
		});
		
		this.props.graph.vertexes.map((vertex) => {

			ctx.beginPath();
			ctx.arc(vertex.pos.x, vertex.pos.y, vertexRadius, 0, 2 * Math.PI);
			ctx.fillStyle="gainsboro";
			ctx.fill();
			ctx.stroke();
			
			ctx.strokeStyle="black";
			ctx.textAlign = "center";
			ctx.textBaseline = "middle";
			ctx.strokeText(vertex.value, vertex.pos.x, vertex.pos.y);

			return vertex;
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

		this.state.graph.randomize(5, 4, 150, 0.6);
		// this.state.graph.debugCreateDummyData();
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
