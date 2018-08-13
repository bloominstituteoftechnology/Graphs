import React from 'react';
import { Graph } from './graph';
import View from './View';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      graph: new Graph(),
      pxBox: 100,
      amount: 10,
      size: 25,
    };

    this.canvasHeight = null;
    this.canvasWidth = null;

    this.randomize();
  }

  regenerate = () => {
    this.refs.regen.style.background = "white";
    this.state.graph.refresh();
    this.randomize();
    this.forceUpdate();
  }

  randomize = () => {
    this.canvasHeight = Math.floor(window.innerHeight * 0.9);
    this.canvasWidth = Math.floor(this.canvasHeight * 1.2);

    const w = this.canvasWidth / 1000;
    const h = this.canvasHeight / 1000;

    const gridHeight = Math.floor(this.state.amount*h);
    const gridWidth = Math.floor(this.state.amount*w);

    this.state.graph.randomize(gridWidth, gridHeight, this.state.pxBox, 0.5);
  }

  adjust = (e) => {
    const slider = e.target.name;
    this.setState({[slider]: e.target.value}, () => {
      if(slider !== "size") {
        this.refs.regen.style.background = "#FFAAAA";
      }
    });
  }

  render() {
    return (
      <div className="App">
        <View canvasHeight={this.canvasHeight} canvasWidth={this.canvasWidth} graph={this.state.graph} vertexRadius={this.state.size}></View>
        <div className="controls">
          <button ref="regen" onClick={() => {
              this.regenerate();
              }}>Regenerate</button>
          <label>Spread: {this.state.pxBox}</label>
          <input type="range" min="60" max="150" value={this.state.pxBox} onChange={this.adjust} className="slider" name="pxBox"/>
          <label>Amount: {this.state.amount}</label>
          <input type="range" min="1" max="20" value={this.state.amount} onChange={this.adjust} className="slider" name="amount"/>
          <label>Size: {this.state.size}</label>
          <input type="range" min="10" max="40" value={this.state.size} onChange={this.adjust} className="slider" name="size"/>
        </div>
      </div>
    );

  }
}

export default App;
