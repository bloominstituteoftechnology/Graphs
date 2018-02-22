import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

const canvasWidth = window.innerWidth;
const canvasHeight = window.innerHeight;

/**
 * GraphView
 */
class GraphView extends Component {
  constructor(){
    super();
    this.state = { graph: [], ctx : null };
  }
  componentWillReceiveProps(nextProps) {
    clearTimeout(this.timeout);
    this.setState({ graph: nextProps.graph.getConnectedComponents() });
  }
  /**
   * On mount
   */
  componentDidMount() {
    this.setState({ graph: this.props.graph.getConnectedComponents() });
    this.updateCanvas();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvas();
  }

  /**
   * handle BFS
   */
  handleBFS = () => {
    // a simple implementation of drawing bfs-> 
    // not sure how to clearTimeout here on graphChange btn click
    const bfsPos = this.props.graph.bfs(this.state.graph[0]);
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    const drawBFS = (pos, interval) => {
      setTimeout(() => {
          ctx.beginPath();
          ctx.arc(pos.x, pos.y, 22, 0, 2 * Math.PI, false);
          const grd = ctx.createLinearGradient(0,500,0, 0);
          grd.addColorStop(0, 'salmon');
          grd.addColorStop(1, '#40d6a5');
          ctx.fillStyle = grd;
          ctx.fill();
          ctx.lineWidth = 2;
          ctx.strokeStyle = '#000';
          ctx.stroke();
      }, interval);
    }
    for (let i = 0; i < bfsPos.length; i++) {
      drawBFS(bfsPos[i], i * 1000);
    }
  }
  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = '#ffcf75';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const getRandomColor = () => {
      const colors = ['#e1f5fe', '#b3e5fc', '#81d4fa', '#4fc3f7', '#29b6f6', '#03a9f4', '#039be5', '#0288d1', '#0277bd', '#01579b'];
      return colors[Math.floor(Math.random() * 10)];
    }
    // !!! IMPLEMENT ME
    // draw edges
    this.state.graph.forEach(v => {
      v.edges.forEach(e => {
        const v2 = e.destination;
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.strokeStyle = getRandomColor();
        ctx.moveTo(v.pos.x, v.pos.y);
        ctx.lineTo(v2.pos.x, v2.pos.y);
        ctx.stroke();

        /////////////////
        ////////////////
        // stretch 1
        // draw weight values
        ctx.font = '18px serif';
        ctx.fillStyle = 'black';
        ctx.textAlign="center"; 
        ctx.fillText(e.weight, (v.pos.x + v2.pos.x)/2, (v.pos.y + v2.pos.y)/2);
      });      
    });

    this.state.graph.forEach(v => {
      // draw verts
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, 22, 0, 2 * Math.PI, false);
      ctx.fillStyle = '#333';
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#fff';
      ctx.stroke();

      // draw vert values (labels)
      ctx.font = '18px serif';
      ctx.fillStyle = '#fff';
      ctx.textAlign="center"; 
      ctx.fillText(v.value, v.pos.x, v.pos.y + 5);
    });



    /////////////////
    ////////////////
    // stretch 2

    const isIntersect = (point, circle) => {
      return Math.sqrt((point.x-circle.x) ** 2 + (point.y - circle.y) ** 2) < 22; // radius
    }
    
    canvas.addEventListener('click', (e) => {
      const mousePos = {
        x: e.clientX,
        y: e.clientY
      };
      this.state.graph.forEach(circle => {
        if (isIntersect(mousePos, circle.pos)) {
          alert('click on circle: ' + circle.value);
        }
      });
    });
  }
  
  /**
   * Render
   */
  render() {
    return (
      <div>
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
        <button className="btn" onClick={
          this.props.changeGraph        
        }>New Graph</button>
        <button className="bfs-btn" onClick={
          this.handleBFS
        }>Run BFS</button>
      </div>
    )
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);
    this.state = { graph: new Graph() };
    this.state.graph.randomize(5, 4, 150, 0.6);
  }

  changeGraph = () => {
    const state = { graph: new Graph() };
    state.graph.randomize(5, 4, 150, 0.6);
    this.setState(state);
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} changeGraph={this.changeGraph} ></GraphView>        
      </div>
    );
  }
}

export default App;
