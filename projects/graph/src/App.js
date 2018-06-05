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
    
    // Clear it
    ctx.fillStyle = '#222222';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // let debVert = this.props.graph.vertexes;

    let verts = this.props.graph.vertexes;

    console.log('can', verts)
    function truther(){
      let count = 0;
      for(let i = 0; i < verts.length; i++){
      if(verts[i].edges.length > 0){
        count++;
      }
      
    }
    return count;
    }

    console.log(verts[0].edges[0].destination.pos.x)
    console.log(truther());

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '20px Arial';
    

    for (let i = 0; i < verts.length; i++){
      if(verts[i].edges.length > 0){
        for(let edge of verts[i].edges){
        ctx.beginPath();
        ctx.strokeStyle = 'purple';
        ctx.lineWidth = 10;
        // ctx.moveTo(verts[i].pos.x, verts[i].pos.y);
        // ctx.lineTo(verts[i].edges[j].destination.pos.x, verts[i].edges[j].destination.pos.y);
        ctx.moveTo(verts[i].pos.x, verts[i].pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.stroke();
        }
        

      }
    }
    for (let vertex of verts) {
      ctx.beginPath();
      ctx.fillStyle = 'red';
      ctx.arc(vertex.pos.x, vertex.pos.y, vertex.size, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();
  
      ctx.fillStyle = 'white';
      ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);


    }





    
    

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)



    //   ctx.beginPath();
    //   let x = j * 20;
    //   let y = 8.5 * j;
    //   let radius = 70;
    //   let startAngle = 350;
    //   // let endAngle = Math.PI + (Math.PI * j) / 2;
    //   let endAngle = 25;
    //   // var anticlockwise = i % 2 !== 0;

    //   ctx.arc(x, y, radius, startAngle, endAngle);{

      
    //     ctx.stroke();
    //  }



      // ctx.beginPath();
      // let x = j * 20;
      // let y = 8.5 * j;
      // let radius = 20;
      // let startAngle = 0;
      // let endAngle = Math.PI + (Math.PI * j) / 2;
      // var anticlockwise = i % 2 !== 0;

      // ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise);

      // if (i > 1) {
      //   ctx.fill();
      // } else {
      //   ctx.stroke();
      // }

      



    




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

    this.state.graph.randomize(5, 4, 150, 0.6);

    this.state.graph.debugCreateTestData();
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
