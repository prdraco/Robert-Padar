<?php
class Beverage {
  public $temperature, $color, $opacity;
}
// We’ve included the Beverage class. Create an instance of this class and assign it to the variable $tea.
$tea = new Beverage();
// Set the temperature of the object to "hot".
$tea->temperature = 'hot';
// Print the value of the temperature property of $tea.
echo $tea->temperature;