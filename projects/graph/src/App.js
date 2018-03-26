import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = window.innerWidth;
const canvasHeight = window.innerHeight;

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
            ctx.strokeStyle = 'blue';
            vertex.edges.forEach(edge => {
                ctx.moveTo(vertex.pos.x, vertex.pos.y);
                ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
            });
            ctx.stroke();
        });
        // draw verts
        this.props.graph.vertexes.forEach(vertex => {});
        // draw vert values (labels)
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
        this.state.graph.randomize(5, 5, 100, 0.6);
        let start = this.state.graph.vertexes[0];
        this.state.graph.bfs(start);
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
