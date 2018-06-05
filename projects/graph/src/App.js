import React, { Component } from 'react';
import { Graph } from './graph';
import './App.css';

// !!! IMPLEMENT ME
const canvasWidth = 375;
const canvasHeight = 667;

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
    
    // Sky
    ctx.fillStyle = '#ff9246';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    //sun colors
    ctx.fillStyle = '#eb5b0c';
    ctx.fillRect(0, 0, canvasWidth, 60);
    ctx.fillRect(220, 40, 600, 5);
    // ctx.fillRect(0, 50, 600, 10);
    // ctx.fillRect(0, 60, 600, 10);
    
    ctx.fillStyle = '#ff7c31';
    ctx.fillRect(0, 50, canvasWidth, 50);
    ctx.fillRect(0, 100, 95, 5);
    ctx.fillRect(0, 105, 90, 5);
    ctx.fillRect(0, 110, 75, 5);
    ctx.fillRect(0, 115, 55, 5);
    ctx.fillRect(0, 125, 65, 5);
    ctx.fillRect(0, 130, 80, 5);
    ctx.fillRect(340, 110, 55, 5);
    ctx.fillRect(310, 105, 100, 5);
    ctx.fillRect(280, 100, 100, 5);
    ctx.fillRect(335, 125, 155, 5);
    ctx.fillRect(315, 130, 155, 5);
    ctx.fillRect(0, 200, canvasWidth, 50);
    ctx.fillRect(0, 195, 105, 5);
    ctx.fillRect(45, 190, 35, 5);
    ctx.fillRect(245, 190, 55, 5);
    ctx.fillRect(245, 195, 35, 5);

    ctx.fillStyle = '#ff6c21';
    // ctx.fillRect(0, 200, 600, 60);
    ctx.fillRect(0, 25, 400, 35);
    ctx.fillRect(25, 60, 400, 5)
    ctx.fillRect(355, 65, 25, 5)
    ctx.fillRect(0, 220, canvasWidth, 35);
    ctx.fillRect(100, 215, 150, 5);

    ctx.fillStyle = '#eb5b0c';
    ctx.fillRect(240, 45, 600, 5);
    ctx.fillRect(300, 50, 600, 5);
    ctx.fillRect(0, 45, 100, 5);
    ctx.fillRect(0, 50, 120, 5);
    ctx.fillRect(0, 250, canvasWidth, 55);
    ctx.fillRect(0, 240, 25, 5);
    ctx.fillRect(0, 245, 75, 5);
    ctx.fillRect(260, 245, 175, 5);

    //darkest color in sky
    ctx.fillStyle = '#ca3d00';
    ctx.fillRect(0, 10, 120, 5);
    ctx.fillRect(0, 15, 130, 5);
    ctx.fillRect(0, 20, 70, 5);
    ctx.fillRect(0, 5, 40, 5);
    ctx.fillRect(105, 0, 120, 5);
    ctx.fillRect(185, 5, 60, 5);
    ctx.fillRect(260, 15, 150, 5);
    ctx.fillRect(240, 20, 150, 5);
    ctx.fillRect(290, 25, 150, 5);

    //sun
    ctx.beginPath();
    ctx.strokeStyle = '#ffbf56';
    ctx.lineWidth=1;
    ctx.arc((375/2), 130, 90, 0, 2 * Math.PI);
    ctx.fillStyle = '#ffbf56';
    ctx.stroke();
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = '#ffdc67';
    ctx.strokeStyle = '#ffdc67';
    ctx.lineWidth=1;
    ctx.arc((375/2), 130, 70, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
    
    ctx.beginPath();
    ctx.fillStyle = '#fff89a';
    ctx.strokeStyle = '#fff89a';
    ctx.lineWidth=1;
    ctx.arc((375/2), 130, 50, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();

    //ground
    ctx.fillStyle = '#510000';
    ctx.fillRect(0, 300, canvasWidth, 400);

    ctx.fillStyle = '#430000';  
    //left side 
    ctx.fillRect(0, 310, 100, 5);
    ctx.fillRect(0, 325, 120, 5);
    ctx.fillRect(0, 330, 110, 5);
    ctx.fillRect(0, 340, 100, 5);
    ctx.fillRect(0, 350, 120, 5);
    ctx.fillRect(0, 365, 110, 5);
    ctx.fillRect(0, 380, 140, 5);
    ctx.fillRect(0, 390, 110, 5);
    ctx.fillRect(0, 405, 100, 5);
    ctx.fillRect(0, 415, 50, 5);
    ctx.fillRect(0, 435, 100, 5);
    ctx.fillRect(0, 445, 130, 5);
    ctx.fillRect(0, 460, 110, 5);
    ctx.fillRect(0, 480, 10, 5);
    ctx.fillRect(0, 510, 160, 5);
    ctx.fillRect(0, 525, 180, 5);
    ctx.fillRect(0, 555, 160, 5);
    ctx.fillRect(0, 550, 110, 5);
    ctx.fillRect(0, 545, 80, 5);
    
    //right ride
    ctx.fillRect(300, 310, 100, 5);
    ctx.fillRect(310, 325, 120, 5);
    ctx.fillRect(290, 340, 200, 5);
    ctx.fillRect(270, 350, 220, 5);
    ctx.fillRect(250, 365, 220, 5);
    ctx.fillRect(280, 380, 240, 5);
    ctx.fillRect(270, 390, 220, 5);
    ctx.fillRect(290, 405, 200, 5);
    ctx.fillRect(300, 415, 250, 5);
    ctx.fillRect(280, 435, 200, 5);
    ctx.fillRect(300, 445, 230, 5);
    ctx.fillRect(320, 460, 220, 5);
    ctx.fillRect(290, 480, 220, 5);
    ctx.fillRect(250, 510, 260, 5);
    ctx.fillRect(220, 525, 280, 5);
    ctx.fillRect(250, 555, 260, 5);
    ctx.fillRect(340, 550, 210, 5);
    ctx.fillRect(350, 545, 280, 5);

    ctx.fillRect(0, 560, canvasWidth, 500);

    //shadow
    ctx.fillStyle = '#320000';
    //neck
    ctx.fillRect(190, 330, 10, 60);
    //head
    ctx.fillRect(185, 380, 15, 15);
    //body
    ctx.fillRect(185, 330, 17, 45);
    ctx.fillRect(185, 355, 20, 20);
    ctx.fillRect(185, 330, 20, 15);
    //left leg
    ctx.fillRect(180, 325, 10, 15);
    ctx.fillRect(175, 315, 10, 15);
    ctx.fillRect(170, 310, 7, 10);
    ctx.fillRect(169, 300, 5, 20);
    //right leg
    ctx.fillRect(200, 325, 10, 15);
    ctx.fillRect(205, 315, 10, 15);
    ctx.fillRect(210, 310, 7, 10);
    ctx.fillRect(213, 300, 5, 20);
    //left arm
    ctx.fillRect(180, 365, 15, 5);
    ctx.fillRect(180, 360, 15, 5);
    ctx.fillRect(175, 355, 5, 5);
    ctx.fillRect(170, 355, 5, 5);
    ctx.fillRect(165, 360, 5, 5);
    ctx.fillRect(160, 365, 5, 5);
    //right arm
    ctx.fillRect(195, 365, 15, 5);
    ctx.fillRect(195, 360, 15, 5);
    ctx.fillRect(195, 370, 15, 5);
    
    ctx.fillStyle = '#510000';
    //neck
    ctx.fillRect(190, 200, 10, 60);
    //head
    ctx.fillRect(185, 195, 15, 15);
    //body
    ctx.fillRect(185, 220, 17, 45);
    ctx.fillRect(185, 215, 20, 20);
    ctx.fillRect(185, 245, 20, 15);
    //left leg
    ctx.fillRect(180, 260, 10, 15);
    ctx.fillRect(175, 270, 10, 15);
    ctx.fillRect(170, 280, 7, 10);
    ctx.fillRect(169, 280, 5, 20);
    //right leg
    ctx.fillRect(200, 260, 10, 15);
    ctx.fillRect(205, 270, 10, 15);
    ctx.fillRect(210, 280, 7, 10);
    ctx.fillRect(213, 280, 5, 20);
    //left arm
    ctx.fillRect(180, 220, 15, 5);
    ctx.fillRect(180, 225, 15, 5);
    ctx.fillRect(175, 230, 5, 5);
    ctx.fillRect(170, 230, 5, 5);
    ctx.fillRect(165, 225, 5, 5);
    ctx.fillRect(160, 220, 5, 5);
    //right arm
    ctx.fillRect(195, 220, 15, 5);
    ctx.fillRect(195, 225, 15, 5);
    ctx.fillRect(195, 230, 15, 5);

    // clouds
    ctx.fillStyle = '#ffbf56';
    ctx.fillRect(0, 160, 140, 5);
    ctx.fillRect(0, 165, 170, 5);
    

    ctx.fillStyle = '#ffbf56';
    ctx.fillRect(215, 140, 1000, 5);
    ctx.fillRect(195, 145, 1000, 5);
    ctx.fillRect(230, 150, 1000, 5);
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
