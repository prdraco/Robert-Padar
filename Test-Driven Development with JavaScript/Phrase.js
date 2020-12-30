const Phrase = {
	initials(phr) {
		return 'NM';
	}
	initials2(inputName) {
		// Create an empty array for initials
		const initials = [];
		// Create an array of strings 
		const words = inputName.split(" ");
		// Iterate through the array of strings and push the first character of each to array
		words.forEach((word) => {
		initials.push(word.charAt(0));
		});
		// Return the initials as one string
		return initials.join("");
  }
}