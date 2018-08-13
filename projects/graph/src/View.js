import React from 'react';

class View extends React.Component {
    constructor(props) {
      super(props);
      this.drag = null;
      this.startX = null;
      this.startY = null;
      this.boundingBox = null;
      this.offsetX = null;
      this.offsetY = null;
  
      this.selected = [];
      this.path = [];
  
      this.canvas = null;
      this.ctx = null;
  
      this.scale = window.devicePixelRatio;
    }
  
    /**
     * On mount
     */
    componentDidMount() {
      this.setRelMouseCoord();
      this.createCanvas();
  
      // console.log('canvHeigh: ',this.canvasHeight);
      this.canvas.style.width = this.props.canvasWidth + 'px';
      this.canvas.style.height = this.props.canvasHeight + 'px';
  
      this.canvas.width = this.props.canvasWidth * this.scale;
      this.canvas.height = this.props.canvasHeight * this.scale;
  
      this.ctx.scale(this.scale, this.scale);
  
      this.setListeners();
      this.setBoundingBox();
      this.clearCanvas();
      this.updateCanvas();
  
  
    }
  
    /**
     * On state update
     */
    componentDidUpdate() {
      this.clearCanvas();
      this.clearSelected();
      this.updateCanvas();
    }
  
    createCanvas = () => {
      this.canvas = this.refs.canvas;
      this.ctx = this.canvas.getContext('2d');
    }
  
    setListeners = () => {
      this.canvas.onmousedown = this.mouseDown;
      this.canvas.onmouseup = this.mouseUp;
      this.canvas.onmousemove = this.mouseMove;
    }
  
    setBoundingBox = () => {
      this.boundingBox = this.canvas.getBoundingClientRect();
      this.offsetX = this.boundingBox.left;
      this.offsetY = this.boundingBox.top;
    }

    setRelMouseCoord = () => {  // stackoverflow answer for calculating click offsets through the parent trees and scroll positions
      function relMouseCoords(event){
        let totalOffsetX = 0;
        let totalOffsetY = 0;
        let canvasX = 0;
        let canvasY = 0;
        let currentElement = this;
    
        do{
            totalOffsetX += currentElement.offsetLeft - currentElement.scrollLeft;
            totalOffsetY += currentElement.offsetTop - currentElement.scrollTop;
        }
        while(currentElement = currentElement.offsetParent)
    
        canvasX = event.pageX - totalOffsetX;
        canvasY = event.pageY - totalOffsetY;
    
        return {x:canvasX, y:canvasY}
      }
      HTMLCanvasElement.prototype.relMouseCoords = relMouseCoords;
    }
  
    mouseDown = (e) => {
      e.preventDefault();
      let vertSelected = false;
  
      // const mouseX = +(e.clientX-this.offsetX); // Offsets are needed because events provide the xy position of the click for the entire window, not relative to the canvas
      // const mouseY = +(e.clientY-this.offsetY);
      console.log('ClientX: ', e.clientX);
      console.log('ClientY: ', e.clientY);

      const mCoords = this.canvas.relMouseCoords(e);
      const mouseX = mCoords.x;
      const mouseY = mCoords.y;
  
  
      this.drag = null;
      for(let vert of this.props.graph.vertexes) {
        const dx = vert.pos.x-mouseX;
        const dy = vert.pos.y-mouseY;
        if((dx * dx) + (dy * dy) < (this.props.vertexRadius * this.props.vertexRadius)) { // Check if click was within the radius of any node
          this.drag = vert.value;

          if(!this.selected[0] || this.selected[0] && this.selected[0].group === vert.group) { // make sure the 2nd node is reachable otherwise dont allow selection
            this.select(vert);
            vertSelected = true;
            break;
          }
        }
      }
  
      if(!vertSelected) {
        console.log('not a vertex');
        this.clearSelected();
      }
      this.startX = mouseX;
      this.startY = mouseY;
    }
  
    select = (vert) => {
      if(this.isSelected(vert)){
        this.selected = this.selected.filter(elem => elem.value !== vert.value);
        if(this.selected.length === 0) {
          this.path = [];
        }
        this.updateCanvas();
      } else if(this.selected.length >= 2) {
        // this.clearSelected();
        this.selected.pop();
        this.selected.push({ value: vert.value, group: vert.group });
        this.updateCanvas();
      } else {
        this.selected.push({ value: vert.value, group: vert.group });
        this.updateCanvas();
      }
    }
  
    clearSelected = () => {
      this.selected = [];
      this.path = [];
      this.updateCanvas();
    }
  
    mouseUp = (e) => {
      e.preventDefault();
      this.drag = null;
    }
  
