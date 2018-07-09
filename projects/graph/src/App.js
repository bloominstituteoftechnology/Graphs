 import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 600;
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
    const canvas = this.refs.canvas;
    const ctx = canvas.getContext('2d');
    
    // Clear it
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    ctx.fillStyle = 'red'; // HAT 1
    ctx.fillRect(200, 10, 20, 20);

    ctx.fillStyle = 'red'; //2
    ctx.fillRect(222, 10, 20, 20);

    ctx.fillStyle = 'red'; //3
    ctx.fillRect(244, 10, 20, 20);

    ctx.fillStyle = 'red'; //4
    ctx.fillRect(266, 10, 20, 20);

    ctx.fillStyle = 'red'; //5
    ctx.fillRect(288, 10, 20, 20);

    //2nd row
    ctx.fillStyle = 'red'; // HAT 1
    ctx.fillRect(178, 32, 20, 20);

    ctx.fillStyle = 'red'; //2
    ctx.fillRect(200, 32, 20, 20);

    ctx.fillStyle = 'red'; //3
    ctx.fillRect(222, 32, 20, 20);

    ctx.fillStyle = 'red'; //4
    ctx.fillRect(244, 32, 20, 20);

    ctx.fillStyle = 'red'; //5
    ctx.fillRect(266, 32, 20, 20);

    ctx.fillStyle = 'red'; //6
    ctx.fillRect(288, 32, 20, 20);

    ctx.fillStyle = 'red'; //7
    ctx.fillRect(310, 32, 20, 20);

    ctx.fillStyle = 'red'; //8
    ctx.fillRect(332, 32, 20, 20);

    ctx.fillStyle = 'red'; //9
    ctx.fillRect(354, 32, 20, 20);

    //3rd row
    ctx.fillStyle = '#663300'; // HAIR brown 1
    ctx.fillRect(178, 54, 20, 20);

    ctx.fillStyle = '#663300'; //2
    ctx.fillRect(200, 54, 20, 20);

    ctx.fillStyle = '#663300'; //3
    ctx.fillRect(222, 54, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 4
    ctx.fillRect(244, 54, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 5
    ctx.fillRect(266, 54, 20, 20);

    ctx.fillStyle = '#663300'; // EYE 6
    ctx.fillRect(288, 54, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 7
    ctx.fillRect(310, 54, 20, 20);

    //4th row
    ctx.fillStyle = '#663300'; // HAIR brown 1
    ctx.fillRect(156, 76, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 2
    ctx.fillRect(178, 76, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 3
    ctx.fillRect(200, 76, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 4
    ctx.fillRect(222, 76, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 5
    ctx.fillRect(244, 76, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 6
    ctx.fillRect(266, 76, 20, 20);

    ctx.fillStyle = '#663300'; // EYE 7
    ctx.fillRect(288, 76, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 8
    ctx.fillRect(310, 76, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 9
    ctx.fillRect(332, 76, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 10
    ctx.fillRect(354, 76, 20, 20);

    //5th row
    ctx.fillStyle = '#663300'; // HAIR brown 1
    ctx.fillRect(156, 98, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 2
    ctx.fillRect(178, 98, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 3
    ctx.fillRect(200, 98, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 4
    ctx.fillRect(222, 98, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 5
    ctx.fillRect(244, 98, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 6
    ctx.fillRect(266, 98, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 7
    ctx.fillRect(288, 98, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 8
    ctx.fillRect(310, 98, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 9
    ctx.fillRect(332, 98, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 10
    ctx.fillRect(354, 98, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 11
    ctx.fillRect(376, 98, 20, 20);

    //6th row
    ctx.fillStyle = '#663300'; // HAIR brown 1
    ctx.fillRect(156, 120, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 2
    ctx.fillRect(178, 120, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 3
    ctx.fillRect(200, 120, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 4
    ctx.fillRect(222, 120, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 5
    ctx.fillRect(244, 120, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 6
    ctx.fillRect(266, 120, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 7
    ctx.fillRect(288, 120, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 8
    ctx.fillRect(310, 120, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 9
    ctx.fillRect(354, 120, 20, 20);

    ctx.fillStyle = '#663300'; // HAIR 10
    ctx.fillRect(332, 120, 20, 20);

    //7th row
    ctx.fillStyle = '#ffcc99'; // SKIN 1
    ctx.fillRect(200, 142, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 2
    ctx.fillRect(222, 142, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 3
    ctx.fillRect(244, 142, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 4
    ctx.fillRect(266, 142, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 5
    ctx.fillRect(288, 142, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 6
    ctx.fillRect(310, 142, 20, 20);

    ctx.fillStyle = '#ffcc99'; // SKIN 7
    ctx.fillRect(332, 142, 20, 20);

    //8th row
    ctx.fillStyle = 'red'; // SHIRT 1
    ctx.fillRect(178, 164, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 2
    ctx.fillRect(200, 164, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 3
    ctx.fillRect(222, 164, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 4
    ctx.fillRect(244, 164, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 5
    ctx.fillRect(266, 164, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 6
    ctx.fillRect(288, 164, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 7
    ctx.fillRect(310, 164, 20, 20);

    //9th row
    ctx.fillStyle = 'red'; // SHIRT 1
    ctx.fillRect(156, 186, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 2
    ctx.fillRect(178, 186, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 3
    ctx.fillRect(200, 186, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 4
    ctx.fillRect(222, 186, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 5
    ctx.fillRect(244, 186, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 6
    ctx.fillRect(266, 186, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 7
    ctx.fillRect(288, 186, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 8
    ctx.fillRect(310, 186, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 9
    ctx.fillRect(332, 186, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 10
    ctx.fillRect(354, 186, 20, 20);

    //10th row
    ctx.fillStyle = 'red'; // SHIRT 1
    ctx.fillRect(134, 208, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 2
    ctx.fillRect(156, 208, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 3
    ctx.fillRect(178, 208, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 4
    ctx.fillRect(200, 208, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 5
    ctx.fillRect(222, 208, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 6
    ctx.fillRect(244, 208, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 7
    ctx.fillRect(266, 208, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 8
    ctx.fillRect(288, 208, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 9
    ctx.fillRect(310, 208, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 10
    ctx.fillRect(332, 208, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 11
    ctx.fillRect(354, 208, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 12
    ctx.fillRect(376, 208, 20, 20);

    //11th row
    ctx.fillStyle = 'white'; // GLOVE 1
    ctx.fillRect(134, 230, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 2
    ctx.fillRect(156, 230, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 3
    ctx.fillRect(178, 230, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 4
    ctx.fillRect(200, 230, 20, 20);

    ctx.fillStyle = 'yellow'; // SHIRT 5
    ctx.fillRect(222, 230, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 6
    ctx.fillRect(244, 230, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 7
    ctx.fillRect(266, 230, 20, 20);

    ctx.fillStyle = 'yellow'; // SHIRT 8
    ctx.fillRect(288, 230, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 9
    ctx.fillRect(310, 230, 20, 20);

    ctx.fillStyle = 'red'; // SHIRT 10
    ctx.fillRect(332, 230, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 10
    ctx.fillRect(354, 230, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 11
    ctx.fillRect(376, 230, 20, 20);

    //12th row
    ctx.fillStyle = 'white'; // GLOVE 1
    ctx.fillRect(134, 252, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 2
    ctx.fillRect(156, 252, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 3
    ctx.fillRect(178, 252, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 4
    ctx.fillRect(200, 252, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 5
    ctx.fillRect(222, 252, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 6
    ctx.fillRect(244, 252, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 7
    ctx.fillRect(266, 252, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 8
    ctx.fillRect(288, 252, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 9
    ctx.fillRect(310, 252, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 10
    ctx.fillRect(332, 252, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 11
    ctx.fillRect(354, 252, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 12
    ctx.fillRect(376, 252, 20, 20);

    //13th row
    ctx.fillStyle = 'white'; // GLOVE 1
    ctx.fillRect(134, 274, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 2
    ctx.fillRect(156, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 3
    ctx.fillRect(178, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 4
    ctx.fillRect(200, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 5
    ctx.fillRect(222, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 6
    ctx.fillRect(244, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 7
    ctx.fillRect(266, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 8
    ctx.fillRect(288, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 9
    ctx.fillRect(310, 274, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 10
    ctx.fillRect(332, 274, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 11
    ctx.fillRect(354, 274, 20, 20);

    ctx.fillStyle = 'white'; // GLOVE 12
    ctx.fillRect(376, 274, 20, 20);

    //14th row
    ctx.fillStyle = 'blue'; // SHIRT 1
    ctx.fillRect(178, 296, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 2
    ctx.fillRect(200, 296, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 3
    ctx.fillRect(222, 296, 20, 20);

    ctx.fillStyle = 'black'; // SHIRT 4
    ctx.fillRect(244, 296, 20, 20);

    ctx.fillStyle = 'black'; // SHIRT 5
    ctx.fillRect(266, 296, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 6
    ctx.fillRect(288, 296, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 7
    ctx.fillRect(310, 296, 20, 20);

    ctx.fillStyle = 'blue'; // SHIRT 8
    ctx.fillRect(332, 296, 20, 20);

    //15th row
    ctx.fillStyle = '#663300'; // SHOES 1
    ctx.fillRect(156, 318, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 2
    ctx.fillRect(178, 318, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 3
    ctx.fillRect(200, 318, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 4
    ctx.fillRect(222, 318, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 5
    ctx.fillRect(244, 318, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 6
    ctx.fillRect(266, 318, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 7
    ctx.fillRect(288, 318, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 8
    ctx.fillRect(310, 318, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 9
    ctx.fillRect(332, 318, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 10
    ctx.fillRect(354, 318, 20, 20);

    //16th row
    ctx.fillStyle = '#663300'; // SHOES 1
    ctx.fillRect(134, 340, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 2
    ctx.fillRect(156, 340, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 3
    ctx.fillRect(178, 340, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 4
    ctx.fillRect(200, 340, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 5
    ctx.fillRect(222, 340, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 6
    ctx.fillRect(244, 340, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 7
    ctx.fillRect(266, 340, 20, 20);

    ctx.fillStyle = 'black'; // SHOES 8
    ctx.fillRect(288, 340, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 9
    ctx.fillRect(310, 340, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 10
    ctx.fillRect(332, 340, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 11
    ctx.fillRect(354, 340, 20, 20);

    ctx.fillStyle = '#663300'; // SHOES 12
    ctx.fillRect(376, 340, 20, 20);

    

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
