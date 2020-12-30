<?php
namespace Codecademy;
function airQuality($color) {
  switch ($color) {
    case "green":
      echo "good";
      break;
    case "yellow":
      echo "moderate";
      break;
    case "orange":
      echo "unhealthy for sensitive groups";
      break;
    case "red":
      echo "unhealthy";
      break;
    case "purple":
      echo "very unhealthy";
      break;
    case "maroon":
      echo "hazardous";
      break;
    default:
      echo "invalid color";
      break;
  }
}

echo airQuality('green'); echo "\n";
echo airQuality('red'); echo "\n";
echo airQuality('orange'); echo "\n";
echo airQuality(''); echo "\n";



