using System;

namespace LearnInheritance
{
  /*Inheritance is a way to avoid duplication across multiple classes.
In inheritance, one class inherits the members of another class.
The class that inherits is called a subclass or derived class. The other class is called a superclass or base class.
We can access a superclass’ members using base. This is very useful when calling the superclass’ constructor.
We can restrict access to a superclass and its subclasses using protected.
We can override a superclass member using virtual and override.
We can make a member in a superclass without defining its implementation using abstract. This is useful if every subclass’ implementation will be different.
  */
  class Program
  {
    static void Main(string[] args)
    {
      Sedan s = new Sedan(60);
      // Call SpeedUp() here
      Console.WriteLine(s.Describe());
      
      Truck t = new Truck(45, 500);
      // Call SpeedUp() here
      Console.WriteLine(t.Describe());
      
      Bicycle b = new Bicycle(10);
      // Call SpeedUp() here
      Console.WriteLine(b.Describe());
    }
  }
}