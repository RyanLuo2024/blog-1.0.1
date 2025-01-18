const conversionFactor = 180 / Math.PI;

let radianToDegrees = function(radian) {
	return radian * conversionFactor;
}
let degreesToRadian = function(degrees) {
	return degrees / conversionFactor;
}

// Taken from https://github.com/wethegit/wtc-vector
/**
 * A basic 2D Vector class that provides simple algebraic functionality in the form
 * of 2D Vectors.
 *
 * We use Getters/setters for both principle properties (x & y) as well as virtual
 * properties (rotation, length etc.).
 *
 * @class Vector
 * @author Liam Egan <liam@wethecollective.com>
 * @version 0.5
 * @created Dec 19, 2017
 */
class Vector {

	/**
	 * The Vector Class constructor
	 *
	 * @constructor
	 * @param {number} x 				The x coord
	 * @param {number} y 				The y coord
	 */
  constructor(x, y){
    this.x = x;
    this.y = y;
  }

  /**
   * Resets the vector coordinates
   *
   * @public
	 * @param {number} x 				The x coord
	 * @param {number} y 				The y coord
   */
	reset(x, y) {
    this.x = x;
    this.y = y;
	}
  resetToVector(v) {
    if(v instanceof Vector) {
      this.x = v.x;
      this.y = v.y;
    }
  }

	/**
	 * Clones the vector
	 *
	 * @public
	 * @return {Vector}					The cloned vector
	 */
  clone() {
    return new Vector(this.x, this.y);
  }

  /**
   * Adds one vector to another.
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to add to this one
   * @return {Vector}					Returns itself, modified
   */
  add(vector) {
    this.x += vector.x;
    this.y += vector.y;
    return this;
  }
  /**
   * Clones the vector and adds the vector to it instead
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to add to this one
   * @return {Vector}					Returns the clone of itself, modified
   */
  addNew(vector) {
    let v = this.clone();
    return v.add(vector);
  }

  /**
   * Adds a scalar to the vector, modifying both the x and y
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to add to the vector
   * @return {Vector}					Returns itself, modified
   */
  addScalar(scalar) {
    return this.add(new Vector(scalar, scalar));
  }
  /**
   * Clones the vector and adds the scalar to it instead
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to add to the vector
   * @return {Vector}					Returns the clone of itself, modified
   */
  addScalarNew(scalar) {
    let v = this.clone();
    return v.addScalar(scalar);
  }

  /**
   * Subtracts one vector from another.
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to subtract from this one
   * @return {Vector}					Returns itself, modified
   */
  subtract(vector) {
    this.x -= vector.x;
    this.y -= vector.y;
    return this;
  }
  /**
   * Clones the vector and subtracts the vector from it instead
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to subtract from this one
   * @return {Vector}					Returns the clone of itself, modified
   */
  subtractNew(vector) {
    let v = this.clone();
    return v.subtract(vector);
  }

  /**
   * Subtracts a scalar from the vector, modifying both the x and y
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to subtract from the vector
   * @return {Vector}					Returns itself, modified
   */
  subtractScalar(scalar) {
    return this.subtract(new Vector(scalar, scalar));
  }
  /**
   * Clones the vector and subtracts the scalar from it instead
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to add to the vector
   * @return {Vector}					Returns the clone of itself, modified
   */
  subtractScalarNew(scalar) {
    let v = this.clone();
    return v.subtractScalar(scalar);
  }

  /**
   * Divides one vector by another.
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to divide this by
   * @return {Vector}					Returns itself, modified
   */
  divide(vector) {
    if(vector.x !== 0) {
      this.x /= vector.x
    } else {
      this.x = 0;
    }
    if(vector.y !== 0) {
      this.y /= vector.y
    } else {
      this.y = 0;
    }
    return this;
  }
  /**
   * Clones the vector and divides it by the vector instead
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to divide the clone by
   * @return {Vector}					Returns the clone of itself, modified
   */
  divideNew(vector) {
    let v = this.clone();
    return v.divide(vector);
  }

