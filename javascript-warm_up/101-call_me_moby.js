#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
    let supp = 0
    while (supp < x) {
        theFunction(); supp++;
    }
};