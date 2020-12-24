<?php
namespace Codecademy;

$learner_one = ["is_correct"=>FALSE, "box"=>["shape"=>"none", "color"=>"none"]];
   
$learner_two = ["is_correct"=>TRUE, "box"=>["shape"=>"none", "color"=>"none"]];
  
function markAnswer($val, &$arr) {
  if($val) {
    $arr["shape"] = "checkmark";
    $arr["color"] = "green";
  } else {
    $arr["shape"] = "x";
    $arr["color"] = "red";    
  }
}

markAnswer($learner_one["is_correct"], $learner_one["box"]);
markAnswer($learner_two["is_correct"], $learner_two["box"]);

print_r($learner_one["box"]);
print_r($learner_two["box"]);