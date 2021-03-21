using System;

namespace BasicClasses
{
  class Forest
  {
    public string name;
    public string Name {
      get { return name; }
      set { name = value; }
    }
    public int trees;
    public int Trees {
      get { return trees; }
      set { trees = value; }
    }
    public int age;
    public string biome;
    public string Biome {
      get { return biome; }
      set {
        if(value == "Tropical") {
          biome = value;
        } else if(value == "Temperate") {
          biome = value;
        } else if(value == "Boreal") {
          biome = value;
        } else { biome = "Unknown"; }
      }
    }
  }
}