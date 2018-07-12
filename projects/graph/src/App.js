//@ts-check */
import React, { Component } from 'react'
import { Graph } from './graph'
import './App.css'

// !!! IMPLEMENT ME
const canvasWidth = 750
const canvasHeight = 600

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
    /**
     * @type {HTMLCanvasElement} canvas
     */
    //@ts-ignore
    let canvas = this.refs.canvas
    let ctx = canvas.getContext('2d')

    // Clear it
    ctx.fillStyle = 'white'
    ctx.fillRect(0, 0, canvasWidth, canvasHeight)

    generateCirclefromCanvasContext(ctx)
    // !!! IMPLEMENT ME
    // compute connected components
    const connectedComponents = this.props.graph.getConnectedComponents()
    console.log(connectedComponents)
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
    this.state.graph.randomize(5, 4, 150)
    //this.state.graph.dump()
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

/**
 *
 * @param {CanvasRenderingContext2D} ctx
 */
function generateCirclefromCanvasContext(ctx) {
  ctx.arc(10, 10, 10, 0, 2 * Math.PI)
  ctx.stroke()
  ctx.beginPath()
  ctx.arc(100, 100, 10, 0, 2 * Math.PI)
  ctx.stroke()
}
