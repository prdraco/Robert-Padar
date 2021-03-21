using System;

namespace ArchitectArithmetic
{
  class Program
  {
    public static void Main(string[] args)
    {
      double rect = Rectangle(1500, 2000);
      double circ = Circle(375) / 2;
      double tri = Triangle(750, 500);
      double teotihuacan = rect + circ + tri;
      double costs = teotihuacan * 180;
      costs = Math.Round(costs);

      double TajMahal = Rectangle(90.5, 90.5) - (4 * Triangle(24,24));
      double costs2 = TajMahal * 180;
      costs2 = Math.Round(costs2);

      double AlMasjidalharam = Rectangle(106, 180) + (Rectangle(284, 264) - Triangle(84, 264));
      double costs3 = AlMasjidalharam * 180;
      costs3 = Math.Round(costs3);

      Console.WriteLine("What monument would you like to work with? \nTaj Mahal in Agra, India write 'India' or \nAl-Masjid al-haram (Great Mosque) in Mecca, write 'Mecca' or \nTeotihuacan in Mexico City, Mexico write 'Mexico' ");
      string answer = Console.ReadLine();
      if(answer == "India") {
        Console.WriteLine($"The plan for that monument costs {costs2} pesos!");
      } else if(answer == "Mecca") {
        Console.WriteLine($"The plan for that monument costs {costs3} pesos!");
      } else if(answer == "Mexico") {
        Console.WriteLine($"The plan for that monument costs {costs} pesos!");
      } else {
        Console.WriteLine("Sorry incorrect choice!");
      }
    }
    static double Rectangle(double length, double width) {
      double area = length * width;
      return area;
    }
    static double Circle(double radius) {
      double area = Math.PI * (radius * radius);
      return area;
    }
    static double Triangle(double bottom, double height) {
      double area = 0.5 * bottom * height;
      return area;
    }
  }
}
