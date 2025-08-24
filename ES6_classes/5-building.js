// ES6_classes/5-building.js
export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
    if (new.target !== Building
        && this.evacuationWarningMessage === undefined) {
      throw new Error(
        'Class extending Building must override evacuationWarningMessage'
      );
    }
  }

  // getter
  get sqft() {
    return this._sqft;
  }
}
