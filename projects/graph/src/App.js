import React, { Component } from 'react'
import { Graph } from './graph'
import './App.css'

// !!! IMPLEMENT ME
const canvasWidth = window.innerWidth
const canvasHeight = window.innerHeight

/**
 * GraphView
 */
class GraphView extends Component {
  /**
   * On mount
   */
  componentDidMount() {
    this.updateCanvas()
  }

  /**
   * On state update
   */
  componentDidUpdate() {
    this.updateCanvas()
  }

  /**
   * Render the canvas
   */
  updateCanvas() {
    let canvas = this.refs.canvas
    let ctx = canvas.getContext('2d')

    // Clear it
    ctx.fillStyle = 'white'
    ctx.fillRect(0, 0, canvasWidth, canvasHeight)

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
    return <canvas ref="canvas" width={canvasWidth} height={canvasHeight} />
  }
}

/**
 * App
 */
class App extends Component {
  constructor(props) {
    super(props)

    this.state = {
      graph: new Graph()
    }

    // !!! IMPLEMENT ME
    // use the graph randomize() method
    this.state.graph.randomize(3, 4, 1)
    this.state.graph.dump()
  }

  render() {
    return (
      <div className="App">
        <GraphView graph={this.state.graph} />
      </div>
    )
  }
}

export default App
