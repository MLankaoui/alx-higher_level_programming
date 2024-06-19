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
};
