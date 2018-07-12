import * as THREE from "three";
import OrbitControls from "./orbit_controls";

export default (vertexes, connections) => {
  let cameraX = 350, cameraY = 300, cameraZ = 1000;
  let camera, scene, renderer, controls;
  let ambientLight, directionalLight;

  const nodes = [];
  const lines = [];

  const init = () => {
    const colors = ["aqua", "lime", "fuchsia", "yellow", "orange", "maroon", "purple", "lavender", "gray"];

    scene = new THREE.Scene();
    // scene.position.set(10, 10, -25);

    camera = new THREE.PerspectiveCamera(55, window.innerWidth/window.innerHeight, 0.1, 1500);
    // camera.position.set(0, 100, 150);
    // camera.lookAt(scene.position);

    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    ambientLight = new THREE.AmbientLight(0x8c8c8c, 1);
    directionalLight = new THREE.DirectionalLight(0x8c8c8c, 1);
    scene.add(ambientLight);
    scene.add(directionalLight);

    connections.forEach(connection => {
      const color = colors.shift() || "white";

      connection.forEach((v, i) => {
        let nextNode;
        const x = v.pos.x, y = v.pos.y, z = -v.pos.z;

        const lineMaterial = new THREE.LineBasicMaterial({color: "white"});
        const lineGeometry = new THREE.Geometry();
        const line = new THREE.Line(lineGeometry, lineMaterial);

        if (nextNode = connection[i+1]) {
          lineGeometry.vertices.push(new THREE.Vector3(x, y, z));
          lineGeometry.vertices.push(new THREE.Vector3(nextNode.pos.x, nextNode.pos.y, -nextNode.pos.z));
          scene.add(line);
          lines.push(line);
        }

        line.rotation.x += 0.01;
        
        const sphereGeometry = new THREE.SphereGeometry(10, 50, 50, 0, Math.PI*2, 0, Math.PI*2);
        const sphereMaterial = new THREE.MeshLambertMaterial({color: color});
        const node = new THREE.Mesh(sphereGeometry, sphereMaterial);

        node.position.x = x;
        node.position.y = y;
        node.position.z = z;

        nodes.push(node);

        scene.add(node);
      });
    });

    window.addEventListener("resize", () => onWindowResize(), false);
    console.log(scene.position);
  }

  const onWindowResize = () => {
    const width = window.innerWidth, height = window.innerHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
    render();
  }

  const render = () => {
    requestAnimationFrame(render);
    renderer.render(scene, camera);
  }

  init();
  render();
}