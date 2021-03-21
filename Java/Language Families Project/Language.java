/* In Language.java, create a Language class with a main() method and the following fields:

name: a protected string.
numSpeakers: a protected integer.
regionsSpoken: a protected string.
wordOrder: a protected string.*/
class Language {
  /* Above the main() method, give Language a constructor that sets each field to the values passed in.*/
  protected String name;
  protected int numSpeakers;
  protected String regionsSpoken;
  protected String wordOrder;

  Language(String langName, int speakers, String regions, String wdOrder) {
    this.name = langName;
    this.numSpeakers = speakers;
    this.regionsSpoken = regions;
    this.wordOrder = wdOrder;
  }
  /* Create a public method for Language called getInfo(). We’ll use this method to display all of its information (using its field values).

The method should not return anything.

We want to set up the information like this:

[name] is spoken by [numSpeakers] people mainly in [regionsSpoken].
The language follows the word order: [wordOrder].*/
  public void getInfo() {
    System.out.println(this.name+" is spoken by "+this.numSpeakers+ " people mainly in "+this.regionsSpoken+". The language follows the word order: "+this.wordOrder+".");
  }

  public static void main(String[] arg) {
    /* Let’s test out the code so far!

In main(), instantiate a new Language of your choice.

Then call getInfo() on the Language variable.

Run your code in the terminal to see if the information gets printed. If nothing displays, try compiling your code first.*/
    Language spanish = new Language("Spanish", 555000000, "Spain, Latin America, and Equatorial Guinea", "subject-verb-object");
    spanish.getInfo();
    /* Time to test out the tweaks you made to the Mayan class…

Tab back over to Language.java.

In main(), instantiate a new Mayan language of your choice (you can find one here).

Then call getInfo() on the language variable.

Run your code in the terminal to see if the information gets printed. If nothing displays, try compiling your code first.*/
    Language mayan = new Mayan();
    mayan.getInfo();
    /* Test out the SinoTibetan class by instantiating two new Sino-Tibetan language objects of your choosing:

One Chinese (e.g., “Mandarin Chinese”)
One non-Chinese (e.g., Burmese)
Then call getInfo() on each language variable.

Run your code in the terminal to see if the information gets printed. If nothing displays, try compiling your code first.*/
    Language mandarinChinese = new SinoTibetan("mandarinChinese");
    mandarinChinese.getInfo();
    Language Burmese = new SinoTibetan("Burmese");
    Burmese.getInfo();
  }
}