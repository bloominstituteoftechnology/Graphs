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
    function windowToCanvas(canvas,x,y){
      let bbox = canvas.getBoundingClientRect();
      return {x:x-bbox.left*(canvas.width/bbox.width),
      y:y-bbox.top*(canvas.height/bbox.height)
      };
    }
    let vertexes = this.props.graph.vertexes;
    let start = null;
    let end = null;

    canvas.addEventListener('mousedown',function(e){
      let loc = windowToCanvas(canvas,e.clientX,e.clientY);
      let x0 = loc.x;
      let y0 = loc.y;
      vertexes.forEach(vertex=>{
        let x1 = vertex.pos.x;
        let y1 = vertex.pos.y;
        let distance = Math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0));
        if(distance < 15){
          if(start === null){
            start = vertex;
          }
          else{
            end = vertex;
          }
        }
      });
      console.log(start,end);
    });
    
    // Clear it
    ctx.fillStyle = 'orange';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    this.props.graph.connectedComponents.forEach(component=>{
      ctx.strokeStyle = '#' + (Math.random() * 0xFFFFFF << 0).toString(16);
      component.forEach(vertex=>{
        vertex.edges.forEach(edge=>{
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x,vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x,edge.destination.pos.y);
          ctx.stroke();
          ctx.beginPath();
          //ctx.moveTo((vertex.pos.x + edge.destination.pos.x) / 2, (vertex.pos.y + edge.destination.pos.y) / 2);
          ctx.fillStyle="black";
          let x = (vertex.pos.x + edge.destination.pos.x) / 2;
          let y = (vertex.pos.y + edge.destination.pos.y) / 2;
          ctx.fillText(edge.weight,x,y);
          ctx.stroke();
        });
      });
    });


   
    // draw verts
    vertexes.forEach(e=>{
      ctx.beginPath();
      ctx.strokeStyle=e.color;
      ctx.arc(e.pos.x,e.pos.y,15,0,2*Math.PI);
      ctx.stroke();
    });
    // draw vert values (labels)
    vertexes.forEach(e=>{
      ctx.beginPath();
      ctx.fillStyle="black"
      ctx.textAlign="center";
      ctx.textBaseline="middle";
      ctx.fillText(e.value,e.pos.x,e.pos.y,15);
    });


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
    this.newGraph= this.newGraph.bind(this);
    this.state.graph.randomize(5,4,150,0.6);
    this.state.graph.getConnectedComponents();
  }

  newGraph(e){
    window.location.reload();
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.newGraph}>Generate new random graph</button>
      </div>
    );
  }
}

export default App;
