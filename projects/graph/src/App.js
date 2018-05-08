import React, {Component} from 'react';
import {Graph} from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 300;
const canvasHeight = 400;

/**
 * GraphView
 */2
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
        ctx.fillStyle = 'lightblue';
        ctx.fillRect(0, 0, canvasWidth, canvasHeight);

        // ctx.beginPath();
        // ctx.arc(80,120,10,0,2*Math.PI);
        // ctx.stroke();

        ctx.beginPath();
        // ctx.arc(80,75,10,0,2*Math.PI);
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(150, 75, 10, 0, 2*Math.PI);
        ctx.arc(80,  75, 10, 0, 2*Math.PI);
        ctx.arc(80, 120, 10, 0, 2*Math.PI);
        ctx.stroke();


        // Create gradient
        const grd=ctx.createLinearGradient(10,0,200,0);
        grd.addColorStop(0,"red");
        grd.addColorStop(1,"white");

        // Fill with gradient
        ctx.fillStyle=grd;
        ctx.fillRect(10,200,150,80);

        ctx.font = "15px Arial";
        ctx.fillText("a",75,80);

        ctx.font = "15px";
        ctx.fillText("b",150,80);
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
        // use the graph randomize() method
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
