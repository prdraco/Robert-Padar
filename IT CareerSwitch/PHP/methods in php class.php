<?php
class Beverage {
  public $temperature, $color, $opacity;
  /* Add a getInfo method to our Beverage class. We’ll be using 
  this method to return some information about our objects.*/
  function getInfo() {
    /* The method should return this statement about the beverage, 
    with <temperature> and <color> replaced with the beverage’s temperature and color:
    "This beverage is <temperature> and <color>."*/
    return "This beverage is " . $this->temperature . " and "  . $this->color . ".";
  }
}

$soda = new Beverage();
$soda->color = "black";
$soda->temperature = "cold";
/* We’ve created an instance of Beverage and saved it in the variable $soda. 
We’ve also assigned some values to its properties.
After our code, print the result of calling getInfo on the object (and nothing else).*/
echo $soda->getInfo();