  /**
   * Divides the vector by a scalar.
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to divide both x and y by
   * @return {Vector}					Returns itself, modified
   */
  divideScalar(scalar) {
    var v = new Vector(scalar, scalar);
    return this.divide(v);
  }
  /**
   * Clones the vector and divides it by the provided scalar.
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to divide both x and y by
   * @return {Vector}					Returns the clone of itself, modified
   */
  divideScalarNew(scalar) {
    let v = this.clone();
    return v.divideScalar(scalar);
  }

  /**
   * Multiplies one vector by another.
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to multiply this by
   * @return {Vector}					Returns itself, modified
   */
  multiply(vector) {
    this.x *= vector.x;
    this.y *= vector.y;
    return this;
  }
  /**
   * Clones the vector and multiplies it by the vector instead
   *
   * @public
   * @chainable
   * @param  {Vector}  vector The vector to multiply the clone by
   * @return {Vector}					Returns the clone of itself, modified
   */
  multiplyNew(vector) {
    let v = this.clone();
    return v.multiply(vector);
  }

  /**
   * Multiplies the vector by a scalar.
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to multiply both x and y by
   * @return {Vector}					Returns itself, modified
   */
  multiplyScalar(scalar) {
    var v = new Vector(scalar, scalar);
    return this.multiply(v);
  }
  /**
   * Clones the vector and multiplies it by the provided scalar.
   *
   * @public
   * @chainable
   * @param  {number}  scalar The scalar to multiply both x and y by
   * @return {Vector}					Returns the clone of itself, modified
   */
  multiplyScalarNew(scalar) {
    let v = this.clone();
    return v.multiplyScalar(scalar);
  }

  /**
   * Alias of {@link Vector#multiplyScalar__anchor multiplyScalar}
   */
  scale(scalar) {
    return this.multiplyScalar(scalar);
  }
  /**
   * Alias of {@link Vector#multiplyScalarNew__anchor multiplyScalarNew}
   */
  scaleNew(scalar) {
    return this.multiplyScalarNew(scalar);
  }

  /**
   * Rotates a vecor by a given amount, provided in radians.
   *
   * @public
   * @chainable
   * @param  {number}  radian The angle, in radians, to rotate the vector by
   * @return {Vector}					Returns itself, modified
   */
  rotate(radian) {
  	var x = (this.x * Math.cos(radian)) - (this.y * Math.sin(radian));
  	var y = (this.x * Math.sin(radian)) + (this.y * Math.cos(radian));

		this.x = x;
		this.y = y;

  	return this;
  }
  /**
   * Clones the vector and rotates it by the supplied radian value
   *
   * @public
   * @chainable
   * @param  {number}  radian The angle, in radians, to rotate the vector by
   * @return {Vector}					Returns the clone of itself, modified
   */
  rotateNew(radian) {
    let v = this.clone();
    return v.rotate(radian);
  }

	/**
	 * Rotates a vecor by a given amount, provided in degrees. Converts the degree
	 * value to radians and runs the rotaet method.
	 *
	 * @public
	 * @chainable
	 * @param  {number}  degrees The angle, in degrees, to rotate the vector by
	 * @return {Vector}						Returns itself, modified
	 */
  rotateDeg(degrees) {
    return this.rotate(degreesToRadian(degrees));
  }
  /**
   * Clones the vector and rotates it by the supplied degree value
   *
   * @public
   * @chainable
	 * @param  {number}  degrees The angle, in degrees, to rotate the vector by
   * @return {Vector}					 Returns the clone of itself, modified
   */
  rotateDegNew(degrees) {
    return this.rotateNew(degreesToRadian(degrees));
  }

  /**
   * Alias of {@link Vector#rotate__anchor rotate}
   */
  rotateBy(radian) {
		return this.rotate(radian);
  }
  /**
   * Alias of {@link Vector#rotateNew__anchor rotateNew}
   */
  rotateByNew(radian) {
    return this.rotateNew(radian);
  }

