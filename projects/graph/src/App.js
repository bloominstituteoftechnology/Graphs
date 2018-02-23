import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 750;
const canvasHeight = 600;
const lineWidth = 2;
const radius = 15;
const boxSize = canvasHeight / 4;
const randomProbability = 0.6;
Math.toDegrees = function () {
  if (arguments.length !== 1) return 0;
  return arguments[0] * 180 / Math.beginPath;
}
/*
function relMouseCoords(event) {
  var totalOffsetX = 0;
  var totalOffsetY = 0;
  var canvasX = 0;
  var canvasY = 0;
  var currentElement = this;

  do {
    totalOffsetX += currentElement.offsetLeft - currentElement.scrollLeft;
    totalOffsetY += currentElement.offsetTop - currentElement.scrollTop;
  }
  while (currentElement = currentElement.offsetParent)

  canvasX = event.pageX - totalOffsetX;
  canvasY = event.pageY - totalOffsetY;

  return { x: canvasX, y: canvasY }
}
HTMLCanvasElement.prototype.relMouseCoords = relMouseCoords;
*/
/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvas();
    //  console.log(`componentDidMount`);
    this.props.update(this.runBfs);
    this.runBfs();
  }
  runBfs = () => {
    // console.log(`calling runBfs`);
    this.props.graph.bfs(this.props.graph.vertexes[0], () => this.updateCanvas())
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvas();
  }
  drawArrow(ctx, fromx, fromy, tox, toy, lineWidth = ctx.lineWidth) {
    //variables to be used when creating the arrow

    // var headlen = 10;

    // var angle = Math.atan2(toy-fromy,tox-fromx);

    //starting path of the arrow from the start square to the end square and drawing the stroke
    ctx.lineWidth = lineWidth;
    ctx.beginPath();
    ctx.moveTo(fromx, fromy);
    ctx.lineTo(tox, toy);
    ctx.fill();
    ctx.stroke();
    ctx.closePath();


    // //starting a new path from the head of the arrow to one of the sides of the point
    // ctx.beginPath();
    // ctx.moveTo(tox, toy);
    // ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),toy-headlen*Math.sin(angle-Math.PI/7));

    // //path from the side point of the arrow, to the other side point
    // ctx.lineTo(tox-headlen*Math.cos(angle+Math.PI/7),toy-headlen*Math.sin(angle+Math.PI/7));

    // //path from the side point back to the tip of the arrow, and then again to the opposite side point
    // ctx.lineTo(tox, toy);
    // ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),toy-headlen*Math.sin(angle-Math.PI/7));

    // //draws the paths created above

    // ctx.stroke();


  }
  angleOf(p1, p2) {
    // NOTE: Remember that most math has the Y axis as positive above the X.
    // However, for screens we have Y as positive below. For this reason, 
    // the Y values are inverted to get the expected results.
    const deltaY = (p1.y - p2.y);
    const deltaX = (p2.x - p1.x);
    const result = Math.atan2(deltaY, deltaX) + Math.PI / 2;
    return (result < 0) ? (2 * Math.PI + result) : result;
  }
  // rxy(dx, dy) {
  //   let rx, ry;
  //   if (dy === 0) {
  //     rx = rx > 0 ? 1 : -1;
  //     ry = 0;
  //   }
  //   else if (dy === 0) {
  //     rx = 0;
  //     ry = ry > 0 ? 1 : -1;
  //   } else {
  //     rx = dx / dy;
  //     ry = 1 / rx;
  //   }
  //   return [rx, ry]
  // }
  // rx = deltax/deltay  r^^2 + (1/r) ^^2 = radius ^^ 2
  // pow(a,2) + pow(1/a, 2) =  pow(c,2)
  //pow(a,2) x (1 + pow(1/a, 4))
  // (1 + pow(1/a,4)) = pow(1/a,2)
  // 1 + 2(pow(1/a,4)) + pow(1/a,2) = pow(1/a,4)
  // 1 + pow(1/a,4) + pos(1/a,2) = 0
  // pow(a,4) + 1 =  pow(a,2)
  drawEdges(ctx) {
    ctx.lineWidth = lineWidth;
    // let edges = 0;
    this.props.graph.vertexes.forEach(v => {
      v.edges.forEach(e => {
        if (e.isVisible) {
          const angle = this.angleOf(v.pos, e.destination.pos);
          let rx = radius * Math.sin(angle), ry = radius * Math.cos(angle);
          ctx.strokeStyle = e.color;
          this.drawArrow(ctx, v.pos.x + rx, v.pos.y + ry, e.destination.pos.x - rx, e.destination.pos.y - ry);
          ctx.beginPath();
          ctx.save();
          ctx.translate(v.pos.x + (e.destination.pos.x - v.pos.x) / 2 - 7, v.pos.y + (e.destination.pos.y - v.pos.y) / 2);
          ctx.rotate(angle > Math.PI ? angle - 0 : angle);
          ctx.textAlign = "center";
          ctx.font = '34px serif';
          ctx.fillStyle = "black"
          ctx.fillText(e.weight.toString(), 10, 10);
          ctx.restore();
          // edges++;
        }
      })
    });
    // console.log(`drawEdges edges: ${edges}`);
  }
  drawVerts(ctx) {
    ctx.fillStyle = "brown";
    ctx.strokeStyle = "blue"
    this.props.graph.vertexes.forEach(v => {
      // if (v.isBlack)
      //   console.log(`v.value: ${v.value} back color: ${v.color[0].toString(16)}  forcolor: ${v.color[1].toString(16)} `);
      ctx.beginPath();
      ctx.fillStyle = v.color[0];
      ctx.arc(v.pos.x, v.pos.y, radius, 0, 2 * Math.PI);
      ctx.fill();

      ctx.font = '24px serif';
      ctx.strokeStyle = v.color[1];
      ctx.strokeText(v.value.substring(1), v.pos.x - radius / 2, v.pos.y + radius / 2, radius);
      ctx.stroke();

      ctx.closePath();
      // v.edges.forEach(e => {

      //   // ctx.beginPath();
      //   // ctx.moveTo(v.pos.x, v.pos.y);
      //   // ctx.closePath();        
      //   // ctx.fill();          
      // })
    })
  }
  /*
ctx.beginPath();
ctx.fillStyle = "yellow"

ctx.arc(50, 50, 50, 0, 2 * Math.PI, false);
ctx.stroke();
ctx.fill()
  */
  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas;
    canvas.addEventListener('click', this.getRelativeCoords, false);
    let ctx = canvas.getContext('2d');

    // Clear it
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
    this.drawEdges(ctx);
    this.drawVerts(ctx);
    // draw vert values (labels)
  }
  getRelativeCoords = (event) => {
    // return { x: event.offsetX, y: event.offsetY };

    const x = event.offsetX;
    const y = event.offsetY;
    //console.log(`x: ${x} y: ${y}`);
    const vertexes = this.props.graph.vertexes.filter(v => (x > v.pos.x - radius) && (x < v.pos.x + radius) &&
      (y > v.pos.y - radius) && (y < v.pos.y + radius));
    if (vertexes.length > 0) {
      const v = vertexes[0];
      console.log(`you clicked vertex ${v.value}`);
    }

  }
  // /**
  //  * Render
  //  */
  render() {
    return (
      <div>
      <canvas ref="canvas" width={canvasWidth} height={canvasHeight}></canvas>
      </div>
    );
  }
}
/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props);
    // console.log(`in App constuctor `);
    this.state = {
      graph: new Graph(this.bsfIterateUpdate)
    };
    this.state.graph.randomize(5, 4, boxSize, randomProbability);
    this.updateCanvas = null;
  }

  setupUpdate = (f) => {
    this.updateCanvas = f;
  }
  bsfIterateUpdate = () => {
    this.updateCanvas();
  }
  render() {
    return (
      <form className="App" onSubmit={() => {

      }}  >
        <GraphView graph={this.state.graph} update={this.setupUpdate}></GraphView>
        <button type="button" onClick={this.bsfIterateUpdate}>Rerun BFS of Graph</button>
        <input type="submit" value="New Graph" />
      </form>
    );
  }
}

export default App;
