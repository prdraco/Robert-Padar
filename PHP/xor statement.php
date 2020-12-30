<?php
namespace Codecademy;
$banana_cream = ["whole milk", "sugar", "cornstarch", "salt", "egg yolks", "butter", "vanilla extract", "bananas", "heavy cream", "powdered sugar"];
$experimental_pie = ["whole milk", "sugar", "bananas", "chicken", "salmon", "garlic"];

// Write your code below:
function eatPie($list) {
  if(in_array("chicken", $list) xor in_array("bananas", $list)) {
    return "Delicious pie!";
  } else {
    return "Disgusting!";
  }
}

echo eatPie($banana_cream);
echo "\n\n";
echo eatPie($experimental_pie);