const Calculate = {
  factorial(num) {
    if(num === 0) {
      return 1;
    }
    /*
    for (let i = num - 1; i >= 1; i--) {
      num = num * i; 
    }
    return num*/
    const numbers = [];
    for(let i = 1; i <= num; i++) {
    numbers.push(i);
}
    const reducer = (accumulator, currentValue) =>    accumulator * currentValue;
    return numbers.reduce(reducer);
  }
}

module.exports = Calculate;
