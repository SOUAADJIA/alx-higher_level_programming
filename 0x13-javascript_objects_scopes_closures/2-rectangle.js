#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if w or h is equal to 0 or not a positive integer
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Create an empty object
      return {};
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
