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
		console.log('refs', this.refs);
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
		var canvasGradient=ctx.createLinearGradient(0,0,750,600);
		canvasGradient.addColorStop(0,"white");
		canvasGradient.addColorStop(1,"gainsboro");
    ctx.fillStyle = canvasGradient;
		ctx.fillRect(0, 0, canvasWidth, canvasHeight);

		let { found } = this.props.graph;

		console.log('found', found);	
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
					ctx.stroke();
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
    return (
			<div>
				<canvas className="canvas" ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
			</div>
		);
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
		console.log('this', this);
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
				<div className="Button" onClick={() => this.handleClick()}>randomize</div>
      </div>
    );
  }
}

export default App;
