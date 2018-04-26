import React, { Component } from 'react';
import { Graph } from './graph';
import ReloadButton from './components/reload';
import './App.css';

const width = 12;
const height = 5;
const jitter = 150;
const vertexRadius = 12;
const font = 'Courier';
const prob = 0.4;
const backgroundColor = 'white';
const fontColor = 'white';
// const delay = 0;

const canvasWidth = width * jitter;
const canvasHeight = height * jitter;

const colors = {
  0: '#000000',
  1: '#808080',
  2: '#a9a9a9',
  3: '#d3d3d3',
  4: '#00008b',
  5: '#0000ff',
  6: '#add8e6',
  7: '#008000',
  8: '#90ee90',
  9: '#adff2f',
  10: '#ff00ff',
  11: '#8b008b',
  12: '#ffc0cb',
  13: '#ff1493',
  14: '#ff69b4',
  15: '#df25d5',
};

const getRandomColor = _ => {
  return '#' + Math.floor(Math.random() * 16777215).toString(16);
};

/**
 * GraphView
 */
class GraphView extends Component {
  state = {
    vS: null,
    vT: null,
  };

  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvas();
    window.alert(
      'It may be difficult to click on nodes when scrolling. Try zooming out when clicking on nodes (then zoom back in).',
    );
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    if (this.props.graph.vertexes.length === 0) {
      this.props.graph.randomize(width, height, jitter, prob);
      this.updateCanvas();
    } else if (this.state.vS !== null && this.state.vT !== null)
      this.findShortestPath();
    else if (this.state.vS !== null) this.updateCanvas([this.state.vS]);
  }

  /**
   * Render the canvas
   */
  updateCanvas(highlightCluster = []) {
    let canvas = this.refs.canvas;
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = backgroundColor;
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    const highlightColor =
      '#f2c977'; /* http://www.colourlovers.com/color/F2C977/Honey_Mustard */

    const connectedComponents = this.props.graph.getConnectedComponents();

    for (let i = 0; i < connectedComponents.length; i++) {
      // setTimeout(_ => {
      const cluster = connectedComponents[i];
      const color = colors[i] || getRandomColor();

      for (let vertex of cluster) {
        for (let edge of vertex.edges) {
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y);
          ctx.strokeStyle =
            highlightCluster.includes(edge.destination) &&
            highlightCluster.includes(vertex)
              ? highlightColor
              : color;
          ctx.stroke();

          const averagePosX = (vertex.pos.x + edge.destination.pos.x) / 2;
          const averagePosY = (vertex.pos.y + edge.destination.pos.y) / 2;

          const weightWidth = vertexRadius * 1.2;
          const weightHeight = vertexRadius * 1.2;
          ctx.fillStyle = backgroundColor;
          ctx.fillRect(
            averagePosX - weightWidth / 2,
            averagePosY - weightHeight / 2,
            weightWidth,
            weightHeight,
          );

          ctx.fillStyle = 'black';
          ctx.font = `${vertexRadius}px ${font}`;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(edge.weight, averagePosX, averagePosY);
        }
      }

      for (let vertex of cluster) {
        const posX = vertex.pos.x;
        const posY = vertex.pos.y;

        ctx.beginPath();
        ctx.arc(posX, posY, vertexRadius, 0, 2 * Math.PI);
        ctx.strokeStyle = highlightCluster.includes(vertex)
          ? highlightColor
          : color;
        ctx.stroke();
        ctx.fillStyle = highlightCluster.includes(vertex)
          ? highlightColor
          : color;
        ctx.fill();

        ctx.fillStyle = fontColor;
        ctx.font = `${vertexRadius}px ${font}`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vertex.value, posX, posY);
      }
      // }, delay * (i + 1));
    }
  }

  canvasClickedHandler = e => {
    const offset = (window.innerWidth - canvasWidth) / 2;

    const pointX = e.clientX - offset;
    const pointY = e.clientY;

    for (let vertex of this.props.graph.vertexes) {
      const posX = vertex.pos.x;
      const posY = vertex.pos.y;

      const sqDist = (pointX - posX) ** 2 + (pointY - posY) ** 2;
      const sqRad = vertexRadius ** 2;

      if (sqDist <= sqRad) {
        if (this.state.vS === null) {
          this.setState({ vS: vertex });
        } else if (this.state.vT === null) {
          this.setState({ vT: vertex });
        } else {
          /* for unexpected errors */
          console.error(
            'vS and vT not null (check GraphView state reset func)',
          );
        }
      }
    }
  };

  findShortestPath = _ => {
    /* check if v_target is in same connected component as v_source */
    const cluster = this.props.graph
      .getConnectedComponents()
      .find(cl => cl.includes(this.state.vS));

    if (cluster.find(v => v === this.state.vT) === undefined) {
      // convert to React comp
      window.alert(
        `target vertex (${this.state.vT.value}) not found in source vertex (${
          this.state.vS.value
        }) cluster`,
      );
      this.updateCanvas();
    } else if (this.state.vS === this.state.vT) {
      window.alert(
        `target and source vertex are the same (${this.state.vT.value})`,
      );
      this.updateCanvas();
    } else {
      const shortestPath = this.dijkstra(cluster);
      this.updateCanvas(shortestPath);
    }

    /* reset after finding shortest path */
    this.setState({ vS: null, vT: null });
  };

  dijkstra = graph => {
    /* got a lot of help from https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e */

    const q = [];
    let qVisited = 0;

    for (let v of graph) {
      const d = {
        vertex: v,
        shortestDist: v === this.state.vS ? 0 : 1000000 /* 1 million */,
        previousVertex: null,
        visited: false,
      };

      q.push(d);
    }

    while (qVisited < q.length) {
      let currentV;

      /* find vertex with smallest known cost/distance */
      for (let v of q) {
        if (!currentV && v.visited === false) currentV = v;
        else if (currentV) {
          if (v.shortestDist < currentV.shortestDist && v.visited === false) {
            currentV = v;
          }
        }
      }

      currentV.visited = true;

      /* calc edge weights of current vertex edges that are unvisited */
      for (let edge of currentV.vertex.edges) {
        const edgeDestination = edge.destination;
        const edgeWeight = edge.weight;

        const qTblVert = q.find(el => el.vertex === edgeDestination);

        /* check if current vertex + edge weight is smaller than current shortest dist in q
           only if neighbor is not visited
         */
        if (
          currentV.shortestDist + edgeWeight < qTblVert.shortestDist &&
          qTblVert.visited === false
        ) {
          qTblVert.shortestDist = currentV.shortestDist + edgeWeight;
          qTblVert.previousVertex = currentV.vertex;
        }
      }

      qVisited++;
    }

    const shortestPath = [];
    let vertexToPush = this.state.vT;

    while (1) {
      shortestPath.unshift(vertexToPush);

      // eslint-disable-next-line
      const qTblRow = q.find(r => r.vertex === vertexToPush);
      if (qTblRow.previousVertex === null) break;
      vertexToPush = qTblRow.previousVertex;
    }

    return shortestPath;
  };

  /**
   * Render
   */
  render() {
    return (
      <canvas
        ref="canvas"
        width={canvasWidth}
        height={canvasHeight}
        onClick={e => this.canvasClickedHandler(e)}
      />
    );
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph(),
    };

    this.state.graph.randomize(width, height, jitter, prob);
  }

  reloadButtonClicked = _ => {
    this.setState({ graph: new Graph() });
  };

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />

        <ReloadButton reloadButtonClicked={this.reloadButtonClicked} />
      </div>
    );
  }
}

export default App;
