#!/usr/bin/node
const Esquer = require('./5-square');

module.exports = class Square extends Esquer {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
      this.print(c);
  }
};
