import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;

/**
 * GraphView
 */
class GraphView extends Component {
  state = {
    count: 1,
    bubbles: [],
    maxBubbles: 100,
    graph: "test data",
  }

  componentWillUnmount () {
    clearInterval(this.timer);
  }

  /**
   * On mount
   */
  async componentDidMount() {
    const graph = new Graph();
    console.log("About to print out the newly generated graph:", graph);
    await this.setState({ graph: graph });
    console.log("State of graph is:", this.state.graph);
    this.state.graph.randomize(5, 4, 150);
    console.log("Randomized the graph");
    const randomColor = () => {
      const r = Math.floor(Math.random()*255);
      const g = Math.floor(Math.random()*255);
      const b = Math.floor(Math.random()*255);
      return `rgb(${r},${g},${b})`;
    }
    this.state.graph.vertexes.forEach(vertex => {
      const networks = this.state.graph.getConnectedComponents();
      console.log("These are the individual networks found: ", networks);
      networks.forEach(network => {
        const netColor = randomColor();
        network.forEach(vertex => {
          vertex.color = netColor;
        })
      })
    })
    this.updateCanvas();
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    //this.updateCanvas();
  }

  tick () {
    //this.setState({count: (this.state.count + 1)})
    if (this.state.count > 11) this.setState({count: 0})
    console.log("The timer ticked.");
    //this.updateCanvas();
  }
  startTimer () {
    clearInterval(this.timer)
    this.timer = setInterval(this.tick.bind(this), 50)
  }
  stopTimer () {
    clearInterval(this.timer)
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');
    
    const backgroundOlive = 'rgb(184,186,103)';
    const darkOlive = 'rgb(81,83,0)';
    const darkMedOlive = 'rgb(111,113,30)';
    const lightMedOlive = 'rgb(141,143,60)';
    const lightOlive = 'rbg(171,173,90)';

    const colors = [darkOlive, darkMedOlive, lightMedOlive, lightOlive];

    ctx.fillStyle = backgroundOlive;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    this.state.graph.vertexes.forEach(vertex => {
      vertex.edges.forEach(edge => {
        ctx.beginPath();
        ctx.strokeStyle = lightMedOlive;
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        ctx.closePath();
      });
    });
    this.state.graph.vertexes.forEach(vertex => {
      ctx.beginPath();
      ctx.fillStyle = vertex.color;
      ctx.arc(vertex.pos.x, vertex.pos.y, 10, 0, 2*Math.PI);
      ctx.fill();
      ctx.fillStyle = "rgb(200,200,200)";
      ctx.font = '10px serif';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.closePath();
    });
    
    // const seed = Math.floor(Math.random() * 10);

    // if (seed < 4 && this.state.bubbles.length < this.state.maxBubbles) {
    //   this.state.bubbles.push({
    //     color: colors[seed],
    //     x: Math.floor(Math.random()*canvasWidth),
    //     y: Math.floor(Math.random()*canvasHeight),
    //     radius: 25,
    //     degrees: 0,
    //   })
    // }

    // this.state.bubbles.forEach((bubble, index) => {
    //   //bubble.radius++,
    //   bubble.degrees = bubble.degrees+=((2*Math.PI)/360);
    //   if (bubble.degrees > 2 * Math.PI) {
    //     const newBubbleArray = this.state.bubbles.slice(0,index).concat(this.state.bubbles.slice(index+1));
    //     this.setState({
    //       bubbles: newBubbleArray
    //     })
    //   }
    //   ctx.beginPath();
    //   ctx.strokeStyle = bubble.color;
    //   ctx.arc(bubble.x, bubble.y, bubble.radius, 0, bubble.degrees);
    //   ctx.stroke();
    // })
    

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
  }
  
  /**
   * Render
   */
  render() {
    return <div>
      <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
      <button onClick={() => this.startTimer()}>Start</button>
      <button onClick={() => this.stopTimer()}>Stop</button>
    </div>
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
