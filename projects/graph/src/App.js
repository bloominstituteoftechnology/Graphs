import React, { Component } from "react";
import { Graph, Vertex, Edge } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 800;
const canvasHeight = 800;
const vertexRadius = 25;
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
    let ctx = canvas.getContext("2d");

    // Clear it
    var grd = ctx.createLinearGradient(0, 0, 1000, 600);
    grd.addColorStop(0, "salmon");
    grd.addColorStop(1, "purple");

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const debugVertex = () => {
      let debug0 = new Vertex("debug0", { x: 100, y: 100 });
      let debug1 = new Vertex("debug1", { x: 800, y: 300 });

      debug0.edges.push(new Edge(debug1));
      debug1.edges.push(new Edge(debug0));

      this.props.graph.vertexes.push(debug0);
      this.props.graph.vertexes.push(debug1);

      const connect = (startingVertex, endingVertex, biDirectional = false) => {
        if (!startingVertex || !endingVertex) return console.log({Oops: 'Need a startingVertex and an endingVertex.'});

        if(!biDirectional){
          ctx.beginPath();
          let startingPosition = startingVertex.position;
          let endingPosition = endingVertex.position;

          ctx.moveTo(startingPosition.x, startingPosition.y);
          ctx.lineTo(endingPosition.x, endingPosition.y);
          ctx.stroke();

          let d = Math.sqrt(Math.pow((endingPosition.x - startingPosition.x), 2) + Math.pow((endingPosition.y - startingPosition.y), 2));
          let t = vertexRadius / d;
          let edgePostion = {x: ((1 - t)*endingPosition.x + t*startingPosition.x), y: ((1 - t)*endingPosition.y + t*startingPosition.y)}
        
          ctx.beginPath();
          ctx.fillStyle = 'green';
          console.log({edgePostion});
          ctx.moveTo(edgePostion.x, edgePostion.y);
          ctx.lineTo(startingPosition.x + vertexRadius * 2, startingPosition.y);
          ctx.stroke();
          // ctx.moveTo(edgePostion.x, edgePostion.y);

        // ctx.fill();
        //   ctx.arc(
        //   edgePostion.x,
        //   edgePostion.y,
        //   vertexRadius /4,
        //   0,
        //   2 * Math.PI
        // );

        } 
        return console.log({startingVertex, endingVertex, biDirectional});
      }
      console.log(connect(debug0, debug1));
    };

    debugVertex();

    console.log(this.props.graph);

    // const pulse = setInterval(() => {
      this.props.graph.vertexes.forEach((vertex, i) => {
        ctx.beginPath();
        ctx.arc(
          vertex.position.x,
          vertex.position.y,
          vertexRadius,
          0,
          2 * Math.PI
        );
        ctx.stroke();

        ctx.fillStyle = "aqua";
        ctx.fill();
        ctx.fillStyle = "black";
        ctx.font = "12px Ariel";
        ctx.textAlign = "center";
        ctx.fillText(`V${i}`, vertex.position.x, vertex.position.y);
      });
    // }, 2000);

    // clearInterval(pulse);

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
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
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
        <GraphView graph={this.state.graph} />
      </div>
    );
  }
}

export default App;
