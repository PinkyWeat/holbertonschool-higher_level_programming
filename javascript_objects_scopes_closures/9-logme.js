#!/usr/bin/node
let helper = 0;
exports.logMe = function (item) {
  console.log(helper + ': ' + item);
  helper++;
};
