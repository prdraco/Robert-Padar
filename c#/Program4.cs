using System;

namespace MoneyMaker
{
  class MainClass
  {
    public static void Main(string[] args)
    {
      Console.WriteLine("Welcome to Money Maker!");
      
      Console.WriteLine("The amount to convert: ");
      string amount = Console.ReadLine();
      double amountAsDouble = Convert.ToDouble(amount);
      Console.WriteLine($"{amountAsDouble} cents is equal to...");

      int gold = 10;
      int bronze = 5;
      
      double goldCoins = Math.Floor(amountAsDouble / 10);
      Console.WriteLine($"{goldCoins} goldcoins");
      double centsLeft = amountAsDouble % 10;

      double silverCoins = Math.Floor(centsLeft / 5);
      Console.WriteLine($"{silverCoins} silvercoins");
      double bronzeCoins = centsLeft % 5;
      Console.WriteLine($"{bronzeCoins} bronzecoins");
    }
  }
}
