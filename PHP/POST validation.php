<?php
/* Define checkWord() here:
In the following tasks, you’ll be providing your validation logic within a function that you’ll 
invoke multiple times within the HTML.

In the PHP section of your code (above the HTML), write a function checkWord(). This function will be 
used to generate an error if the user submitted a word that does not start with the correct letter.

Your function should have two parameters:

A string representing the user’s input.
A string with the letter to which the input is supposed to correspond.
If the form has been submitted ($_SERVER["REQUEST_METHOD"] === "POST") and the first letter in the 
input is NOT the correct letter, your function should return the following string: "* This word must 
start with the letter [current letter]!" with [current letter] replaced by the letter currently being tested. 
Otherwise, your function should return an empty string.

checkWord("apple", "b"); // Returns: "* This word must start with the letter b!"
Note that "A" and "a" are not considered the same value by PHP by default. You can choose whether your 
function accounts for this or not.
*/
function checkWord($str, $corr) {
  if($_SERVER["REQUEST_METHOD"] === "POST" && strtolower($str[0]) != $corr) {
    return "* This word must start with the letter ${corr}!";
  } else {
    return "";
  }
}
  
?>
  
<h1>Time to Practice our ABCs</h1>
<form method="post" action="">
    Enter a word that starts with the letter "a":
    <br>
    /* Assign the value attribute of each input tag to the value submitted by a user. For example, if 
    a user enters the word “apple” in the first input field, they should still see apple in that input 
    field once they submit their form. */
    <input type="text" name="a-word" id="a-word" value='<?= $_POST["a-word"];?>'>
    /* Add three <p> elements to the HTML <form>—one below each <input>. All three should have a class of "error".

The <p> below the "a-word" input should have an id of "a-error".
The <p> below the "b-word" input should have an id of "b-error".
The <p> below the "c-word" input should have an id of "c-error".
The inner HTML of each error <p> element should be assigned to the value returned when your checkWord() function 
is invoked with the corresponding element from the $_POST array and the appropriate letter. */
    <p id='a-error'><?= checkWord($_POST["a-word"], "a");?></p>
    <br>      
      
    <br>     
    Enter a word that starts with the letter "b":
    <br>
    <input type="text" id="b-word" name="b-word" value='<?= $_POST["b-word"];?>'>
    <p id='b-error'><?= checkWord($_POST["b-word"], "b");?></p>
    <br>      
      
    <br>
    Enter a word that starts with the letter "c":
    <br>
    <input type="text" id="c-word" name="c-word" value='<?= $_POST["c-word"];?>'>
    <p id='c-error'><?= checkWord($_POST["c-word"], "c");?></p>
    <br>      
      
    <br>
    <input type="submit" value="Submit Words">
</form>
<div>
    <h3>"a" is for: <?= $_POST["a-word"];?><h3>
    <h3>"b" is for: <?= $_POST["b-word"];?><h3>
    <h3>"c" is for: <?= $_POST["c-word"];?><h3>    
<div>  