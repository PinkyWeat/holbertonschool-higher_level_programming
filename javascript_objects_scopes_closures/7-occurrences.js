#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let res = 0;
  for (let item = 0; item < list.length; item++) {
    if (list[item] === searchElement) {
      ++res;
    }
  }
  return res;
};
