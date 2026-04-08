/**
 * @param {string} s
 * @return {number}
 */
var maxDistinct = function(s) {
   const d = new Set(s)
   return d.size
};
