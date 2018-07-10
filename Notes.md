#HTML Canvas Reference: https://www.w3schools.com/tags/ref_canvas.asp 

This reference will cover the properties and methods of the getContext("2d") object, which can be used to draw text, lines, boxes, circles, and more - on the canvas.

#Colors, Styles and Shadows

PROPERTIES

* fillStyle - Sets or returns the color, gradient, or pattern used to fill the drawing

* strokeStyle - Sets or returns the color, gradient, or pattern used for strokes

* shadowColor - Sets or returns the color to use for shadows

* shadowBlur - Sets or returns the blur level for shadows

* shadowOffsetX - Sets or returns the horizontal distance of the shadow from the shape

* shadowOffsetX - Sets or returns the verticle distance of the shadow from the shape


METHODS
* createLinearGradient() - Creates a linear gradient (to use on canvas content)

* createPattern() - Repeats a specified element in the specified direction

* createRadialGradient() - Creates a radial/circular gradient (to use on canvas content)

* addColorStop() - Specifies the colors and stop positions in a gradient object


LINES STYLES PROPERTIES

* lineCap - Sets or returns the style of the end caps for a line

* lineJoin - Sets or returns the type of corner created, when two lines meet

* lineWidth - Sets or returns the current line width

* miterLimit - Sets or returns the maximum miter length


RECTANGLES

* rect() - Creates a rectangle 

* fillRect() - Draws a "filled" rectangle

* strokeRect() - Draws a rectangle (no fill)

* clearRect() - Clears the specified pixels within a given rectangle 


PATHS

* fill() - Fills the current drawing (path)

* stroke() - Actually draws the path you have defined

* beginPath() - Begins a path, or resets the current path

* moveTo() - Moves the path to the specified point in the canvas, without creating a line

* closePath() - Creates a path from the current point back to the starting point

* lineTo() - Adds a new point and creates a line to that point from the last specified point in the canvas

* clip() - Clips a region of any shape and size from the original canvas 

* quadraticCurveTo() - Creates a quadratic Bézier curve

* bezierCurveTo() - Creates a cubic Bézier curve

* arc() - Creates an arc/curve (used to create circles, or parts of circles)

* arcTo() - Creates an arc/curve between two tangents

* isPointInPath() - Returns true if the specified point is in the current path, otherwise false


TRANSFORMATIONS

* scale() - Scales the current drawing bigger or smaller

* rotate() - Rotates the current drawing

* translate() - Remaps the (0,0) position on the canvas

* transform() - Replaces the current transformation matrix for the drawing

* setTransform() - Resets the current transform to the identity matrix. Then runs transform()


TEXT

* font - Sets or returns the current font properties for the text content

* textAlign - Sets or returns the current alignment for text content

* textBaseline - Sets or returns the current text baseline used when drawing text

* fillText() - Draws "filled" text on the canvas

* strokeText() - Draws text on the canvas (no fill)

* measureText() - Returns an object that contains the width of the specified text


IMAGE DRAWING

* drawImage() - Draws an image, canvas, or video onto the canvas


PIXEL MANIPULATION

* width - Returns the width of an ImageData object

* height - Return the height of a ImageData object 

* data - Returns an object that contains image data of a specified ImageData object

* createImageData() - Creates a new, blank ImageData object

* getImageData() - Returns and ImageData object that copies the pixel data for the specified rectangle on a canvas

* putImageData() - Puts the image data (from a specified ImageData object) back onto the canvas


COMPOSTING

* globalAlpha - Sets or returns the current alpha or transparency value of the drawing 

* globalCompositeOperation - Sets or returns how a new image are drawn onto an existing image


OTHER

* save() - Saves the state of the current context 

* restore() - Returns previously saved path state and attributes

* createEvent()
* getContext()
* toDataURL()
