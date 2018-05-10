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
     * Draw graph with vertexes and edges
     */

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
        const connectedComponentsList = this.props.graph.getConnectedComponents();
        connectedComponentsList.forEach(component => {
            let randomColor = '#000000'.replace(/0/g, () => {
                return (~~(Math.random() * 16)).toString(16);
            });

            // draw edges
            component.forEach(vertex => {
                ctx.beginPath();
                ctx.strokeStyle = randomColor;
                vertex.edges.forEach(edge => {
                    ctx.lineWidth = 2;
                    ctx.moveTo(vertex.pos.x, vertex.pos.y);
                    ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
                    ctx.stroke();
                });
            });
            // draw verts
            component.forEach(vertex => {
                ctx.beginPath();
                ctx.arc(
                    vertex.pos.x,
                    vertex.pos.y,
                    radius,
                    0,
                    Math.PI * 2,
                    true
                );
                ctx.strokeStyle = randomColor;
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
            component.forEach(vertex => {
                ctx.beginPath();
                ctx.fillStyle = 'black';
                ctx.font = '15px sans-serif';
                vertex.edges.forEach(edge => {
                    let x = (edge.destination.pos.x + vertex.pos.x) / 2;
                    let y = (edge.destination.pos.y + vertex.pos.y) / 2;
                    if (edge.weight) ctx.fillText(edge.weight, x, y);
                });
            });
        });
    }

    handleClick = e => {
        const canvas = this.refs.canvas;
        const ctx = canvas.getContext('2d');
        const rect = canvas.getBoundingClientRect();

        let x = e.clientX - rect.left;
        let y = e.clientY - rect.top;

        const vertexes = this.props.graph.vertexes;
        const selected = vertexes.find(vertex => {
            return (
                Math.abs(vertex.pos.x - x) <= radius &&
                Math.abs(vertex.pos.y - y) <= radius
            );
        });

        if (selected) {
            ctx.beginPath();
            ctx.arc(
                selected.pos.x,
                selected.pos.y,
                radius,
                0,
                Math.PI * 2,
                true
            );
            ctx.fillStyle = selected.isSelected ? 'white' : 'yellowgreen';
            ctx.fill();
            ctx.beginPath();
            ctx.font = '10px sans-serif';
            ctx.fillStyle = 'black';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(selected.value, selected.pos.x, selected.pos.y);
            selected.isSelected = !selected.isSelected;
            console.log(
                `Vertex ${selected.value} is selected: ${selected.isSelected}.`,
                `Coordinates is x: ${selected.pos.x} y: ${selected.pos.y}`
            );
        }
    };

    /**
     * Render
     */
    render() {
        return (
            <canvas
                ref="canvas"
                width={canvasWidth}
                height={canvasHeight}
                onClick={this.handleClick}
            />
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
