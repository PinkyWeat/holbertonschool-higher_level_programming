#!/usr/bin/node
exports.esrever = function (list) {
  const helper = [];

  for (let item = list.length - 1; item >= 0; item--) {
    helper.push(list[item]);
  }
  return helper;
};
