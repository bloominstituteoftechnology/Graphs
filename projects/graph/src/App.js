import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const numX = 5;
const numY = 5;
const pxBox = 150;
const probability = 0.6;
const canvasWidth = numX * pxBox;
const canvasHeight = numY * pxBox;
const radius = 10;

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

        // compute connected components
        const connectedComponents = this.props.graph.getConnectedComponents();
        // draw edges
        this.props.graph.vertexes.forEach(vertex => {
            ctx.beginPath();
            ctx.strokeStyle = 'green';
            vertex.edges.forEach(edge => {
                ctx.lineWidth = 2;
                ctx.moveTo(vertex.pos.x, vertex.pos.y);
                ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
                ctx.stroke();
            });
        });
        // draw verts
        this.props.graph.vertexes.forEach(vertex => {
            ctx.beginPath();
            ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, Math.PI * 2, true);
            ctx.strokeStyle = 'green';
            ctx.lineWidth = 4;
            ctx.stroke();
            ctx.fillStyle = 'white';
            ctx.fill();
            ctx.beginPath();
            ctx.font = '10px sans-serif';
            ctx.fillStyle = 'black';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
        });
        // draw edge weights (labels)
        this.props.graph.vertexes.forEach(vertex => {
            ctx.beginPath();
            ctx.fillStyle = 'black';
            ctx.font = '15px sans-serif';
            vertex.edges.forEach(edge => {
                let x = (edge.destination.pos.x + vertex.pos.x) / 2;
                let y = (edge.destination.pos.y + vertex.pos.y) / 2;
                ctx.fillText(edge.weight, x, y);
            });
        });
    }

    /**
     * Render
     */
    render() {
        return (
            <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />
        );
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

        // use the graph randomize() method
        this.state.graph.randomize(numX, numY, pxBox, probability);
    }

    handleClick = () => {
        const graph = new Graph();
        graph.randomize(numX, numY, pxBox, probability);
        this.setState({ graph });
    };

    render() {
        return (
            <div className="App">
                <GraphView graph={this.state.graph} />
                <button onClick={this.handleClick}>Generate Graph</button>
            </div>
        );
    }
}

export default App;
