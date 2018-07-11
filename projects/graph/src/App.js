import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 600;
const circleSize = 15;

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

		let start;
		let end;

		canvas.addEventListener(
			'click',
			e => {
				const x = e.pageX - canvas.offsetLeft;
				const y = e.pageY - canvas.offsetTop;
				let vertClick;

				for (let vertex of this.props.graph.vertexes) {
					if (
						Math.abs(vertex.pos.x - x) <= circleSize &&
						Math.abs(vertex.pos.y - y) <= circleSize
					) {
						vertClick = vertex;
						if (!start) {
							start = vertClick;

							ctx.textAlign = 'center';
							ctx.textBaseline = 'middle';
							ctx.font = '16px Arial';
							ctx.fillStyle = 'black';

							ctx.fillText('START', vertex.pos.x, vertex.pos.y + 20);
						} else if (!end) {
							end = vertClick;
							ctx.textAlign = 'center';
							ctx.textBaseline = 'middle';
							ctx.font = '16px Arial';
							ctx.fillStyle = 'black';

							ctx.fillText('END', vertex.pos.x, vertex.pos.y + 20);
							console.log(`Start at: ${start.value} and End at: ${end.value}`);
						}
					}
				}
			},
			false,
		);

		// Clear it
		ctx.fillStyle = 'rgb(220, 245, 150)';
		ctx.fillRect(0, 0, canvasWidth, canvasHeight);

		console.log('in updateCanvas', this.props.graph.vertexes);

		ctx.textAlign = 'center';
		ctx.textBaseline = 'middle';
		ctx.font = '16px Arial';

		for (let vertex of this.props.graph.vertexes) {
			for (let edge of vertex.edges) {
				ctx.beginPath();
				ctx.moveTo(vertex.pos.x, vertex.pos.y);
				ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
				ctx.strokeStyle = vertex.fillColor;
				ctx.stroke();

				// Add edge weight.
				const xCenter = (vertex.pos.x + edge.destination.pos.x) / 2;
				const yCenter = (vertex.pos.y + edge.destination.pos.y) / 2;
				ctx.font = '20px Arial';
				ctx.fillStyle = 'black';
				if (edge.drawWeight === false) {
					ctx.fillText(edge.weight, xCenter + 8, yCenter + 8);
				} else {
					continue;
				}
			}
		}

		for (let vertex of this.props.graph.vertexes) {
			ctx.strokeStyle = vertex.fillColor;
			ctx.beginPath();
			ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
			ctx.fillStyle = vertex.fillColor;
			ctx.fill();
			ctx.fillStyle = 'black';
			ctx.font = '16px Arial';
			ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
			ctx.stroke();
		}
	}

	// // Clear it
	// ctx.fillStyle = 'white';
	// ctx.fillRect(0, 0, canvasWidth, canvasHeight);

	// ctx.fillStyle = 'orange';
	// ctx.fillRect(200, 200, canvasWidth, canvasHeight);
	// ctx.fillStyle = 'gray';
	// ctx.fillRect(50, 50, 50, 50);
	// ctx.fillStyle = 'black';
	// ctx.fillRect(250, 250, 25, 25);

	// ctx.moveTo(50, 20);
	// ctx.lineTo(500, 900);
	// ctx.stroke();
	// ctx.strokeStyle = 'black';

	// ctx.lineTo(50, 200);
	// ctx.lineTo(500, 20);
	// ctx.lineTo(75, 100);
	// ctx.stroke();

	// ctx.beginPath();
	// ctx.moveTo(135, 50);
	// ctx.arc(95, 50, 40, 0, 2 * Math.PI);
	// ctx.moveTo(200, 250);
	// ctx.arc(200, 250, 40, 0, 1 * Math.PI);
	// ctx.moveTo(300, 50);
	// ctx.arc(300, 50, 40, 0, 2 * Math.PI);
	// ctx.stroke();

	// ctx.strokeStyle = 'green';
	// for (let i = 0; i < 150; i++) {
	// 	ctx.beginPath();
	// 	ctx.moveTo(0, 0);
	// 	ctx.lineTo(i * 10, 600);
	// 	ctx.stroke();
	// }

	// ctx.strokeStyle = 'blue';
	// for (let i = 0; i < 150; i++) {
	// 	ctx.beginPath();
	// 	ctx.moveTo(Math.cos(i) * 300, Math.sin(i) * 100);
	// 	ctx.lineTo(Math.sin(i) * 600, Math.cos(i) * 600);
	// 	ctx.stroke();
	// }

	// set up the gradient
	// let grd = ctx.createLinearGradient(500, 50, 50, 90, 60, 100);
	// grd.addColorStop(0, 'orange');
	// grd.addColorStop(1, 'black');

	// // Fill with gradient
	// ctx.fillStyle = grd;
	// ctx.fillRect(0, 0, canvasWidth, canvasHeight);

	// ctx.beginPath();
	// ctx.arc(400, 300, 140, 0, 2 * Math.PI);
	// ctx.stroke();
	// ctx.strokeStyle = 'white';
	// ctx.fillStyle = 'black';
	// ctx.fill();

	// ctx.strokeStyle = '#C8102E';
	// for (let i = 0; i < 50; i++) {
	// 	ctx.beginPath();
	// 	ctx.moveTo(0, 0);
	// 	ctx.lineTo(i * 10, 600);
	// 	ctx.stroke();
	// }

	// ctx.strokeStyle = '#C8102E';
	// for (let i = 0; i < 150; i++) {
	// 	ctx.beginPath();
	// 	ctx.moveTo(Math.cos(i) * 100, Math.sin(i) * 100);
	// 	ctx.lineTo(Math.sin(i) * 600, Math.cos(i) * 600);
	// 	ctx.stroke();
	// }

	// ctx.font = '50px Arial';
	// ctx.fillStyle = 'black';
	// ctx.fillText('LETS GO FLYERS!!!', 150, 60);

	// create circles in a loop
	// ctx.strokeStyle = '#B9975B';
	// for (let i = 0; i < canvas.width; i += 15) {
	// 	for (let j = 0; j < canvas.height; j += 15) {
	// 		// ctx.fillRect(x, y, 20, 20);
	// 		ctx.beginPath();
	// 		ctx.arc(i, j, 40, 0, 2 * Math.PI);
	// 		ctx.stroke();
	// 		ctx.strokeStyle = '#B9975B';
	// 	}
	// }

	// ctx.moveTo(100, 100);
	// ctx.lineTo(300, 100);
	// ctx.strokeStyle = '#C8102E';
	// ctx.stroke();

	// ctx.moveTo(100, 100);
	// ctx.lineTo(100, 300);
	// ctx.strokeStyle = '#C8102E';
	// ctx.stroke();

	// ctx.moveTo(300, 100);
	// ctx.lineTo(300, 300);
	// ctx.strokeStyle = '#C8102E';
	// ctx.stroke();

	// ctx.moveTo(100, 300);
	// ctx.lineTo(200, 400);
	// ctx.strokeStyle = '#C8102E';
	// ctx.stroke();

	// ctx.moveTo(300, 300);
	// ctx.lineTo(200, 400);
	// ctx.strokeStyle = '#C8102E';
	// ctx.stroke();

	// ctx.beginPath();
	// ctx.arc(150, 150, 0, 10, 10);
	// ctx.strokeStyle = '#C8102E';
	// ctx.stroke();

	// !!! IMPLEMENT ME
	// compute connected components
	// draw edges
	// draw verts
	// draw vert values (labels)
	// }

	/**
	 * Render
	 */
	render() {
		return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
	}
}

class App extends Component {
	constructor(props) {
		super(props);

		this.state = {
			graph: new Graph(),
		};
		// this.state.graph.debugCreateTestData();
		this.state.graph.randomize(5, 4, 150, 0.6);
		this.state.graph.getConnectedComponents();
	}

	handleClick() {
		const newGraph = { graph: new Graph() };
		newGraph.graph.randomize(5, 4, 150, 0.6);
		newGraph.graph.getConnectedComponents();
		this.setState(newGraph);
	}
	render() {
		return (
			<div className="App">
				<GraphView graph={this.state.graph} />
				<div className="btnDiv">
					<div className="Button" onClick={() => this.handleClick()}>
						New Graph
					</div>
				</div>
			</div>
		);
	}
}

export default App;
