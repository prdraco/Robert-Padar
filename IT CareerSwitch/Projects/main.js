// Write your function here:
function howOld(age, year) {
  ages = age + (year - 2020);
  bornYear = 2020 - age;
  calcYear = bornYear - year;
  if(year > 2020) {    
    return `You will be ${ages} in the year ${year}`
  } else if(year < bornYear) {
      return `The year ${year} was ${calcYear} years before you were born`
  } else if(year < 2020 && year > bornYear) {
    return `You were ${ages} in the year ${year}`
  }
}

console.log(howOld(21,2008))
// Once your function is written, write function calls to test your code!