    mouseMove = (e) => {
      if(this.drag) {
        e.preventDefault();
  
        // const mouseX = +(e.clientX-this.offsetX);
        // const mouseY = +(e.clientY-this.offsetY);
        const mCoords = this.canvas.relMouseCoords(e);
        const mouseX = mCoords.x;
        const mouseY = mCoords.y;

        const dx = mouseX - this.startX;
        const dy = mouseY - this.startY;
  
        for(let vert of this.props.graph.vertexes) {
          if(this.drag === vert.value) {
            vert.pos.x += dx;
            vert.pos.y += dy;
            if(dx > 10 || dy > 10) {  // threshold to deselect by dragging,  nudging the mouse slightly is common with single clicks
              this.selected = this.selected.filter(elem => elem.value !== vert.value);
            }
          }
        }
  
        this.updateCanvas();
        this.startX = mouseX;
        this.startY = mouseY;
      }
    }
  
    clearCanvas = () => {
      this.ctx.fillStyle = 'white';
      this.ctx.fillRect(0, 0, this.props.canvasWidth, this.props.canvasHeight);
    }
  
    isSelected = (vert) => {
      for(let selected of this.selected) {
        if(selected.value === vert.value) {
          return true;
        }
      }
      return false;
    }
  
    /**
     * Render the canvas
     */
    updateCanvas() {
      const ctx = this.ctx;
  
      this.clearCanvas();
  
      // ------------ Graph -----------------------------
      this.props.graph.getConnectedComponents();
  
      if(this.selected.length === 2) {
        let firstSelected, secondSelected;
        for(let vertex of this.props.graph.vertexes) {
          if(vertex.value === this.selected[0].value){
            firstSelected = vertex;
          } else if (vertex.value === this.selected[1].value) {
            secondSelected = vertex;
          }
        }
        // console.log('selected: ', firstSelected);
        this.path = this.props.graph.dijkstra(firstSelected, secondSelected);
      }
  
      ctx.lineWidth=2;
      for(let vertex of this.props.graph.vertexes) {  // draw edges before nodes to asure theyre always below
        for(let edge of vertex.edges) {
          const offX = (edge.destination.pos.x - vertex.pos.x) / 2;
          const offY = (edge.destination.pos.y - vertex.pos.y) / 2;
          ctx.beginPath();
          ctx.moveTo(vertex.pos.x, vertex.pos.y);
          ctx.lineTo(edge.destination.pos.x, edge.destination.pos.y); // edge
          ctx.strokeStyle = vertex.color;
          if (this.path) {
            if (edge.destination.value === this.path[vertex.value]) {
              ctx.strokeStyle = 'black';
              ctx.lineWidth = 4;
            } else if (vertex.value === this.path[edge.destination.value]) {
              ctx.strokeStyle = 'black';
              ctx.lineWidth = 4;
            } else {
              ctx.lineWidth = 2;
            }
          }
          ctx.stroke();
  
          ctx.beginPath();
          ctx.arc(vertex.pos.x + offX, vertex.pos.y + offY, 9, 0, 2*Math.PI);  // edge weight circle
          ctx.fillStyle = 'white';
          ctx.strokeStyle = 'grey';
          ctx.fill();
          ctx.stroke();
  
          ctx.fillStyle = 'black';
          ctx.font = '10px Arial';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(edge.weight, vertex.pos.x + offX, vertex.pos.y + offY);  // edge weight label
        }
      }
  
      for(let vertex of this.props.graph.vertexes) { // drawing nodes
        ctx.beginPath();
        ctx.arc(vertex.pos.x, vertex.pos.y, this.props.vertexRadius, 0, 2*Math.PI);
        ctx.fillStyle = vertex.color;
        ctx.fill();
  
        if(this.isSelected(vertex)) {
          ctx.lineWidth = 4;
          ctx.strokeStyle = 'black';
          ctx.stroke();
        }
  
        ctx.fillStyle = 'black';
        ctx.font = Math.floor(this.props.vertexRadius * 0.5) + 'px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(vertex.value, vertex.pos.x, vertex.pos.y);
      }
  
      // ----------------------------------------------------
  
      // ------------- Retro C64 looking trippy thing ---------------
      // for(let x = 0; x < canvasWidth; x += 5) {
      //   for(let y = 0; y < canvasHeight; y += 5) {
      //       const r = (Math.sqrt(y * (x/20))) % 255;
      //       const g = (Math.cos(x*y + Math.sin(y)) * 100) % 255;
      //       const b = (r*(y/(Math.PI*r)) + g) % 255;
      //       ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
      //       ctx.fillRect(x, y, 5, 5);
      //   }
      // }
      // -------------------------------------------
  
      // ------------- Happy Accident ---------------
      // for(let x = 0; x < canvasWidth; x++) {
      //   for(let y = 0; y < canvasHeight; y++) {
      //       const r = (Math.sqrt(y * (x/20))) % 255;
      //       const g = (Math.cos(x*y + Math.sin(y)) * 100) % 255;
      //       const b = (r*(y/(Math.PI*r)) + g) % 255;
      //       ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
      //       ctx.fillRect(x, y, 1, 1);
      //   }
      // }
      // -------------------------------------------
  
      // --------------- FIB Spiral ----------------------
  
      // for(let y = 0; y < canvasHeight; y++) {
      //   for(let x = 0; x < canvasWidth; x++) {
      //     const py = (y - canvasHeight/2) / canvasHeight ;
      //     const px = (x - canvasWidth/2) / canvasHeight ;
      //     const lp = Math.sqrt(Math.pow(py, 2) + Math.pow(px, 2));
      //     const spiralTension = 0.618;
      //     const theta = Math.atan(px/py);
      //     const spiral = ((Math.log(lp)/spiralTension) + theta);
      //     const r = ( Math.sin(10 * spiral) * 150 ) * Math.atan(x/y) % 255;
      //     const g = ( Math.sin(10 * spiral) * 150 ) % 255;
      //     const b = ( Math.sin(10 * spiral) * 150 ) + Math.sqrt(y) * 2 % 255;
      //     ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
      //     ctx.fillRect(x, y, 1, 1);
      //   }
      // }
  
      // -----------------------------------------------
  
  
      // ------------ Space thing ---------------------------------------------
      // ctx.beginPath();
      // for(let x = 0; x < canvasWidth; x++) {
      //   for(let y = 0; y < canvasHeight; y++) {
      //     const r = Math.cos((Math.sqrt(y)*Math.tan(x)*-x)) % 255;
      //     const b = Math.tan((Math.sqrt(y)*Math.tan(x)*x)) % 255;
      //     const g = (b + (r + (Math.PI/2))) % 255;
  
      //     ctx.fillStyle = 'rgb(' + r + ', ' + g + ', ' + b + ')';
      //     ctx.fillRect(x, y, 1, 1);
      //   }
      // }
  
      // ctx.globalAlpha = 0.01;
      // ctx.lineWidth=1;
      // // for(let i = 0; i < 50; i++) {
      // //   // ctx.beginPath();
      // //   // ctx.fillStyle = 'black';
      // //   ctx.strokeStyle = 'rgb(200, 50, 100)';
      // //   ctx.arc((Math.cos(i)*canvasWidth), (i)*10, Math.sqrt(i), 0, Math.PI * 2);
      // //   // ctx.fill();
      // //   ctx.stroke();
      // //   ctx.closePath();
      // // }
      // // ctx.beginPath();
      // // for(let i = 0; i < 50; i++) {
      // //   // ctx.fillStyle = 'black';
      // //   ctx.strokeStyle = 'rgb(200, 50, 100)';
      // //   ctx.arc((i*i)/2, i*10, Math.sqrt(i), 0, Math.PI * 2);
      // //   // ctx.fill();
      // //   ctx.stroke();
      // //   ctx.closePath();
      // // }
  
      // ctx.beginPath();
      // for(let i = 0; i < 50; i++) {
      //   // ctx.fillStyle = 'black';
      //   ctx.strokeStyle = 'rgb(200, 50, 100)';
      //   ctx.arc(Math.cos(i)*canvasWidth, i*10, Math.sqrt(i), 0, Math.PI * 2);
      //   // ctx.fill();
      //   ctx.stroke();
      //   ctx.closePath();
      // }
      // ctx.globalAlpha = 1;
      // ctx.lineWidth=0.5;
      // ctx.beginPath();
      // // ctx.fillStyle = 'white';
      // ctx.strokeStyle = 'white';
      // const radgrad = ctx.createRadialGradient(canvasWidth/2, canvasHeight/2, 100, canvasWidth/2, canvasWidth/2, 1);
      // radgrad.addColorStop(0, 'rgba(0,0,0,0)');
      // radgrad.addColorStop(1, '#70002C');
      // // radgrad.addColorStop(1, 'white');
      // ctx.fillStyle = radgrad;
      // ctx.arc(canvasWidth/2, canvasHeight/2, 70, 0, Math.PI * 2);
      // ctx.fill();
      // ctx.stroke();
      // ctx.closePath();
  
      // -------------------------------------------------------
  
    }
  
  
    /**
     * Render
     */
    
    render() {
      return (
          <canvas ref="canvas" ></canvas>
      );
    }
}

export default View;