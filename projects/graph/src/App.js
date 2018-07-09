import React, {Component} from 'react';
import {Graph} from './graph';
import './App.css';

// !!! IMPLEMENT ME
const xValue = 6;
const yValue = 6;
const boxSize = 150;
const probability = 0.6;


const canvasWidth = xValue * boxSize;
const canvasHeight = yValue * boxSize;
const radius = boxSize / 9;


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
        const graph = this.props.graph;

        this.drawVertex(graph.vertexes);
    }

    drawVertex(vertexes, color, clear=true) {
        let canvas = this.refs.canvas;
        let ctx = canvas.getContext('2d');

        // Clear it
        if (clear) {
            ctx.fillStyle = 'white';
            ctx.fillRect(0, 0, canvasWidth, canvasHeight);
        }

        this.drawLines(vertexes, ctx);


        // for (let v of vertexes) {
        //     ctx.fillStyle = this.randomColor();
        //     ctx.beginPath();
        //     ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
        //     ctx.stroke();
        //     ctx.fill();
        // }

        this.drawGraph(vertexes, ctx);


        this.drawVertexName(vertexes, ctx);
    }

    drawLines(vertexes, ctx) {
        ctx.lineWidth = 2;
        ctx.strokeStyle = this.randomColor();

        for (let v of vertexes) {
            for (let e of v.edges) {
                const v2 = e.destination;
                ctx.beginPath();
                ctx.moveTo(v.pos.x, v.pos.y);
                ctx.lineTo(v2.pos.x, v2.pos.y);
                ctx.stroke();
            }
        }
    }

    drawGraph(vertexes, ctx) {
        for (let v of vertexes) {
            ctx.fillStyle = this.randomColor();
            ctx.beginPath();
            ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI, false);
            ctx.stroke();
            ctx.fill();
        }
    }


    drawVertexName(vertexes, ctx) {

        ctx.font = '12px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillStyle = 'white';

        for (let v of vertexes) {
            ctx.fillText(v.value, v.pos.x, v.pos.y + 4);
        }
    }
    randomColor() {

        const number = Math.floor(Math.random() * 10) + 1;

        switch (number) {
            case 1:
                return 'blue';

            case 2:
                return 'red';
            case 3:
                return 'green';
            case 4:
                return 'brown';

            case 5:
                return 'black';

            case 6:
                return 'navy';

            case 7:
                return 'cyan';

            case 8:
                return 'LightBlue';
            case 9:
                return 'SpringGreen';
            case 10:
                return 'Magenta';

            default:
                return 'blue';

        }

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

        // !!! IMPLEMENT ME
        this.state.graph.randomize(xValue, yValue, boxSize, probability);
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
