import React, { Component } from "react";
import { Graph } from "./graph";
import "./App.css";

// !!! IMPLEMENT ME
const canvasWidth = 1100;
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
    // console.log("did mount");
  }

  /**
   * On state update
   * It will only fire when the state has changed
   * i.e. whenver setState() is called
   */
  componentDidUpdate() {
    this.updateCanvas();
    // console.log("did update");
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext("2d");

    // call dummy graph
    // console log confirms this.props.graph is being rendered
    // console.log("this.props.graph", this.props.graph);
    // console.log("createDummyGraph", this.props.graph.createDummyGraph);

    // Clear it
    ctx.clearRect(0, 0, canvasWidth, canvasWidth);
    ctx.fillStyle = "#3c4047";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // draw dummy vertex (hardcoded)
    // ctx.beginPath();
    // ctx.arc(10, 10, 10, 0, 2 * Math.PI); // x, y, radius, start angle, finish angle
    // ctx.stroke();
    // ctx.closePath();

    // ctx.beginPath();
    // ctx.arc(100, 100, 10, 0, 2 * Math.PI); // x, y, radius, start angle, finish angle
    // ctx.stroke();
    // ctx.closePath();

    // edges
    for (let vertex of this.props.graph.vertexes) {
      for (let edge of vertex.edges) {
        // console.log(edge.destination.color_connect)

        if (edge.weight) {
          ctx.fillStyle = "white";
          ctx.font = "12px arial";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";

          let edgeAvg_x = (vertex.pos.x + edge.destination.pos.x) / 2;
          let edgeAvg_y = (vertex.pos.y + edge.destination.pos.y) / 2;
          let edgeSum_x = Math.abs(vertex.pos.x - edge.destination.pos.x);
          let edgeSum_y = Math.abs(vertex.pos.y - edge.destination.pos.y);

          if (edgeSum_x > edgeSum_y) {
            ctx.fillText(edge.weight, edgeAvg_x, edgeAvg_y - 10);
          } else if (edgeSum_x < edgeSum_y) {
            if (vertex.pos.x > edge.destination.pos.x) {
              ctx.fillText(
                edge.weight,
                edgeAvg_x - 10,
                edgeAvg_y
              );
            } else if (vertex.pos.x < edge.destination.pos.x)
              ctx.fillText(
                edge.weight,
                edgeAvg_x + 10,
                edgeAvg_y
              );
          }
        }
        ctx.strokeStyle = edge.destination.color_connect;
        ctx.beginPath();
        ctx.moveTo(vertex.pos.x, vertex.pos.y);
        ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
        ctx.closePath();
        ctx.stroke();
      }
    }

    // draw dummy verticies (dynamic)
    this.props.graph.vertexes.forEach(v => {
      // verts

      /* connected component checker */
      if (v.color2) {
        ctx.fillStyle = v.color2;
      } else {
        ctx.fillStyle = v.color;
      }
      // ctx.fillStyle = v.color;

      ctx.strokeStyle = v.color_connect; // connected vertecies color
      ctx.beginPath();
      ctx.arc(v.pos.x, v.pos.y, 14, 0, 2 * Math.PI);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // vert values (labels)
      /* connected component checker */
      if (v.color === "black") {
        ctx.fillStyle = "white";
        if (v.color2) {
          ctx.fillStyle = "black";
        }
      } else {
        ctx.fillStyle = "black";
      }
      // ctx.fillStyle = "white";

      ctx.font = "11px arial";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(v.value, v.pos.x, v.pos.y);
    });

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
    // this.state.graph.createDummyGraph();
    this.state.graph.randomize(8, 5, 115, 0.6);
    this.state.graph.bfs();
    // this.state.graph.getConnectedComponents();
  }

  generateGraph() {
    this.setState((this.state.graph = new Graph())); // setState to fire componentDidUpdate()
    this.state.graph.randomize(8, 5, 115, 0.6);
    this.state.graph.bfs();
    // console.log(this.state.graph.vertexes);
    // window.location.reload(true);
  }

  // this.state.graph.bfs()
  // this.state.graph.randomize(5, 4, 150, 0.6),
  render() {
    return (
      <div className="App">
        <h3>Legend - black: stem vertex / yellow: connecting vertecies</h3>
        <GraphView graph={this.state.graph} />
        <div>
          <button onClick={this.generateGraph.bind(this)}>
            Generate Graph!
          </button>
        </div>
      </div>
    );
  }
}

export default App;
