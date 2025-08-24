// ES6_classes/8-hbtn_class.js
export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // cast to Number
  valueOf() {
    return this._size;
  }

  // cast to String
  toString() {
    return this._location;
  }
}
