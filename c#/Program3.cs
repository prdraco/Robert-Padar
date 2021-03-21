using System;

namespace NameGrab
{
  class Program
  {
    static void Main(string[] args)
    {
      // User Name
      string name = "Farhad Hesam Abbasi";
      /* .Substring() grabs part of a string using the specified 
      character position and continues until the end of the 
      string and returns a new string. 
      .IndexOf() is usually used first to get the specific character position.*/
      // Get first letter
      int stat = name.IndexOf("F");
      char firstLetter = name[stat];

      // Get last name
      int charPosition = name.IndexOf("Abbasi");
      string lastName = name.Substring(charPosition);

      // Print results
      Console.WriteLine(firstLetter + " " + lastName);

    }
  }
}
