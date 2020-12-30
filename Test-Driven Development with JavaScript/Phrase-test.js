const assert = require('assert');
const Calculate =  require('../Phrase.js')

describe('Phrase', () => {
	describe('.initials', () => {
		it('returns the first letter of each word in a phrase.', () => {
		  const inputName = 'Nelson Mandela';
		  const expectedInitials = 'NM';
		  const result = Phrase.initials(inputName);
		  assert.equal(result, expectedInitials);
		});
	});
	describe('.initials2', () => {
		it('returns the initials of a name', () => {
		  const nameInput = 'Juan Manuel Santos';
		  const expectedInitials = 'JMS';

		  const result = Phrase.initials(nameInput);

		  assert.equal(result, expectedInitials);
		});
	});
});