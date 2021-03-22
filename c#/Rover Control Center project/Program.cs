using System;

namespace RoverControlCenter
{
  class Program
  {
    static void Main(string[] args)
    {
      MoonRover lunokhod = new MoonRover("Lunokhod 1", 1970);
      MoonRover apollo = new MoonRover("Apollo 15", 1971);
      MarsRover sojourner = new MarsRover("Sojourner", 1997);
      Satellite sputnik = new Satellite("Sputnik", 1957); 
  		Rover[] rov = new Rover[]
      {
        lunokhod, apollo, sojourner
      };
      DirectAll(rov);
      Object[] all = new Object[]
      {
        lunokhod, apollo, sojourner, sputnik
      };
      foreach(Object al in all) {
        Console.WriteLine($"Tracking a {al.GetType()}…");
      }
      IDirectable[] dict = new IDirectable[]
      {
        lunokhod, apollo, sojourner, sputnik
      };
    }
    public static void DirectAll(IDirectable[] arg) {
      foreach(Rover ar in arg) {
        Console.WriteLine(ar.GetInfo());
        Console.WriteLine(ar.Explore());
        Console.WriteLine(ar.Collect());
      }
    }
  }
}
