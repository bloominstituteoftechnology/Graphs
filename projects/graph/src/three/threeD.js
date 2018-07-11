import * as THREE from "three";
// import TrackballControls from "three-trackballcontrols";

export default vertexes => {
  const width = window.innerWidth, height = window.innerHeight;
  let camera, controls, scene, renderer;

  const init = () => {
    camera = new THREE.PerspectiveCamera(65, width/height, 0.1, 1000);
    camera.position.set(333, 233, 500);

    scene = new THREE.Scene();

    vertexes.forEach(v => {
      const x = v.pos.x - v.pos.x*0.5;
      const y = v.pos.y - v.pos.y*0.5;

      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");

      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillStyle = "red";
      ctx.font = "100px arial bold";
      ctx.fillText(v.value, x, y, 26);

      const texture = new THREE.CanvasTexture(canvas, THREE.SphericalReflectionMapping);

      const display = {
        color: "skyblue",
        map: texture,
        side: THREE.FrontSide,
        depthFunc: THREE.AlwaysDepth,
        combine: THREE.MixOperation
      }

      const geometry = new THREE.SphereGeometry(13, 32, 32);
      const material = new THREE.MeshBasicMaterial(display);
      const node = new THREE.Mesh(geometry, material);

      node.position.x = x;
      node.position.y = y;

      scene.add(node);
    });

    renderer = new THREE.WebGLRenderer();
    renderer.setSize(width, height);
    document.body.appendChild(renderer.domElement);
  }

  const textureLabel = v => {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");

    ctx.fillStyle = "red";
    ctx.font = "30pt arial bold"
    ctx.fillText(v.value, v.pos.x, v.pos.y);

    return canvas;
  }

  const render = () => {
    requestAnimationFrame(render);
    renderer.render(scene, camera);
  }

  init();
  render();
}