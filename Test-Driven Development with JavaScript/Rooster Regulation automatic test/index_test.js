const assert = require('assert');
const Rooster = require('../index');

describe('Rooster', () => {
  describe('.announceDawn', () => {
    it('returns a rooster call', () => {
      // Define expected output
      const expected = 'cock-a-doodle-doo!';

      // Call Rooster.announceDawn and store result in variable
      const actual = Rooster.announceDawn();
      // Use an assert method to compare actual and expected result
      assert.equal(actual, expected);
    });
  });
  describe('.timeAtDawn', () => {
    it('returns its argument as a string', () => {
      //Setup
      const inputNumber = 12;
      const expected = '12';
      //Exercise
      const actual = Rooster.timeAtDawn(inputNumber);
      //Verify
      assert.equal(expected, actual);
    });
    it('throws a range error if passed a number less than 0', () => {
      //Setup
      const inputNumber = -1;
      //Exercise
      const expected = RangeError;
      //Verify
      assert.throws(() => {
        Rooster.timeAtDawn(inputNumber)
      }, expected);
    });
    it('throws an error if passed a number greater than 23', () => {
      //Setup
      const inputNumber = 24;
      //Exercise
      const expected = RangeError;
      //Verify
      assert.throws(() => {
        Rooster.timeAtDawn(inputNumber)
      }, expected);
    });
  });
});