  /**
   * Alias of {@link Vector#rotateDeg__anchor rotateDeg}
   */
  rotateDegBy(degrees) {
		return this.rotateDeg(degrees);
  }
  /**
   * Alias of {@link Vector#rotateDegNew__anchor rotateDegNew}
   */
  rotateDegByNew(radian) {
    return tjos.rotateDegNew(radian);
  }

  /**
   * Rotates a vector to a specific angle
   *
   * @public
   * @chainable
   * @param  {number}  radian The angle, in radians, to rotate the vector to
   * @return {Vector}					Returns itself, modified
   */
	rotateTo(radian) {
		return this.rotate(radian-this.angle);
	};
  /**
   * Clones the vector and rotates it to the supplied radian value
   *
   * @public
   * @chainable
   * @param  {number}  radian The angle, in radians, to rotate the vector to
   * @return {Vector}					Returns the clone of itself, modified
   */
	rotateToNew(radian) {
    let v = this.clone();
    return v.rotateTo(radian);
	};

	/**
	 * Rotates a vecor to a given amount, provided in degrees. Converts the degree
	 * value to radians and runs the rotateTo method.
	 *
	 * @public
	 * @chainable
	 * @param  {number}  degrees The angle, in degrees, to rotate the vector to
	 * @return {Vector}						Returns itself, modified
	 */
  rotateToDeg(degrees) {
    return this.rotateTo(degreesToRadian(degrees));
  }
  /**
   * Clones the vector and rotates it to the supplied degree value
   *
   * @public
   * @chainable
	 * @param  {number}  degrees The angle, in degrees, to rotate the vector to
   * @return {Vector}					 Returns the clone of itself, modified
   */
  rotateToDegNew(degrees) {
    return this.rotateToNew(degreesToRadian(degrees));
  }

	/**
	 * Normalises the vector down to a length of 1 unit
	 *
	 * @public
	 * @chainable
	 * @return {Vector}					Returns itself, modified
	 */
	normalise() {
		return this.divideScalar(this.length);
	}
	/**
	 * Clones the vector and normalises it
	 *
	 * @public
	 * @chainable
	 * @return {Vector}					Returns a clone of itself, modified
	 */
	normaliseNew() {
		return this.divideScalarNew(this.length);
	}

	/**
	 * Calculates the distance between this and the supplied vector
	 *
	 * @param  {Vector} vector The vector to calculate the distance from
	 * @return {number}        The distance between this and the supplied vector
	 */
	distance(vector) {
		return this.subtractNew(vector).length;
	}

	/**
	 * Calculates the distance on the X axis between this and the supplied vector
	 *
	 * @param  {Vector} vector The vector to calculate the distance from
	 * @return {number}        The distance, along the x axis, between this and the supplied vector
	 */
	distanceX(vector) {
		return this.x - vector.x;
	}

	/**
	 * Calculated the distance on the Y axis between this and the supplied vector
	 *
	 * @param  {Vector} vector The vector to calculate the distance from
	 * @return {number}        The distance, along the y axis, between this and the supplied vector
	 */
	distanceY(vector) {
		return this.y - vector.y;
	}


	/**
	 * Calculates the dot product between this and a supplied vector
	 *
	 * @example
	 * // returns -14
	 * new Vector(2, -3).dot(new Vector(-4, 2))
	 * new Vector(-4, 2).dot(new Vector(2, -3))
	 * new Vector(2, -4).dot(new Vector(-3, 2))
	 *
	 * @param  {Vector} vector The vector object against which to calculate the dot product
	 * @return {number}        The dot product of the two vectors
	 */
	dot(vector) {
		return (this.x * vector.x) + (this.y * vector.y);
	}

	/**
	 * Calculates the cross product between this and the supplied vector.
	 *
	 * @example
	 * // returns -2
	 * new Vector(2, -3).cross(new Vector(-4, 2))
	 * new Vector(-4, 2).cross(new Vector(2, -3))
	 * // returns 2
	 * new Vector(2, -4).cross(new Vector(-3, 2))
	 *
	 * @param  {Vector} vector The vector object against which to calculate the cross product
	 * @return {number}        The cross product of the two vectors
	 */
	cross(vector) {
		return (this.x * vector.x) - (this.y * vector.y);
	}
  
