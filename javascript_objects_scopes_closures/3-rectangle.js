#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // first will concat width
    let guith = '';
    for (let uith = 0; uith < this.width; uith++) {
      guith += 'X';
    }
    // then print the width * height times
    for (let jait = 0; jait < this.height; jait++) {
      console.log(guith);
    }
  }
};
