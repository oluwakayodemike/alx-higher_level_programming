#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // return an empty object if w or h is not positive
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // print the rectangle using the character X
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
