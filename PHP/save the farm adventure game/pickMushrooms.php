<?php
  
function pickMushrooms(){
	// Write your code here:
  global $location, $has_mushrooms;
  if($location !== 'woods') {
    echo "There aren't any mushrooms to pick! You should go into the *woods*\n";
  } else {
    echo "You've picked some mushrooms.\n";
    $has_mushrooms = TRUE;
  }
}  