import React, { Component } from 'react';
import { Graph } from './graph';
import Queue from './queue';
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
    const bfsPos = this.props.graph.bfsA(this.state.graph[0][0]);
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    this.bfsInterval = setInterval(() => {
      if (bfsPos.length !== 0) {
        const pos = bfsPos.shift();
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
      } else {
        clearInterval(this.bfsInterval);
      }
    }, 1000);
  }
  /**
  * handle BFS
  */
  handleDijkstra (selectedPath) {
    /////////////////
    ////////////////
    // stretch 3 not finished 

    const graphs = this.state.graph;
    let foundSelectedGraph;
    if (graphs.length > 1) {
      // it works if user selected two points on the same graph
      // but I can come back later to fix it
      graphs.forEach(g => {
        g.forEach((v, i)  => {
          if (selectedPath[0].value === v.value) {
            foundSelectedGraph = g;
            return;
          }
        })
      });
    } else {
      foundSelectedGraph = graphs[0];
    }
    // console.log(foundSelectedGraph)
    const foundPathPos = [];

    for (let i = 0; i < foundSelectedGraph.length; i ++) {
      foundSelectedGraph[i].color = 'white';
    }

    selectedPath[0].color = 'gray';
    selectedPath[0].test = 0;
    const queue = new Queue();
    queue.enqueue(selectedPath[0]);
    while (!queue.isEmpty()) {
      const u = queue.storage[0];
      for (let k = 0; k < u.edges.length; k++) {
        if (u.edges[k].destination.color === 'white') {
          u.edges[k].destination.color = 'gray';
          u.edges[k].destination.test = u.edges[k].weight + u.test;
          queue.enqueue(u.edges[k].destination);
        } else if (u.edges[k].destination.color === 'gray') {
          if (u.edges[k].weight + u.test <= u.edges[k].destination.test) {
            queue.enqueue(u.edges[k].destination);
          }
        }
      }
      queue.dequeue();
      console.log(u)
      if (u.value === selectedPath[1].value) {
        foundPathPos.push(u.pos);
        u.color = 'black';
        break;
      }
      foundPathPos.push(u.pos);
      u.color = 'black';      
    }
  
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    this.bfsInterval = setInterval(() => {
      if (foundPathPos.length !== 0) {
        const pos = foundPathPos.shift();
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
      } else {
        clearInterval(this.bfsInterval);
      }
    }, 1000);
  }

  /**
  * GetRandomEdgeColor
  */
  getRandomEdgeColor = () => {
    const colors = ['#e1f5fe', '#b3e5fc', '#81d4fa', '#4fc3f7', '#29b6f6', '#03a9f4', '#039be5', '#0288d1', '#0277bd', '#01579b'];
    return colors[Math.floor(Math.random() * 10)];
  }

  /**
  * GetRandomVertColor
  */
  getRandomVertColor = () => {
    const letters = '0123456789ABCDE';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 15)];
    }
    return color;
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

    // draw edges
    const graphs = this.state.graph;
    graphs.forEach(g => {
      g.forEach(v => {
        v.edges.forEach(e => {
          const v2 = e.destination;
          ctx.beginPath();
          ctx.lineWidth = 3;
          ctx.strokeStyle = this.getRandomEdgeColor();
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
    })

    graphs.forEach(g => {
      const randomVertColor = this.getRandomVertColor();
      g.forEach(v => {
      // draw verts
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, 22, 0, 2 * Math.PI, false);
      ctx.fillStyle = randomVertColor;
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
    });


    /////////////////
    ////////////////
    // stretch 2

    const isIntersect = (point, circle) => {
      return Math.sqrt((point.x-circle.x) ** 2 + (point.y - circle.y) ** 2) < 22; // radius
    }
    

    this.selectedPath = [];
    let allowedToSelect = true;
    canvas.addEventListener('click', (e) => {
      const mousePos = {
        x: e.clientX,
        y: e.clientY
      };
      graphs.forEach(g => {
        g.forEach(circle => {
          if (isIntersect(mousePos, circle.pos) && allowedToSelect) {
            if (this.selectedPath.length === 0) {
              this.selectedPath.push(circle);
            } else if (this.selectedPath.length === 1) {
              this.selectedPath.push(circle);
              allowedToSelect = false;
            }
            ctx.beginPath();
            ctx.arc(circle.pos.x, circle.pos.y, 22, 0, 2 * Math.PI, false);
            ctx.fillStyle = '#000';
            ctx.fill();
            ctx.lineWidth = 4;
            ctx.strokeStyle = '#fff';
            ctx.stroke();
          }
        });
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
        <button className="btn" onClick={() => {
            clearInterval(this.bfsInterval);
            this.props.changeGraph();
          }
        }>New Graph</button>
        <button className="bfs-btn" onClick={
          this.handleBFS
        }>Run BFS</button>
        <button className="dijk-btn" onClick={
          () => {
            this.handleDijkstra(this.selectedPath)
          }
        }>Dijkstra</button>
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
