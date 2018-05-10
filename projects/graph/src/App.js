import React, { Component } from "react";
import { Graph, Vertex, Edge } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 1000;
const canvasHeight = 1000;
const vertexRadius = 15;
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
    var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
    grd.addColorStop(0, "salmon");
    grd.addColorStop(1, "purple");
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    let noRedos = [];
    let vertexes = this.props.graph.vertexes;
    vertexes.forEach(vertex => {
      let {value, pos, edges} = vertex;

      if(vertex.edges) {
        vertex.edges.forEach(e => {

        let ePos = {x: e.destination.pos.x, y: e.destination.pos.y}
        ctx.beginPath();
        ctx.moveTo(pos.x, pos.y);
        let d = Math.sqrt(Math.pow((ePos.x - pos.x), 2) + Math.pow((ePos.y - pos.y), 2));
        let t = vertexRadius / d;
        let circleEdge = {
          x: (1 - t) * ePos.x + t * pos.x,
          y: (1 - t) * ePos.y + t * pos.y
        }; 
        ctx.lineTo(circleEdge.x, circleEdge.y);
        noRedos.push({e, vertex});
        ctx.stroke();
        });
      }

      ctx.beginPath();
      ctx.arc(
        pos.x,
        pos.y,
        vertexRadius,
        0,
        2 * Math.PI
      );
      ctx.fillStyle = "white";
      ctx.fill();
      ctx.fillStyle = "black";
      ctx.font = "12px Ariel";
      ctx.textAlign = "center";
      ctx.fillText(`${vertex.value}`, pos.x, pos.y + 3);
    });
  //   const debugVertex = () => {
  //     let debug0 = new Vertex("D0", { x: 100, y: 100 });
  //     let debug1 = new Vertex("D1", { x: 200, y: 300 });
  //     let debug2 = new Vertex("D2", { x: 400, y: 100 });

  //     debug0.edges.push(new Edge(debug1));
  //     debug1.edges.push(new Edge(debug0));

  //     this.props.graph.vertexes.push(debug0);
  //     this.props.graph.vertexes.push(debug1);
  //     this.props.graph.vertexes.push(debug2);

  //     const connect = (startingVertex, endingVertex) => {
  //       if (!startingVertex || !endingVertex)
  //         return console.log({
  //           Oops: "Need a startingVertex and an endingVertex."
  //         });

  //       ctx.beginPath();
  //       let startingPosition = startingVertex.position;
  //       let endingPosition = endingVertex.position;
  //       ctx.moveTo(startingPosition.x, startingPosition.y);
  //       ctx.lineTo(endingPosition.x, endingPosition.y);
  //       ctx.stroke();

  //       // let d = Math.sqrt(
  //       //   Math.pow(endingPosition.x - startingPosition.x, 2) +
  //       //     Math.pow(endingPosition.y - startingPosition.y, 2)
  //       // );
  //       // let t = vertexRadius / d;
  //       // let edgePostion = {
  //       //   x: (1 - t) * endingPosition.x + t * startingPosition.x,
  //       //   y: (1 - t) * endingPosition.y + t * startingPosition.y
  //       // };

  //       // ctx.beginPath();
  //       // ctx.fillStyle = "green";
  //       // console.log({ edgePostion });
  //       // ctx.moveTo(edgePostion.x, edgePostion.y);
  //       // ctx.lineTo(startingPosition.x + vertexRadius * 2, startingPosition.y * 2);
  //       // ctx.stroke();
  //       // ctx.moveTo(edgePostion.x, edgePostion.y);

  //       // ctx.fill();
  //       //   ctx.arc(
  //       //   edgePostion.x,
  //       //   edgePostion.y,
  //       //   vertexRadius /4,
  //       //   0,
  //       //   2 * Math.PI
  //       // );
  //     };
  //     connect(debug0, debug1);
  //     connect(debug1, debug2);
  //     console.log(this.props.graph);
  //   };

  //   debugVertex();

  //   this.props.graph.vertexes.forEach((vertex, i) => {
  //     ctx.beginPath();
  //     ctx.arc(
  //       vertex.position.x,
  //       vertex.position.y,
  //       vertexRadius,
  //       0,
  //       2 * Math.PI
  //     );
  //     ctx.stroke();

  //     ctx.fillStyle = "aqua";
  //     ctx.fill();
  //     ctx.fillStyle = "black";
  //     ctx.font = "12px Ariel";
  //     ctx.textAlign = "center";
  //     ctx.fillText(`D${i}`, vertex.position.x, vertex.position.y);
  //   });
  // }

    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)

  /**
   * Render
   */
 }

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
  this.state.graph.randomize(6, 6, 160, .5);
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
