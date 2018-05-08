import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = (window.innerWidth - 25);
const canvasHeight = (window.innerHeight - 25);

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
    ctx.fillStyle =  '#f2f2f2';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    let colors = ['#ff0000',
                '#ffcccc',
                '#4d0000',
                '#ff0080',
                '#39004d',
                '#26004d',
                '#6600cc',
                '#cc99ff',
                '#666699',
                '#0000ff',
                '#00004d',
                '#9999ff',
                '#0099cc',
                '#004d4d',
                '#00cccc',
                '#b3ffff',
                '#133913',
                '#339933',
                '#b3e6b3',
                '#808000',
                '#ffff00',
                '#392613',
                '#bf8040',
                '#e6ccb3',
                '#66ff66',
                '#000000',
                ]
    
    const randomColor = () => {
      let num = Math.floor((Math.random() * 26) + 1);
      return colors[num];
    }

    const midPoint = (x1, y1, x2, y2) => {
      let mx = (x1+x2)/2;
      let my = (y1+y2)/2;
      return [mx, my];
    }
    
    // !!! IMPLEMENT ME
    // compute connected components
    // draw edges
    // draw verts
    // draw vert values (labels)
    let connectedComponents = this.props.graph.getConnectedComponents();
    
    for (let i = 0; i < connectedComponents.length; i++) {
      let verts = connectedComponents[i];
      ctx.fillStyle = randomColor();
      for (let i = 0; i < verts.length; i++) {
        let x = verts[i].pos.x;
        let y = verts[i].pos.y;
        let e = verts[i].edges;
        for (let j = 0; j < e.length; j++) {
          let ex = e[j].destination.pos.x;
          let ey = e[j].destination.pos.y;
          ctx.beginPath();
          ctx.moveTo(x, y);
          ctx.lineTo(ex, ey);
          ctx.stroke();
        }
      }
      ctx.fillStyle = 'black';
      for (let i = 0; i < connectedComponents.length; i++) {
        let verts = connectedComponents[i];
        for (let i = 0; i < verts.length; i++) {
          let x = verts[i].pos.x;
          let y = verts[i].pos.y;
          let e = verts[i].edges;
          for (let j = 0; j < e.length; j++) {
            let ex = e[j].destination.pos.x;
            let ey = e[j].destination.pos.y;
            if (e[j].weight) {
              let mids = midPoint(x, y, ex, ey);
              ctx.font = '15px sans serif';
              ctx.textAlign = 'start';
              ctx.fillText(e[j].weight, mids[0], mids[1]);
            }
          }
        }
      }
      ctx.fillStyle = randomColor();
      for (let i = 0; i < verts.length; i++) {
        let x = verts[i].pos.x;
        let y = verts[i].pos.y;
        ctx.beginPath();
        ctx.arc(x, y, 20, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.fillStyle = 'white';
      for (let i = 0; i < verts.length; i++) {
        let x = verts[i].pos.x;
        let y = verts[i].pos.y;
        ctx.textAlign = 'center';
        ctx.fillText(verts[i].value, x, y);
      }
    }

    // function isIntersect(point, vertex) {
    //   return Math.sqrt((point.x - vertex.x) ** 2 + (point.y - vertex.y) ** 2) < 20;
    // }

    // canvas.addEventListener('click', (e) => {
    //   const pos = {
    //     x: e.clientX,
    //     y: e.clientY
    //   };
    //   verts.forEach(vert => {
    //     if (isIntersect(mousePoint, vert)) {
    //       alert('click on vertex:' + vert.value);
    //     }
    //   })
    // })

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

    this.randomizeGraph = this.randomizeGraph.bind(this);

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(5, 4, 150, 0.6);


    
  }

  randomizeGraph() {
    const newGraph = new Graph();
    newGraph.randomize(5, 4, 150, 0.6);
    this.setState({graph: newGraph});
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph}></GraphView>
        <button onClick={this.randomizeGraph}>Randomize Graph</button>
      </div>
    );
  }
}

export default App;
