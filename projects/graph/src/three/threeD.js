import * as THREE from "three";
import OrbitControls from "./orbit_controls";

export default (vertexes, connections) => {
  let camera, scene, renderer;
  let ambientLight, directionalLight;
  let avgX, avgY, avgZ;

  const init = () => {
    const colors = ["aqua", "lime", "fuchsia", "yellow", "orange", "maroon", "purple", "lavender", "gray"];

    scene = new THREE.Scene();

    camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 2500);
    camera.position.z = 100;
    camera.position.y = 250;
    camera.position.x = 200;

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

        avgX += x;
        avgY += y;
        avgZ += z;

        const lineMaterial = new THREE.LineBasicMaterial({color: color, transparent: true, opacity: 0.65});
        const lineGeometry = new THREE.Geometry();
        const line = new THREE.Line(lineGeometry, lineMaterial);

        if (nextNode = connection[i+1]) {
          lineGeometry.vertices.push(new THREE.Vector3(x, y, z));
          lineGeometry.vertices.push(new THREE.Vector3(nextNode.pos.x, nextNode.pos.y, -nextNode.pos.z));
          scene.add(line);
        }
        
        const sphereGeometry = new THREE.SphereGeometry(17, 50, 50, 0, Math.PI*2, 0, Math.PI*2);
        const sphereMaterial = new THREE.MeshLambertMaterial({color: color});
        const node = new THREE.Mesh(sphereGeometry, sphereMaterial);

        node.position.x = x;
        node.position.y = y;
        node.position.z = z;

        scene.add(node);
      });
    });

    window.addEventListener("resize", () => onWindowResize(), false);
  }

  const onWindowResize = () => {
    const width = window.innerWidth, height = window.innerHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
    render();
  }

  const period = 5;
  const clock = new THREE.Clock();
  const matrix = new THREE.Matrix4();

  const pivot = new THREE.Object3D();
  pivot.position.set(avgX/20, avgY/20, avgZ/20);

  let angle = 0;

  const render = () => {
    const { x, y, z } = camera.position;
    const speed = 0.025;

    requestAnimationFrame(render);

    // matrix.makeRotationY(clock.getDelta()*2*Math.PI / period);
    // camera.position.applyMatrix4(matrix);
    // camera.lookAt(new THREE.Vector3(avgX/20, avgY/20, avgZ/20));
    // camera.lookAt(800, 400, -2500);
    // console.log(camera.position);

    camera.position.x = x*Math.cos(speed) + z*Math.sin(speed);
    camera.position.y = y*Math.cos(speed/2) + z*Math.sin(speed/2);
    camera.position.z = z*Math.cos(speed) - x*Math.sin(speed);
    camera.lookAt(800, 400, -2500);
    // camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }

  init();
  render();
}