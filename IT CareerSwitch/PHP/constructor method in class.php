<?php
class Beverage {
  public $temperature, $color, $opacity;
  // Add a constructor method to our Beverage class.
  function __construct($temperature, $color) {
    /* Modify the constructor to take $temperature and $color arguments (in that order) and set them to their respective object properties.*/
    $this->temperature = $temperature; 
    $this->color = $color;
  }
  function getInfo() {
    return "This beverage is $this->temperature and $this->color.";
  }
}

/* Test your constructor by instantiating an object with a temperature of "cold" and a color of “black“.

Print the result of calling getInfo on this object.*/
$var = new Beverage('cold', 'black');
echo $var->getInfo();