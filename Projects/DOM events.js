// Add the code you want to test below:
let view = document.getElementById('view-button');
let close = document.getElementById('close-button');
let codey = document.getElementById('codey');

let open = function() {
  codey.style.display = 'block';
  close.style.display = 'block';
};

let hide = function() {
  codey.style.display = 'none';
  close.style.display = 'none';
};

view.onclick = open;
close.onclick = hide;

// Write your code here
let textChange = function() {
  view.innerHTML = 'Hello, World!';
}
let textReturn = function() {
  view.innerHTML = 'View';
}

view.addEventListener('click', textChange);
close.addEventListener('click', textReturn);


//remove event handler
let fortunes = ["A beautiful, smart, and loving person will be coming into your life.",
  "A fresh start will put you on your way.",
  "A golden egg of opportunity falls into your lap this month.",
  "A smile is your personal welcome mat.",
  "All your hard work will soon pay off."
]

let button = document.getElementById('fortuneButton');
let fortune = document.getElementById('fortune');

function fortuneSelector(){
  let randomFortune = Math.floor(Math.random() * fortunes.length);
  return fortunes[randomFortune];
}

function showFortune(){
  fortune.innerHTML = fortuneSelector();
  button.innerHTML = "Come back tomorrow!";
  button.style.cursor = "default";

  //add your code here
  button.removeEventListener('click', showFortune)
}

button.addEventListener('click', showFortune);


// This variable stores the "Pick a Color" button
let button = document.getElementById('color-button');

// This variable stores the "Mystery Color" button
let mysteryButton = document.getElementById('next-button');

// This random number function will create color codes for the randomColor variable
function rgb(num) {
  return Math.floor(Math.random() * num);
}

// Write your code below
let colorChange = function (event) {
  let randomColor = 'rgb(' + rgb(255) + ',' + rgb(255) + ',' + rgb(255) + ')';
  event.target.style.backgroundColor = randomColor;
}

button.onclick = colorChange;
mysteryButton.onwheel = colorChange;

// mouseover, mouseup, mouseout
// These variables store the boxes on the side
let itemOne = document.getElementById('list-item-one');
let itemTwo = document.getElementById('list-item-two');
let itemThree = document.getElementById('list-item-three');
let itemFour = document.getElementById('list-item-four');
let itemFive = document.getElementById('list-item-five');
let resetButton = document.getElementById('reset-button');

// This function programs the "Reset" button to return the boxes to their default styles
let reset = function() {
  itemOne.style.width = ''
  itemTwo .style.backgroundColor = ''
  itemThree.innerHTML = 'The mouse must leave the box to change the text'
  itemFive.style.display = "none"
};
resetButton.onclick = reset;

// Write code for the first list item
itemOne.onmouseover = function(){
  itemOne.style.width = '430px';
};

// Write code for the second list item
itemTwo.onmouseup = function(){
  itemTwo.style.backgroundColor = 'green'
};

// Write code for the third list item
itemThree.onmouseout = function(){
  itemThree.innerHTML = 'The mouse has left the element.'
};

// Write code for the fourth list item
itemFour.onmousedown = function(){
  itemFive.style.display = 'block';
};

//keyfunctions like key push down
let ball = document.getElementById('float-circle');

// Write your code below
function up() {
  ball.style.bottom = '250px';
}

function down() {
  ball.style.bottom = '50px';
}

document.onkeydown = up;
document.onkeyup = down;