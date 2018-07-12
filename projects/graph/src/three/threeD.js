import * as THREE from "three";

export default (vertexes, connections) => {
  let camera, scene, renderer;
  let ambientLight;

  const init = () => {
    const colors = ["aqua", "lime", "fuchsia", "yellow", "gray", "orange", "maroon", "purple", "lavender"];

    camera = new THREE.OrthographicCamera(-50, 775, 625, -50, 1, 1000);
    scene = new THREE.Scene();
    renderer = new THREE.WebGLRenderer();

    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    ambientLight = new THREE.AmbientLight(0x404040);
    scene.add(ambientLight);

    connections.forEach(connection => {
      const geometry = new THREE.SphereGeometry(13, 32, 32, 0, Math.PI*2, 0, Math.PI*2);
      const material = new THREE.MeshStandardMaterial({color: colors.shift()});

      connection.forEach(v => {
        const node = new THREE.Mesh(geometry, material);
        node.position.x = v.pos.x;
        node.position.y = v.pos.y;
        scene.add(node);
      });
    });

    document.addEventListener("resize", () => onWindowResize());
  }

  const onWindowResize = () => {
    renderer.setSize(window.innerWidth, window.innerHeight);
  }

  const render = () => {
    requestAnimationFrame(render);
    renderer.render(scene, camera);
  }

  init();
  render();
}