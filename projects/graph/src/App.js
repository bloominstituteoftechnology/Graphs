import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 650;

/**
 * GraphView
 */
class GraphView extends Component {
  state = {
    vertice: null,
    vertice2: null,
    memory: [],
  }
  shouldComponentUpdate(nextProps, nextState) {
    return nextState === this.state;
  }
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
    this.setState({vertice: null, vertice2: null});
    this.updateCanvas();
  }

  /**
   * Render the canvas
   */
  getRndColor() {
    const r = 255*Math.random()|0,
        g = 255*Math.random()|0,
        b = 255*Math.random()|0;
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }

  handleClick(e) {
    const canvas = this.refs.canvas;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    for (const v of this.props.graph.vertexes) {
        if ((x >= v.pos.x - 20 && x <= v.pos.x + 20) && (y >= v.pos.y - 20 && y <= v.pos.y + 20)){
          if (!this.state.vert1) {
            const newMem = this.state.memory;
            newMem.push(canvas.toDataURL("image/png"));
            const ctx = canvas.getContext('2d');
            ctx.beginPath();
            ctx.lineWidth = 7;
            ctx.strokeStyle = 'black';
            ctx.arc(v.pos.x, v.pos.y, 22, 0, Math.PI * 2, true);
            ctx.stroke();
            this.setState({vert1: v, memory: newMem});
            console.log(`Selected: ${v.value}`)
            break;
          }
          else if (!this.state.vert2) {
            if (v === this.state.vert1) {
              const ctx = canvas.getContext('2d');
              let prev = new Image ();
              prev.src = this.state.memory[0];
                prev.onload = function() { 
                ctx.drawImage(prev, 0, 0); 
                console.log(`Deselected: ${v.value}`)
              };
              this.setState({vert1: null, memory: []});
            }
          else {
            const newMem = this.state.memory;
            newMem.push(canvas.toDataURL("image/png"));
            const ctx = canvas.getContext('2d');
            ctx.beginPath();
            ctx.lineWidth = 7;
            ctx.strokeStyle = 'black';
            ctx.arc(v.pos.x, v.pos.y, 21, 0, Math.PI * 2, true);
            ctx.stroke();
            this.setState({vert2: v, memory: newMem});
            console.log(`Selected end: ${v.value}`)
            break;
            }
          }
          else if (v === this.state.vert2) {
            const ctx = canvas.getContext('2d');
              let prev = new Image ();
              prev.src = this.state.memory[1];
              prev.onload = function() { 
                ctx.drawImage(prev, 0, 0); 
                console.log(`Deselected start: ${v.value}`)
              };
              this.setState({vert2: null, memory: this.state.memory.slice(0, 1)});
          }
        }
      }
  }

  updateCanvas() {
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d'); 
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    const g = this.props.graph;
    g.randomize(5, 4, 150, 0.6);
    const connectedComponents = g.getConnectedComponents();
    for (const subgraph of connectedComponents) {
      const color = this.getRndColor();
      for (const v of subgraph) {
        for (let e of v.edges) {
          ctx.beginPath();
          ctx.strokeStyle = color;
          ctx.lineWidth=e.weight;
          ctx.moveTo(v.pos.x, v.pos.y);
          ctx.lineTo(e.destination.pos.x, e.destination.pos.y);
          ctx.closePath();
          ctx.stroke();

          ctx.font = '10px arial';
          ctx.fillStyle = 'black';
          ctx.fillText(`${e.weight}`, (v.pos.x + e.destination.pos.x) / 2, (v.pos.y + e.destination.pos.y) / 2);
        }
      }
      for (let v of subgraph) {
        ctx.beginPath();
        let gradient = ctx.createRadialGradient(v.pos.x - 5, v.pos.y - 5, 1, v.pos.x - 5, v.pos.y - 5, 15);
        gradient.addColorStop(0, '#fff');
        gradient.addColorStop(1, color);
        ctx.fillStyle = gradient;
        ctx.arc(v.pos.x, v.pos.y, 20, 0, Math.PI * 2, true);
        ctx.fill();
        ctx.font = 'bold 20px arial';
        ctx.fillStyle = 'black';
        ctx.fillText(`${v.value.slice(1, v.value.length)}`, v.pos.x, v.pos.y + 2);
      }
    }
  }
  
  /**
   * Render
   */
  render() {
    this.handleClick = this.handleClick.bind(this);
    return (
    <div>
      <canvas onClick={this.handleClick} ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
    </div>
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
      graph: new Graph(),
    };
  }

  newGraph = () => {
    const newGraph = new Graph();
    this.setState({ graph: newGraph });
  }

  listen = () => {
    this.setState({ listening: true });
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.newGraph}>Grapherator</button>
      </div>
    );
  }
}

export default App;