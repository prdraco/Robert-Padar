using System;

namespace GettingInput
{
  class Program
  {
    static void Main()
    {
      //This is the example in c# to demonstrate the user input command
      Console.WriteLine("How old are you?");
      string input = Console.ReadLine();
      Console.WriteLine($"You are {input} years old!");
    }
  }
}
