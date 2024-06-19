#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    // create an empty object if the w or h ar not postivie
    if (!(w > 0 && h > 0)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
  // instance method print that prints a shape with a width and height
  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  // this rotates the shape
  rotate () {
    let i;
    for (i = 0; i < this.width * 2; i++) {
      console.log('X'.repeat(this.height * 2));
    }
  }
  
  // this doubles the height and the width of the shape
  double () {
    let i;
    for (i = 0; i < this.height * 2; i++) {
      console.log('X'.repeat(this.width * 2));
    }
  }
  
};
