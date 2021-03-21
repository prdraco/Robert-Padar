using System;

namespace StoryTime
{
  class Program
  {
    static void Main(string[] args)
    {
      // Declare the variables
      string beginning = "Once upon a time, ";
      string middle = "there was a little bunny, who lowes to play caught and hide game. ";
      string end = "When he finished the game end of the day, returned to home to sleep.";

      // Concatenate the string and the variables
      string story = beginning + middle + end;

      // Print the story to the console 
      Console.WriteLine(story);
    }
  }
}