  // TODO Add this to the main class
  isEqualTo(vector) {
    return this.x === vector.x && this.y === vector.y;
  }
  
  // TODO Add this to the main class
  slopeOf(vector) {
    return ( vector.y - this.y ) / ( vector.x - this.x );
  }

  /**
   * Getters and setters
   */

  /**
   * (getter/setter) The x value of the vector.
   *
   * @type {number}
   * @default 0
   */
  set x(x) {
    if(typeof x == 'number') {
      this._x = x;
    } else {
      throw new TypeError('X should be a number');
    }
  }
  get x() {
    return this._x || 0;
  }

 /**
	* (getter/setter) The y value of the vector.
	*
	* @type {number}
	* @default 0
	*/
  set y(y) {
    if(typeof y == 'number') {
      this._y = y;
    } else {
      throw new TypeError('Y should be a number');
    }
  }
  get y() {
    return this._y || 0;
  }

	/**
	* (getter/setter) The length of the vector presented as a square. If you're using
	* length for comparison, this is quicker.
	*
	* @type {number}
	* @default 0
	*/
  set lengthSquared(length) {
    var factor;
    if(typeof length == 'number') {
      factor = length / this.lengthSquared;
      this.multiplyScalar(factor);
    } else {
      throw new TypeError('length should be a number');
    }
  }
  get lengthSquared() {
    return (this.x * this.x) + (this.y * this.y);
  }

	/**
	* (getter/setter) The length of the vector
	*
	* @type {number}
	* @default 0
	*/
  set length(length) {
    var factor;
    if(typeof length == 'number') {
      factor = length / this.length;
      this.multiplyScalar(factor);
    } else {
      throw new TypeError('length should be a number');
    }
  }
  get length() {
    return Math.sqrt(this.lengthSquared);
  }

	/**
	* (getter/setter) The angle of the vector, in radians
	*
	* @type {number}
	* @default 0
	*/
  set angle(radian) {
    if(typeof radian == 'number') {
      this.rotateTo(radian);
    } else {
      throw new TypeError('angle should be a number');
    }
  }
  get angle() {
    return Math.atan2(this.y, this.x);
  }

	/**
	* (getter/setter) The angle of the vector, in degrees
	*
	* @type {number}
	* @default 0
	*/
  set angleInDegrees(degrees) {
    if(typeof degrees == 'number') {
      this.rotateToDeg(degrees);
    } else {
      throw new TypeError('angle should be a number');
    }
  }
  get angleInDegrees() {
    return radianToDegrees(Math.atan2(this.y, this.x));
  }

	/**
	 * (getter/setter) Vector width.
   * Alias of {@link Vector#x x}
	 *
	 * @type {number}
	 */
	set width(w) {
		this.x = w;
	}
	get width() {
		return this.x;
	}

	/**
	 * (getter/setter) Vector height.
   * Alias of {@link Vector#x x}
	 *
	 * @type {number}
	 */
	set height(h) {
		this.y = h;
	}
	get height() {
		return this.y;
	}

	/**
	 * (getter/setter) Vector area.
	 * @readonly
	 *
	 * @type {number}
	 */
	get area() {
		return this.x * this.y;
	}
  
  // TODO Add this to the main class
  get slope() {
    return this.y / this.x;
  }

}



class Simulation {
  constructor(el) {
    if (el instanceof HTMLElement && el.nodeName.toLowerCase() === 'canvas') {
      this.el = el;
      this.ctx = el.getContext('2d');

      this.bodies = [];

      this.run = this.run.bind(this);
    } else {
      return null;
    }
  }

  addBody(body) {
    if (body instanceof Body) {
      body.yearsPerFrame = this.yearsPerFrame;
      body.dimensions = this.pxdimensions;
      this.bodies.push(body);
    }
    return this.bodies.length - 1;
  }
  removeBody(i) {
    this.bodies.splice(i, 1);
  }

