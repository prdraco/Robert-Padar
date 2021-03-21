using System;

namespace TrueOrFalse
{
  class Program
  {
		static void Main(string[] args)
    {
      // Do not edit these lines
      Console.WriteLine("Welcome to 'True or False?'\nPress Enter to begin:");
      string entry = Console.ReadLine();
      Tools.SetUpInputStream(entry);

      // Type your code below
      string[] questions = {"Green is the color of the sky?", "Gronland is the name of the South Pole continent", "Asia is bigger than North America", "Java is the most popular coding language"};
      bool[] answers = {false, false, true, false};
      bool[] responses = new bool[questions.Length];
      if(questions.Length != answers.Length) {
        Console.WriteLine("There is a problem with missing good answers!");    
      }
      int askingIndex = 0;
      foreach(string quests in questions) {
        string input;
        bool isBool;
        bool inputBool;
        Console.WriteLine(quests);
        input = Console.ReadLine();

        isBool = Boolean.TryParse(input, out inputBool);
        while(!isBool) {
          Console.WriteLine("Please respond with 'true' or 'false'");
          input = Console.ReadLine();
          isBool = Boolean.TryParse(input, out inputBool);
        }
        responses[askingIndex] = inputBool;
        askingIndex++;
      }
      int scoringIndex = 0;
      int score = 0;
      foreach(bool answer in answers) {
        bool response = responses[scoringIndex];
        Console.WriteLine($"{scoringIndex+1}. Input: {response} | Answer: {answer}");
        scoringIndex++;
        if(response == answer) {
          score++;
        }  
      }
      Console.WriteLine($"You got 4 out of {score} correct!");
    }
  }
}
