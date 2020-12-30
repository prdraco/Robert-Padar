let doorImage1 = document.getElementById('door1');
let botDoorPath = 'https://content.codecademy.com/projects/chore-door/images/robot.svg';

let doorImage2 = document.getElementById('door2');
let beachDoorPath = 'https://content.codecademy.com/projects/chore-door/images/beach.svg';

let doorImage3 = document.getElementById('door3');
let spaceDoorPath = 'https://content.codecademy.com/projects/chore-door/images/space.svg';

let closedDoorPath = 'https://content.codecademy.com/projects/chore-door/images/closed_door.svg';
let startButton = document.getElementById('start');
let currentlyPlaying = true;
let numClosedDoors = 3;
let openDoor1;
let openDoor2;
let openDoor3;


const isBot = (door) => {
  if(door.src === botDoorPath) {
    return true;
  } else {
    return false;
  }
}

const isClicked = (door) => {
  if(door.src === closedDoorPath) {
    return false;
  } else {
    return true;
  }
}

const playDoor = (door) => {
  numClosedDoors--;
  if(numClosedDoors === 0) {
    gameOver('win');
  } else if(isBot(door)) {
    gameOver('lose');
  }
}

const randomChoreDoorGenerator = () => {
  let choreDoor = Math.floor(Math.random()*numClosedDoors);
  if(choreDoor === 0) {
    openDoor1 = botDoorPath;
    openDoor2 = spaceDoorPath;
    openDoor3 = beachDoorPath;
  } else if(choreDoor === 1) {
    openDoor1 = beachDoorPath;
    openDoor2 = botDoorPath;
    openDoor3 = spaceDoorPath;
  } else if(choreDoor === 2) {
    openDoor1 = spaceDoorPath;
    openDoor2 = beachDoorPath;
    openDoor3 = botDoorPath;    
  }
}

door1.onclick = () => {
  if(currentlyPlaying && !isClicked(doorImage1)) {
    doorImage1.src = openDoor1;
    playDoor(door1);
  }
};
door2.onclick = () => { 
  if(currentlyPlaying && !isClicked(doorImage2)) {
    doorImage2.src = openDoor2;
    playDoor(door2);
  }
};
door3.onclick = () => {  
  if(currentlyPlaying && !isClicked(doorImage3)) {
    doorImage3.src = openDoor3;
    playDoor(door3);
  }
};

startButton.onclick = () => {
  if(currentlyPlaying === false) {
    startRound();
  }
}

const startRound = () => {
  door1.src = closedDoorPath;
  door2.src = closedDoorPath;
  door3.src = closedDoorPath;
  numClosedDoors = 3;
  startButton.innerHTML = 'Good luck!';
  currentlyPlaying = true;
  randomChoreDoorGenerator();
}

const gameOver = (status) => {
  if(status === 'win') {
    startButton.innerHTML = 'You win! Play again?';
  } else {    
    startButton.innerHTML = 'Game Over! Play again?';
  }
  currentlyPlaying = false;
}

startRound();

