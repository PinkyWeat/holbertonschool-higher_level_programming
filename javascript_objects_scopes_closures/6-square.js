#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
    charPrint(c) {
        if (c === undefined) {
            console.log('X');
        } else {
            let escuer = '';
            for (let char = 0; char < this.size; char++) {
                escuer += c;
            }
            for (let counter = 0; counter < this.size; counter++) {
                console.log(escuer);
            }
        }
    }
};
