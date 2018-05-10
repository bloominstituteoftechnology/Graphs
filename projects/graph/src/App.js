import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = 750;
const canvasHeight = 600;
const vertexRadius = 20;

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
		canvasGradient.addColorStop(0,"white");
		canvasGradient.addColorStop(1,"gainsboro");
    ctx.fillStyle = canvasGradient;
		ctx.fillRect(0, 0, canvasWidth, canvasHeight);

		let { found } = this.props.graph;

		for (let component of found) {
			for (let vertex of component) {
				let { edges } = vertex;
				for (let edge of edges) {
					let { x, y } = vertex.pos;
					let { x: destination_x, y: destination_y } = edge.destination.pos;
					ctx.beginPath();
					ctx.moveTo(x, y);
					ctx.lineTo(destination_x, destination_y);
					ctx.strokeStyle=component.color;
					ctx.lineWidth = edge.weight;
					ctx.stroke();

					ctx.beginPath();
					let weight_x = (x + destination_x)/2;
					let weight_y = (y + destination_y)/2;
					let { weight } = edge;
					let radius = vertexRadius/2;
					ctx.lineWidth=1;
					ctx.moveTo(weight_x + radius, weight_y);
					ctx.arc(weight_x, weight_y, radius, 0, 2 * Math.PI);
					ctx.fillStyle="gainsboro"
					ctx.fill();
					ctx.strokeStyle=component.color;
					ctx.stroke();
					ctx.strokeStyle="black";
					ctx.textAlign = "center";
					ctx.textBaseline = "middle";
					ctx.font=".8rem Arial"
					ctx.strokeText(weight, weight_x, weight_y);
				}
			}
			for (let vertex of component) {
				
				let { x, y } = vertex.pos;
				let { value } = vertex, radius = vertexRadius;
				ctx.beginPath();
				ctx.arc(x, y, radius, 0, 2 * Math.PI);
				ctx.fillStyle=component.color;
				ctx.fill();
				ctx.strokeStyle=component.color;
				ctx.stroke();
				
				ctx.strokeStyle="white";
				ctx.textAlign = "center";
				ctx.textBaseline = "middle";
				ctx.font="1rem Arial";
				ctx.strokeText(value, x, y);
			}	
		}
  }
  
  render() {
    return <canvas className="canvas" ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
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

	handleClick() {
		const refreshedState = {
			graph: new Graph()
		};
		refreshedState.graph.randomize(5, 4, 150);
		refreshedState.graph.getConnectedComponents();
		this.setState(refreshedState);
	}

  

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
				<div className="Button" onClick={() => this.handleClick()}>randomize</div>
      </div>
    );
  }
}

export default App;
