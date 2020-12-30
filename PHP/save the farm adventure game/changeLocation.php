<?php
  // Change player location
function changeLocation(){	
  // Write your code here:
  global $location;
  echo "Where do you want to go?\n";
  $move = readline(">>");
  $move = strtolower($move);
  if($location === 'kitchen') {
    if($move === 'bathroom') {
      echo 'You go to: bathroom.\n';
      $location = 'bathroom';
    } elseif($move === 'woods') {
      echo 'You follow the winding path, shivering as you make your way deep into the Terror Woods.\n';
      $location = 'woods';
    } else {
      echo "You can't go directly to there from your current location. Try going somewhere else first.\n";
    }
  } elseif($location === 'bathroom') {
    if($move === 'kitchen') {
      echo 'You go to: kitchen.\n';
      $location = 'kitchen';
    } else {
      echo "You can't go directly to there from your current location. Try going somewhere else first.\n";
    }
  } elseif($location === 'woods') {
    if($move === 'kitchen') {
      echo 'You go to: kitchen.\n';
      $location = 'kitchen';
    } else {
      echo "You can't go directly to there from your current location. Try going somewhere else first.\n";
    }
  } else {
    echo "That doesn't make sense. Are you confused? Try 'look around'.\n";
  }
  
}