<?php
namespace Codecademy;

echo "Hello, there. What's your first name?\n";
$name = readline(">>");
if (strlen($name) >= 8) {
  echo "Hi, ". $name . " That's a long name.";
} elseif (strlen($name) >= 4) {
  echo "Hi, " . $name;
} else {
  echo "Hi, " . $name . " That's a short name.";
}