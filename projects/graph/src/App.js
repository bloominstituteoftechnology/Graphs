//@ts-check */
import React, { Component } from 'react'
import { Graph, Vertex } from './graph'
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

    // !!! IMPLEMENT ME
    // compute connected components
    const generateCircle = generateCirclefromCanvasContextFunction(ctx)

    /**
     * @type {Graph}
     */
    const GraphInstance = this.props.graph

    const connectedComponents = GraphInstance.getConnectedComponents()
    console.log(connectedComponents)
    connectedComponents.map(
      /**
       * @param {Vertex[]} vertices
       */
      vertices => {
        // draw edges
        // draw verts
        vertices.map(vertex => {
          generateCircle(vertex.pos.x, vertex.pos.y)
        })
        // draw vert values (labels)
      }
    )
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
 * Curry function that returns a function
 * that will create a circle. Useful for composing.
 * @param {CanvasRenderingContext2D} ctx
 */
const generateCirclefromCanvasContextFunction = ctx =>
  /**
   * @param {number} posX Location on canvas for X axis.
   * @param {number} posY Location on canvas for Y axis.
   * @param {number=} radius Radius of circle. Defaults to `20`.
   * @param {number=} startAngle Degrees at which to start drawing the circle.
   * Defaults to `0`.
   * @param {number=} endAngle Degrees at which to end drawing the circle.
   * Defaults to `Math.Pi * 2`
   */
  (posX, posY, radius = 20, startAngle = 0, endAngle = Math.PI * 2) => {
    ctx.beginPath()
    ctx.arc(posX, posY, radius, startAngle, endAngle)
    ctx.stroke()
  }
