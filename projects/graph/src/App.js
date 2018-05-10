import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
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
		let ctx = canvas.getContext("2d");

		// Clear it
		ctx.fillStyle = "lightblue";
		ctx.fillRect(0, 0, canvasWidth, canvasHeight);

		for (let vertex of this.props.graph.vertexes) {
			const px = vertex.pos.x;
			const py = vertex.pos.y;

			for (let edge of vertex.edges) {
				ctx.beginPath();
				ctx.moveTo(px, py);
				ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
				ctx.stroke();
			}
		}

		for (let vertex of this.props.graph.vertexes) {
			const px = vertex.pos.x;
			const py = vertex.pos.y;

			ctx.beginPath();
			ctx.arc(px, py, vertexRadius, 0, 2 * Math.PI);
			ctx.stroke();
			ctx.fillStyle = "black";
			ctx.fill();

			ctx.fillStyle = "white";
			ctx.font = "11px Arial";
			ctx.textAlign = "center";
			ctx.textBaseline = "middle";
			ctx.fillText(vertex.value, px, py);
		}

		// !!! IMPLEMENT ME
		// compute connected components
		// draw edges
		// draw verts
		// draw vert values (labels)

		// var luigiArray = [
		//   [0, 0, 0, 0, 0, 0, 0, 11, 11, 11, 11, 0, 0, 0, 0, 0],
		//   [0, 0, 0, 0, 0, 11, 11, 12, 12, 3, 12, 11, 0, 0, 0, 0],
		//   [0, 0, 0, 0, 11, 12, 12, 10, 30, 3, 0, 11, 0, 0, 0, 0],
		//   [0, 0, 0, 11, 10, 13, 10, 10, 1, 1, 1, 1, 1, 1, 0, 0],
		//   [0, 0, 11, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
		//   [0, 0, 11, 0, 1, 1, 1, 30, 1, 30, 1, 30, 0, 0, 0, 0],
		//   [0, 11, 32, 31, 32, 1, 30, 32, 1, 32, 1, 32, 31, 31, 0, 0],
		//   [0, 11, 30, 31, 32, 1, 1, 32, 32, 32, 32, 32, 32, 32, 31, 0],
		//   [0, 11, 1, 30, 32, 1, 32, 32, 1, 30, 30, 30, 30, 30, 31, 0],
		//   [0, 0, 1, 1, 30, 30, 32, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		//   [0, 0, 0, 1, 31, 30, 32, 32, 32, 1, 1, 1, 1, 0, 0, 0],
		//   [0, 0, 0, 0, 1, 31, 30, 32, 32, 32, 32, 21, 0, 0, 0, 0],
		//   [0, 0, 0, 0, 1, 31, 31, 30, 30, 30, 21, 0, 0, 0, 0, 0],
		//   [0, 0, 0, 0, 11, 10, 10, 31, 31, 12, 21, 0, 0, 0, 0, 0],
		//   [0, 0, 0, 11, 10, 10, 12, 30, 30, 32, 31, 0, 0, 0, 0, 0],
		//   [0, 0, 0, 11, 31, 31, 31, 20, 0, 22, 0, 21, 0, 0, 0, 0],
		//   [0, 0, 0, 31, 0, 0, 0, 31, 0, 22, 0, 21, 0, 0, 0, 0],
		//   [0, 0, 0, 31, 0, 0, 31, 20, 20, 20, 22, 21, 0, 0, 0, 0],
		//   [0, 0, 0, 31, 0, 0, 31, 20, 20, 21, 21, 0, 0, 0, 0, 0],
		//   [0, 0, 0, 0, 31, 31, 31, 31, 1, 31, 1, 0, 0, 0, 0, 0],
		//   [0, 0, 0, 0, 1, 31, 31, 31, 30, 1, 30, 1, 0, 0, 0, 0],
		//   [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
		// ];
		// //starting position
		// var xPos = 0;
		// var yPos = 0;

		// for (var i = 0; i < luigiArray.length; i++) {
		//   for (var r = 0; r < luigiArray[i].length; r++) {
		//     ctx.fillRect(xPos, yPos, 16, 16);

		//     //white
		//     if (luigiArray[i][r] === 0) {
		//       ctx.fillStyle = "white";
		//     }
		//     //black
		//     if (luigiArray[i][r] === 1) {
		//       ctx.fillStyle = "#000000";
		//     }
		//     //brown
		//     if (luigiArray[i][r] === 3) {
		//       ctx.fillStyle = "rgb(249, 218, 117)";
		//     }
		//     // hat colors
		//     // green base
		//     if (luigiArray[i][r] === 10) {
		//       ctx.fillStyle = "rgb(0, 192, 88)";
		//     }
		//     // green dark
		//     if (luigiArray[i][r] === 11) {
		//       ctx.fillStyle = "rgb(0, 80, 32)";
		//     }
		//     // green light
		//     if (luigiArray[i][r] === 12) {
		//       ctx.fillStyle = "rgb(0, 248, 120)";
		//     }

		//     // clothes colors
		//     // blue base
		//     if (luigiArray[i][r] === 20) {
		//       ctx.fillStyle = "rgb(112, 40, 248)";
		//     }
		//     // blue dark
		//     if (luigiArray[i][r] === 21) {
		//       ctx.fillStyle = "rgb(56, 0, 120)";
		//     }
		//     // blue light
		//     if (luigiArray[i][r] === 22) {
		//       ctx.fillStyle = "rgb(152, 104, 248)";
		//     }

		//     // skin colors
		//     // brown base
		//     if (luigiArray[i][r] === 30) {
		//       ctx.fillStyle = "rgb(248, 144, 40)";
		//     }
		//     // brown dark
		//     if (luigiArray[i][r] === 31) {
		//       ctx.fillStyle = "rgb(136, 88, 24)";
		//     }
		//     // brown light
		//     if (luigiArray[i][r] === 32) {
		//       ctx.fillStyle = "rgb(248, 200, 152)";
		//     }
		//     xPos += 16;
		//   }
		//   xPos = 0;
		//   yPos += 16;
		// }
	}

	/**
	 * Render
	 */
	render() {
		return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
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
    this.state.graph.randomize(5, 4, 150);

	}

	render() {
		return (
			<div className="App">
				<GraphView graph={this.state.graph} />
			</div>
		);
	}
}

export default App;
