/**
 * Edge
 */
export class Edge {
    constructor(destination, weight=1) {
        this.destination = destination;
        this.weight = weight;
    }
}

/**
 * Vertex
 */
export class Vertex {
    constructor(value='vertex') {
        this.value = value;
        this.edges = [];
        this.color = 'white';
    }
}

/**
 * Graph
 */
export class Graph {
    constructor() {
        this.vertexes = [];
    }

    /**
     * Create a random graph
     */
    randomize(width, height, pxBox, probability=0.6) {
        // Helper function to set up two-way edges
        function connectVerts(v0, v1) {
            v0.edges.push(new Edge(v1));
            v1.edges.push(new Edge(v0));
        }

        let count = 0;
        this.vertexes.length = 0;

        // Build a grid of verts
        let grid = [];
        for (let y = 0; y < height; y++) {
            let row = [];
            for (let x = 0; x < width; x++) {
                let v = new Vertex();
                //v.value = 'v' + x + ',' + y;
                v.value = 'v' + count++;
                row.push(v);
            }
            grid.push(row);
        }

        // Go through the grid randomly hooking up edges
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                // Connect down
                if (y < height - 1) {
                    if (Math.random() < probability) {
                        connectVerts(grid[y][x], grid[y+1][x]);
                    }
                }

                // Connect right
                if (x < width - 1) {
                    if (Math.random() < probability) {
                        connectVerts(grid[y][x], grid[y][x+1]);
                    }
                }
            }
        }

        // Last pass, set the x and y coordinates for drawing
        const boxBuffer = 0.8;
        const boxInner = pxBox * boxBuffer;
        const boxInnerOffset = (pxBox - boxInner) / 2;

        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                grid[y][x].pos = {
                    'x': (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
                    'y': (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
                };
            }
        }

        // Finally, add everything in our grid to the vertexes in this Graph
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                this.vertexes.push(grid[y][x]);
            }
        }
    }

    /**
     * Dump graph data to the console
     */
    dump() {
        let s;

        for (let v of this.vertexes) {
            if (v.pos) {
                s = v.value + ' (' + v.pos.x + ',' + v.pos.y + '):';
            } else {
                s = v.value + ':';
            }

            for (let e of v.edges) {
                s += ` ${e.destination.value}`;
            }
            console.log(s);
        }
    }

    /**
     * BFS
     *
     * This is a stock BFS, but it is NOT USED in this code. See bfsStep, below.
     */
    bfs(start) {
        const queue = [];

        for (let v of this.vertexes) {
            v.color = 'white';
        }

        start.color = 'gray';
        start.parent = null;
        queue.push(start);

        while (queue.length > 0) {
            let u = queue[0];

            for (let e of u.edges) {
                const v = e.destination;

                if (v.color === 'white') {
                    v.color = 'gray';
                    v.parent = u;
                    queue.push(v);
                }
            }

            queue.shift();
            u.color = 'black';
            console.log(u.value);
        }
    }

    /**
     * BFS step
     */
    bfsStep(start=null, reset=false) {
        if (reset) {
            for (let v of this.vertexes) {
                v.color = 'white';
            }
        }

        if (start !== null) {
            this.bfsQueue = [];
            this.bfsCurrent = start;
            this.bfsComponent = [];

            start.color = 'gray';
            start.parent = null;
            this.bfsQueue.push(start);
        }

        let u = this.bfsQueue[0];

        for (let e of u.edges) {
            const v = e.destination;

            if (v.color === 'white') {
                v.color = 'gray';
                v.parent = u;
                this.bfsQueue.push(v);
            }
        }

        this.bfsQueue.shift();
        u.color = 'black';

        this.bfsComponent.push(u);

        // If we're done, return this connected component. Otherwise return
        // null.
        return this.bfsQueue.length === 0? this.bfsComponent: null;
    }
}