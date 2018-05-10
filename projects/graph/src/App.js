import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;
const radius = 20;
let limitListenerCreation = false;
let color;
let groupsSet = false;

function drawLine(startx, starty, finx, finy, ctx) {
  // ctx.strokeStyle = 'black';
  ctx.strokeStyle = color;
  ctx.moveTo(startx, starty)
  ctx.lineTo(finx, finy);
}

function drawCircle(vertex, ctx) {
  ctx.strokeStyle = 'black';  
  ctx.arc(vertex.pos.x, vertex.pos.y, radius, 0, 2*Math.PI);
  // var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
  fillColor(vertex, ctx);
  writeTheText(vertex, ctx);
}

function checkIntersect(point, vertex) {
  return Math.sqrt(Math.pow(point.x - vertex.pos.x, 2) + Math.pow(point.y - vertex.pos.y, 2)) < radius;
}

function fillColor(vertex, ctx) {
  // let color = 'white';
  // const len = vertex.edges.length;
  // switch (true) {
  //   case len === 0:
  //     color = 'maroon';
  //     break;
  //   case len === 1:
  //     color = 'lightblue';
  //     break;
  //   case len === 2:
  //     color = 'lightskyblue';
  //     break;
  //   case len === 3:
  //     color = 'dodgerblue';
  //     break;
  //   case len === 4:
  //     color = 'blue';
  //     break;
  //   case len >= 5:
  //     color = 'purple';
  //     break;
  //   default:
  //     color = 'orange';
  //     break;      
  // }
  ctx.fillStyle = color;
  ctx.fill();
}

function writeTheText(vertex, ctx) {
  ctx.fillStyle = 'white';
  ctx.font = '20px Arial';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

/**
 * GraphView
 */
class GraphView extends Component {
  state = {
    currentVertex: null,
    groups: this.props.graph.getConnectedComponents(this.props.graph.vertexes),
  }
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvas();
    groupsSet = true;
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    if(!groupsSet){
      // console.log("fine, we are updating", this.state.groups);
      this.updateCanvas();
      groupsSet = true;      
    }
  }

  /**
   * Render the canvas
   */

  // setGroups() {
  //   console.log("the groups have been set!");
  //   this.setState({groups: this.props.graph.getConnectedComponents(this.props.graph.vertexes)});
  //   groupsSet = true;
  // }

  updateCanvas() {
    let canvas = this.refs.canvas;
    if (!limitListenerCreation) {
      limitListenerCreation = true;
      canvas.addEventListener('click', (e) => {
        var rect = canvas.getBoundingClientRect();
        const mousePoint = {
          x: (e.clientX - rect.left) / (rect.right - rect.left) * canvas.width,
          y: (e.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height
        };
        // console.log(this.props.graph.vertexes);
        this.props.graph.vertexes.forEach(circle => {
          // console.log(checkIntersect(mousePoint, circle));
          if (checkIntersect(mousePoint, circle)) {
            // alert('click on circle: ' + circle.value);
            // console.log(circle);
            this.setState({ currentVertex: circle });
          }
        });
      });
    }
    let ctx = canvas.getContext('2d');
    
    // Clear it
    if (!groupsSet) {
      ctx.fillStyle = 'black';
      ctx.fillRect(0, 0, canvasWidth, canvasHeight);
      ctx.fillStyle = 'white';
      ctx.fillRect(2, 2, canvasWidth-4, canvasHeight-4);
      ctx.lineWidth = 5;

      // console.log(this.state.groups);
      this.state.groups.forEach((group) => {
        color = `rgb(${getRandomInt(255)},${getRandomInt(255)},${getRandomInt(255)})`;  
        
        for (let vertex of group) {
          // console.log(vertex);
          ctx.beginPath();
          for (let edge of vertex.edges) {
            drawLine(vertex.pos.x, vertex.pos.y, edge.destination.pos.x, edge.destination.pos.y, ctx);
          }
          ctx.stroke();
        }

        ctx.lineWidth = 3;
        for (let vertex of group) {
          ctx.beginPath()
          drawCircle(vertex, ctx);
          ctx.stroke();
        }
      });
    }
    

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
    const vert = this.state.currentVertex;
    return (
      <div className="canvas_container">
        <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
        <button className="canvas_button" onClick={() => {
          groupsSet = false;
          const newGraph = new Graph();
          newGraph.randomize(5, 5, 150, 0.6);
          // console.log("new graph:", newGraph.vertexes);
          this.setState({groups: newGraph.getConnectedComponents(newGraph.vertexes), currentVertex: null});
          this.props.updateGraph(newGraph);
          }}
        >New Graph
        </button>
    {this.state.currentVertex === null ?
        <div className="canvas_test"></div> : 
        <div>
          <div>
            {vert.value}
          </div>
          <div>
            X: {vert.pos.x} Y: {vert.pos.y}
          </div>
          <div>
            EDGES: {vert.edges.length > 0 ? vert.edges.map((elem) => {
              return [` ${elem.destination.value} `];
            }) : 'None'
            }
          </div>
        </div>}
      </div>
    )
  }
}


/**
 * App
 */
class App extends Component {
  state = {
    graph: new Graph()
  };

  // !!! IMPLEMENT ME
  // use the graph randomize() method
  componentWillMount() {
    this.state.graph.randomize(5, 5, 150, 0.6);
  }

  updateGraph = (graph) =>{
    this.setState({graph: graph});
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} updateGraph={this.updateGraph}></GraphView>
      </div>
    );
  }
}

export default App;