  update() {
    // Set up the canvas for drawing
    this.ctx.fillStyle = `rgba(20,20,20,.9)`;
    // this.ctx.clearRect(0,0,this.el.width,this.el.height);
    this.ctx.fillRect(0, 0, this.el.width, this.el.height);
    this.ctx.translate(this.pxdimensions.width * .5, this.pxdimensions.height * .5);


    const lineThreshold = 20000;

    // Loop through all of the bodies
    this.bodies.forEach(bodyX => {
      const acceleration = new Vector(0, 0); // This is our basal, new acceleration for this body
      // For all the other bodies, calculate the combined force asserted on this
      this.bodies.forEach(bodyY => {
        const distance = bodyY.position.subtractNew(bodyX.position); // The distance between the two bodies
        const sqD = distance.lengthSquared; // The distance squared (cheaper than calculating actual distance, see: Pythagoras)
        const force = this.gravitationalConstant * bodyY.mass / (sqD * Math.sqrt(sqD * this.smoothing)); // Here's some newtonian motion with a some softening to stop it from reaching infinity

        acceleration.add(distance.scale(force));

        if (sqD < lineThreshold) {
          this.ctx.beginPath();
          this.ctx.strokeStyle = `rgba(255,255,255,${(lineThreshold - sqD) / lineThreshold * .5})`;
          this.ctx.lineWidth = 0;
          this.ctx.moveTo(bodyX.position.x, bodyX.position.y);
          this.ctx.lineTo(bodyY.position.x, bodyY.position.y);
          this.ctx.stroke();
        }
      });
      // Update the basal body's accelaration with the calucalted factor
      bodyX.acceleration = acceleration;

      // Draw the body
      this.ctx.beginPath();
      this.ctx.fillStyle = `rgba(255,255,255,1)`;
      this.ctx.arc(bodyX.position.x, bodyX.position.y, bodyX.size, 0, 2 * Math.PI);
      this.ctx.fill();

      // Solve for the next frame
      bodyX.solve();
    });
    // Reset current transformation matrix to the identity matrix
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
  }

  run(delta) {
    if (this.running === true) {
      requestAnimationFrame(this.run);
    }

    this.update();
  }

  set running(value) {
    if (this.running === false && value === true) requestAnimationFrame(this.run);
    this._running = value === true;
  }
  get running() {
    return this._running === true;
  }

  set pxratio(value) {
    if (!isNaN(value)) {
      this._pxratio = value;
    }
  }
  get pxratio() {
    return this._pxratio || 1;
  }

  set dimensions(value) {
    if (value instanceof Vector) {
      this._dimensions = value;
      this._pxdimensions = value.scale(this.pxratio);
      this.el.width = this._pxdimensions.width;
      this.el.height = this._pxdimensions.height;

      // Set up the canvas for drawing
      this.ctx.fillStyle = `rgba(20,20,20,1)`;
      // this.ctx.clearRect(0,0,this.el.width,this.el.height);
      this.ctx.fillRect(0, 0, this.el.width, this.el.height);
    }
  }
  get dimensions() {
    return this._dimensions || new Vector(this.el.width / this.pxratio, this.el.height / this.pxratio);
  }

  get pxdimensions() {
    return this._pxdimensions || new Vector(this.el.width, this.el.height);
  }

  set gravitationalConstant(value) {
    if (!isNaN(value)) this._gravitationalConstant = value;
  }
  get gravitationalConstant() {
    return this._gravitationalConstant || 40;
  }

  set smoothing(value) {
    if (!isNaN(value)) this._smoothing = value;
  }
  get smoothing() {
    return this._smoothing || .5;
  }

  set yearsPerFrame(value) {
    if (!isNaN(value)) this._yearsPerFrame = value;
  }
  get yearsPerFrame() {
    return this._yearsPerFrame || .2;
  }}


class Body {
  constructor(position, velocity, mass, size, fixed = false) {
    this.position = position;
    this.velocity = velocity;
    this.acceleration = new Vector(0, 0);
    this.mass = mass;
    this.size = size;
    this.fixed = fixed;
  }

