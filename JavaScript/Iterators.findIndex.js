const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

const foundAnimal = animals.findIndex(find => {
  return find === 'elephant';
})
console.log(foundAnimal);

const startsWithS = animals.findIndex(letter => {
  return letter[0] == 's';
})
console.log(startsWithS);