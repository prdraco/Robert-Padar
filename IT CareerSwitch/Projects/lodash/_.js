const _ = {};
_.clamp = (number, lower, upper) => {
    let lowerClampedValue = Math.max(number, lower);
    let clampedValue = Math.min(lowerClampedValue, upper) ;
    return clampedValue;
  },

_.inRange = (number, start, end) => {
    if(end === undefined) {
      end = start;
      start = 0;
    }
    if(start > end) {
      let temp = end;
      end = start;
      start = temp;
    }
    const isInRange = (start <= number && number < end);
    return isInRange;
  }

_.words = string => {
  let words = string.split(' ');
  return words;
}

_.pad = (string, length) => {
  if(length <= string.length) {
    return string;
  }
  const startPaddingLength = Math.floor((length - string.length) / 2);
  const endPaddingLength = length - string.length - startPaddingLength;
  const paddedString = ' '.repeat(startPaddingLength) + string + ' '.repeat(endPaddingLength);
  return paddedString;
}

_.has = (object, key) => {
  const hasValue = object[key];
  if(hasValue !== undefined) {
    return true;
  }
  return false;
}

_.invert = object => {
  let invertedObject = {};
  for(let key in object) {
    const originalValue = object[key];
    invertedObject = {originalValue: key};
  }
  return invertedObject;
}

_.findKey = (object, predicate) => {
  for(let key in object) {
    let value = object[key];
    let predicateReturnValue = predicate(value);
    if(predicateReturnValue === true) {
      return key;
    }
  return undefined;
  }
}

_.drop = (array, n) => {
  if(n === undefined) {
    n = 1;
  }
  const droppedArray = array.slice(n, array.length);
  return droppedArray;
}

_.dropWhile = (array, predicate) => {
  const cb = (element, index) => {
    return !predicate(element, index, array);
  }
  let dropNumber = array.findIndex(cb);
  let droppedArray = _.drop(array, dropNumber);
  return droppedArray;
}

_.chunk = (array, size) => {
  if(size === undefined) {
    size = 1;
  }
  let arrayChunks = [];
  for(let i=0; i < array.length; i+=size) {
    let arrayChunk = array.slice(i, i+size);
    arrayChunks.push(arrayChunk);
  }
  return arrayChunks;
}

// Do not write or modify code below this line.
module.exports = _;