  solve() {
    if (this.fixed) return;
    // console.log(this.acceleration)
    let vel = this.velocity.addNew(this.acceleration.scaleNew(this.yearsPerFrame));
    this.velocity = vel;
    this.position.add(this.velocity.scaleNew(this.yearsPerFrame));
    if (this.position.x > this.dimensions.x * .5 + 30.) {
      this.position.x = this.dimensions.x * -.5 - 10.;
    } else if (this.position.x < this.dimensions.x * -.5 - 30.) {
      this.position.x = this.dimensions.x * .5 + 10.;
    }
    if (this.position.y > this.dimensions.y * .5 + 30.) {
      this.position.y = this.dimensions.y * -.5 - 10.;
    } else if (this.position.y < this.dimensions.y * -.5 - 30.) {
      this.position.y = this.dimensions.y * .5 + 10.;
    }
  }

  set fixed(value) {
    this._fixed = value === true;
  }
  get fixed() {
    return this._fixed === true;
  }

  set position(value) {
    if (value instanceof Vector) {
      this._position = value;
    }
  }
  get position() {
    return this._position || null;
  }

  set friction(value) {
    if (!isNaN(value)) {
      this._friction = value;
    }
  }
  get friction() {
    return this._friction || .99;
  }

  set maxVelocity(value) {
    if (!isNaN(value)) {
      this._maxVelocity = value;
    }
  }
  get maxVelocity() {
    return this._maxVelocity || 50.;
  }

  set velocity(value) {
    if (value instanceof Vector) {
      if (value.length > this.maxVelocity) value.normalise().scale(this.maxVelocity);
      value.scale(this.friction);
      this._velocity = value;
    }
  }
  get velocity() {
    return this._velocity || null;
  }

  set acceleration(value) {
    if (value instanceof Vector) {
      this._acceleration = value;
    }
  }
  get acceleration() {
    return this._acceleration || null;
  }

  set mass(value) {
    if (!isNaN(value)) {
      this._mass = value;
    }
  }
  get mass() {
    return this._mass || 0;
  }

  set size(value) {
    if (!isNaN(value)) {
      this._size = value;
    }
  }
  get size() {
    return this._size || 0;
  }

  set yearsPerFrame(value) {
    if (!isNaN(value)) this._yearsPerFrame = value;
  }
  get yearsPerFrame() {
    return this._yearsPerFrame || .008;
  }}


console.clear();

const sim = new Simulation(document.querySelector('canvas'));
sim.dimensions = new Vector(window.innerWidth, window.innerHeight);
window.addEventListener('resize', e => {
  sim.dimensions = new Vector(window.innerWidth, window.innerHeight);
});

let mouseBody = new Body(new Vector(0, 0), new Vector(0, 0), -1000, 50, true);
let bodyIndex = null;
window.addEventListener('pointerdown', e => {
  mouseBody.position.x = e.pageX - window.innerWidth * .5;
  mouseBody.position.y = e.pageY - window.innerHeight * .5;
  console.log(mouseBody.position);
  bodyIndex = sim.addBody(mouseBody);
});
window.addEventListener('pointermove', e => {
  mouseBody.position.x = e.pageX - window.innerWidth * .5;
  mouseBody.position.y = e.pageY - window.innerHeight * .5;
});
window.addEventListener('pointerup', e => {
  sim.removeBody(bodyIndex);
  bodyIndex = null;
});

// sim.addBody(new Body(new Vector(0, 0), new Vector(0,0), -3, 50, true));
// sim.addBody(new Body(new Vector(0, 500), new Vector(0,0), 1, 10, true));

for (i = 0; i < 100; i++) {
  const r = new Vector(200 + Math.random() * 200, Math.random() * Math.PI * 2.);
  const p = new Vector(Math.cos(r.y) * r.x, Math.sin(r.y) * r.x);
  const a = new Vector(p.y, -p.x).normalise().scale(10.);
  // const a = new Vector(0,0);
  const rf = Math.random();
  sim.addBody(new Body(p, a, -10 + rf * 15., 1 + rf * 10));
  // sim.addBody(new Body(p, a, .5 + rf * .5, 5 + rf * 5.));

}

sim.running = true;