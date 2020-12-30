var assert = require("assert");
var Calculate =  require('../index.js')

describe('Calculate', () => {
  describe('.factorial', () => {
    it('the output of 5! is equal to 120', () => {
      const expected = 120;
      const num = 5;
      const actual = Calculate.factorial(num);
      assert.equal(actual, expected);
    });
    it('method returns 6 when you pass 3!', () => {
      const expected = 6;
      const num = 3;
      const actual = Calculate.factorial(num);
      assert.equal(actual, expected);
    });
    it('error message with 0 number', () => {
      const expected = 1;
      const num = 0;
      const actual = Calculate.factorial(num);
      assert.equal(actual, expected);
    });
  });
});