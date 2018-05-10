// import React, { Component } from 'react';
// import { Graph } from './graph';
// import './App.css';

// const canvasWidth = 750;
// const canvasHeight = 600;

// /**
//  * GraphView
//  */
// class GraphView extends Component {
//   /**
//    * On mount
//    */
//   componentDidMount() {
//     this.updateCanvas();
//   }

//   /**
//    * On state update
//    */
//   componentDidUpdate() {
//     this.updateCanvas();
//   }

//   /**
//    * Render the canvas
//    */
//   updateCanvas() {
//     let canvas = this.refs.canvas;
//     let ctx = canvas.getContext('2d');

//     var grd = ctx.createLinearGradient(0, 0, canvasWidth, canvasHeight);
//     grd.addColorStop(0, '#ffffff');
//     grd.addColorStop(0.1, '#3c0045');
//     grd.addColorStop(0.2, '#fe008d');
//     grd.addColorStop(0.3, '#ff6a00');
//     grd.addColorStop(0.4, '#fffc00');
//     grd.addColorStop(0.5, '#70ff00');
//     grd.addColorStop(0.6, '#00ff2e');
//     grd.addColorStop(0.7, '#00b7ff');
//     grd.addColorStop(0.8, '#9b0004');
//     grd.addColorStop(0.9, '#cc7274');
//     grd.addColorStop(1, '#ffffff');

//     ctx.fillStyle = grd;
//     ctx.fillRect(0, 0, canvasWidth, canvasHeight);

//     let seen = [];

//     //two edges create conflicting weights being written
//     //
//     function includes(arr,el) {
//       for(let i = 0; i < arr.length; i++) {
//         if(arr[i][0] === el[0] && arr[i][1] === el[1]) return true;
//       }
//       return false;
//     }

//     // Draw Edges
//     for (let i = 0; i < this.props.graph.vertexes.length; i++) {
//       let vertex = this.props.graph.vertexes[i];
//       if (vertex.edges.length) {
//         let edge = vertex.edges[0].destination.position;
//         let midpoint = [(edge.x + vertex.position.x) / 2, (edge.y + vertex.position.y) / 2];
//         if (includes(seen, midpoint) === false) {
//           ctx.beginPath();
//           ctx.moveTo(vertex.position.x, vertex.position.y);
//           ctx.lineTo(edge.x, edge.y);
//           ctx.stroke();
//           //*Broken* Draw Weights
//           let weight = vertex.edges[0].weight;
//           ctx.strokeStyle = 'white';
//           ctx.font = '15px Arial';
//           ctx.fillStyle = 'black';
//           ctx.fillText(weight, (edge.x + vertex.position.x) / 2, (edge.y + vertex.position.y) / 2);
//           seen.push(midpoint);
//           ctx.stroke();
//         }
//       }
//     }

//     console.log("Vertices", this.props.graph.vertexes);

//     // Draw Vertices
//     for (let i = 0; i < this.props.graph.vertexes.length; i++) {
//       let vertex = this.props.graph.vertexes[i];
//       ctx.beginPath();
//       ctx.arc(vertex.position.x, vertex.position.y, 10, 0, 2 * Math.PI);
//       ctx.fillStyle = 'black';
//       ctx.fill();
//       ctx.stroke();
//       ctx.strokeStyle = 'white';
//       ctx.font = '10px Arial';
//       ctx.textAlign = 'center';
//       ctx.textBaseline = 'middle';
//       ctx.fillStyle = 'white';
//       ctx.fillText(vertex.value, vertex.position.x, vertex.position.y);
//       ctx.stroke();
//       ctx.closePath();
//     }
//   }

//   /**
//    * Render
//    */
//   render() {
//     return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />;
//   }
// }

// /**
//  * App
//  */
// class App extends Component {
//   constructor(props) {
//     super(props);

//     this.state = {
//       graph: new Graph(),
//       foundConnections: new Set([]),
//     };

//     // this.state.graph.debugCreateTestData();
//     this.state.graph.randomize(5, 4, 150, 0.6);
//     for(let i = 0; i < this.state.graph.vertexes.length; i++) {
//       if(this.state.graph.vertexes[i].edges.length) {
//         let result = this.state.graph.bfs(this.state.graph.vertexes[i]);
//         this.state.foundConnections.add(result);
//       }
//       else{
//         this.state.foundConnections.add([this.state.graph.vertexes[i]]);
//       }
//     }

//   }

//   refreshPage() {
//     window.location.reload();
//   }

//   render() {
//     let style = {
//       color: 'red',
//       background: 'black',
//       width: 200,
//       height: 50,
//       fontSize: 20,
//     };

//     return (
//       <div className="App">
//         <GraphView graph={this.state.graph} />
//         <div>
//           <button type="button" style={style} onClick={this.refreshPage}>
//             Refresh{' '}
//           </button>
//         </div>
//       </div>
//     );
//   }
// }

// export default App;

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

    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    let colors = ['white', 'red', 'yellow', 'orange', 'green', 'pink', 'blue', 'lightblue', 'lightpink', 'grey'];

    for (let i = 0; i < this.props.foundConnections.length; i++) {
      // console.log('TOTAL CONNECTION: ', this.props.foundConnections[i]);
      for (let j = 0; j < this.props.foundConnections[i].length; j++) {
        if (this.props.foundConnections[i][j].edges.length) {
          // console.log('VERTEX in conditional: ', this.props.foundConnections[i][j]);
          ctx.beginPath();
          ctx.moveTo(this.props.foundConnections[i][j].position.x, this.props.foundConnections[i][j].position.y);
          ctx.lineTo(
            this.props.foundConnections[i][j].edges[0].destination.position.x,
            this.props.foundConnections[i][j].edges[0].destination.position.y
          );
          // console.log(colors[i]);
          ctx.strokeStyle = colors[i];
          ctx.stroke();
          // ctx.closePath();
        }
      }
    }

    // // !!! IMPLEMENT ME
    // compute connected components
    this.props.graph.vertexes.forEach((vert) => {
      vert.edges.forEach((edge) => {
        ctx.moveTo(vert.position.x, vert.position.y);
        ctx.lineTo(edge.destination.position.x, edge.destination.position.y);
        ctx.stroke();
      });
    });

    this.props.graph.vertexes.forEach((vert) => {
      ctx.beginPath();
      ctx.arc(vert.position.x, vert.position.y, 10, 0, 2 * Math.PI);

      ctx.fillStyle = 'white';
      ctx.fill();
      ctx.strokeStyle = 'blue';
      ctx.stroke();

      ctx.fillStyle = 'black';
      ctx.font = '10px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(vert.value, vert.position.x, vert.position.y);
    });
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
      graph: new Graph(),
      foundConnections: [],
    };

    this.state.graph.randomize(5, 4, 150, 0.6);
    for (let i = 0; i < this.state.graph.vertexes.length; i++) {
      if (this.state.graph.vertexes[i].edges.length > 0) {
        let result = this.state.graph.bfs(this.state.graph.vertexes[i]);
        if (result) {
          this.state.foundConnections.push(result);
        }
      } else {
        this.state.foundConnections.push([this.state.graph.vertexes[i]]);
      }
    }
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} foundConnections={this.state.foundConnections} />
      </div>
    );
  }
}

export default App;
