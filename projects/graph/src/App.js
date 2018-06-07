import React, {
  Component
} from 'react';
import {
  Graph
} from './graph';
import './App.css';

// !!! IMPLEMENT ME
//Global Variables
const canvasWidth = 850;
const canvasHeight = 600;

const circleSize = 15;

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
    ctx.fillStyle = 'grey';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);



    //Create a forEach method to iterate the vertexes (produce more vertexes)
    //Difference between forEach in and forEach of is: 
    //forEach in: goes inside of all of the array properties
    //forEach of: goes over the iterable properties

    //Global Variables
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '16px Arial';

    //Drawing of the graph(updates)
    for (let vertex of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(vertex.pos.x, vertex.pos.y, circleSize, 0, 2 * Math.PI);
      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.fillStyle = 'black';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      ctx.stroke();
    }


    // !!! IMPLEMENT ME
    // TODO: compute connected components

    // TODO: draw edges
    //Refactored code to mimic graph.js variables for edges and vertexes
    for (let v of this.props.graph.vertexes) {
      for (let e of v.edges) {
        ctx.beginPath();
        ctx.moveTo(v.pos.x, v.pos.y);
        //setting the connection 
        v = e.destination;
        //making the connection of the points
        ctx.lineTo(v.pos.x, v.pos.y);
        ctx.stroke();

      }
    }
    // TODO: draw verts
    //(loop)
    for (let v of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, circleSize, 0, 2 * Math.PI, false);
      ctx.fillStyle = v.color; //set to variable to initiate the randomColor function
      ctx.fill();
      ctx.stroke();
    }


    // TODO: draw vert values (labels)
    for (let v of this.props.graph.vertexes) {
      ctx.beginPath();
      ctx.fillStyle = 'black';
      ctx.textAlign = 'cener';
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    }

  }

  /**
   * Render
   */
  render() {
    return <canvas ref = "canvas"
    width = {
      canvasWidth
    }
    height = {
      canvasHeight
    } > < /canvas>;
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

    //binding the button
    this.randomGraph = this.randomGraph.bind(this);

    // !!! IMPLEMENT ME
    //TODO: Also add bfs here as well to showcase the colors and structure
    // use the graph randomize() method
    // this.state.graph.debugCreateTestData();
    this.state.graph.randomize(5, 3, 150, 0.6);
    //testing bfs
    // this.state.graph.bfs(this.state.graph.vertexes[0]);
    //testing getConnectedComponents
    this.state.graph.getConnectedComponents();
  }
  //TODO: Need to somehow connect my randomized functions to get the colors to be random as well
  //randomGraph function
  randomGraph() {
    let newGraph = new Graph();
    newGraph.randomize(5, 3, 150, 0.6);
    this.setState({
      graph: newGraph
    });
  }

  render() {
    return ( <
      div className = "App" >
      <
      GraphView graph = {
        this.state.graph
      }
      />  <
      button onClick = {
        this.randomGraph
      } > Random Graph < /button>< /
      div >
    );
  }
}

export default App;