import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
// const canvasWidth = 1200;
// const canvasHeight = 900;
const canvasWidth = window.innerWidth;
const canvasHeight = window.innerHeight - 50;
const circleRadius = 15;
const canvasStartX = 0;
const canvasStartY = 0;

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
    let left = canvas.offsetLeft;
    let top = canvas.offsetTop;
    let ctx = canvas.getContext('2d');
    // this.props.graph.createDummyGraph();
    // this.props.graph.dump();
    let myGraph = this.props.graph;
    
    
    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(canvasStartX, canvasStartY, canvasWidth, canvasHeight);
    // ctx.fillRect(100, 100, canvas.width, canvas.height);

    myGraph.randomize(canvasWidth / 155, canvasHeight / 170, 149, .4);
    ctx.font = '13px Arial';  //font and size of text
    ctx.textAlign = 'center';  //location of text on x axis 
    ctx.textBaseline = 'middle';  //location of text on y axis

    // !!! IMPLEMENT ME
    // compute connected components
    const checkedEdges = {};
    const checkedVerts = {};
    myGraph.vertexes.forEach(v => {
      checkedVerts[v.value] = false;
      checkedEdges[v.value] = false;
    })

    canvas.addEventListener('click', function(event) {
      let x = event.pageX - left;
      let y = event.pageY - top;

      myGraph.vertexes.forEach(v => {
        let vertX = v.pos.x;
        let vertY = v.pos.y;
        let xDiff = Math.abs(vertX - x);
        let yDiff = Math.abs(vertY - y);
        if(xDiff < circleRadius && yDiff < circleRadius) {
          console.log(`${v.value} was clicked`);
        }
      })
    }, false);

    const uncheckedEdges = [];
    for (let i = 0; i < myGraph.vertexes.length; i++) {
      let vert = myGraph.vertexes[i];
      if (!checkedEdges[vert.value]) {
        let current = vert;
        let color = vert.color;
        uncheckedEdges.push(current);
        checkedEdges[vert.value] = true;
        while (uncheckedEdges.length > 0) {
          for (let j = 0; j < current.edges.length; j++) {
            if (!checkedEdges[current.edges[j].destination.value]) {
              checkedEdges[current.edges[j].destination.value] = true;
              current.edges[j].destination.color = color;
              uncheckedEdges.push(current.edges[j].destination);
            }
          }
          let vertex = uncheckedEdges.shift();
          ctx.fillStyle = color;  //sets color for the circle
          ctx.strokeStyle = color;  //sets color for the circle's edge
          for (let j = 0; j < vertex.edges.length; j++) {
            ctx.beginPath();
            ctx.moveTo(vertex.pos.x + canvasStartX, vertex.pos.y + canvasStartY);
            // draw edges
            ctx.lineTo(vertex.edges[j].destination.pos.x + canvasStartX, vertex.edges[j].destination.pos.y + canvasStartY);
            ctx.stroke();
          }
          current = uncheckedEdges[0];
        }
      }
    }

    const unchecked = [];
    for (let i = 0; i < myGraph.vertexes.length; i++) {
      let v = myGraph.vertexes[i];
      if (!checkedVerts[v.value]) {
        let current = v;
        let color = v.color;
        unchecked.push(current);
        checkedVerts[v.value] = true;
        while (unchecked.length > 0) {
          for (let j = 0; j < current.edges.length; j++) {
            if (!checkedVerts[current.edges[j].destination.value]) {
              checkedVerts[current.edges[j].destination.value] = true;
              current.edges[j].destination.color = color;
              unchecked.push(current.edges[j].destination);
            }
          }
          let vertex = unchecked.shift();
          ctx.fillStyle = color;  //sets color for the circle
          ctx.strokeStyle = color;  //sets color for the circle's edge

          ctx.beginPath();
          // draw verts
          ctx.arc(vertex.pos.x + canvasStartX, vertex.pos.y + canvasStartY, circleRadius, 0, 2 * Math.PI);  //(x,y) center of cicle, radius, arc of circle (in radians)
          ctx.fill();  //fills in the circle
          ctx.stroke();  //draws the circle

          // draw vert values (labels)
          ctx.fillStyle = 'black';  //sets color for the text
          ctx.fillText(vertex.value, vertex.pos.x + canvasStartX, vertex.pos.y + canvasStartY);  //fill in the text of v.value @ (x,y) of (v.pos.x, v.pos.y);
          current = unchecked[0];
        }
      }
    }

    myGraph.dump();
  }

  /**
   * Render
   */
  render() {
    return <canvas id='myCanvas' ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>;
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

    this.timer = null;
    this.counter = 1000;
    this.stopRandomize.bind(this);
    this.setDefault = true;
  }

  // !!! IMPLEMENT ME
  // use the graph randomize() method
  randomize = () => {
    this.setState({ graph: new Graph() });
  }

  randomizeIndefinitely = () => {
    clearInterval(this.timer);
    this.timer = setInterval(this.randomize, this.counter);
  }

  increaseRandomize = () => {
    this.setDefault = false;
    this.stopRandomize();
    this.counter *= .8;
    this.timer = setInterval(this.randomize, this.counter);
  }

  decreaseRandomize = () => {
    this.setDefault = false;
    this.stopRandomize();
    this.counter *= 1.2;
    this.timer = setInterval(this.randomize, this.counter);
  }

  stopRandomize = () => {
    clearInterval(this.timer);
    if (this.setDefault) this.counter = 1000;
    this.setDefault = true;
  }

  findThisElem = e => {
    e.preventDefault();

  }

  render() {
    return (
      <div className="App">
        <div>
          <GraphView elemFinder={this.findThisElem} graph={this.state.graph}></GraphView>
        </div>
        <div>
          <button onClick={this.randomize}>Random </button>
          <button onClick={this.increaseRandomize}>Speed Up </button>
          <button onClick={this.randomizeIndefinitely}>Continuous </button>
          <button onClick={this.decreaseRandomize}>Slow Down </button>
          <button onClick={this.stopRandomize}>STOP </button>
        </div>
      </div>
    );
  }
}

export default App;
