/* Now let’s model a language family.

Tab over to Mayan.java and create an empty Mayan class that inherits from Language.*/
class Mayan extends Language {
  /* Mayan languages share several traits in common including:

regionsSpoken: "Central America"
wordOrder: "verb-object-subject"
Tweak the Mayan constructor so that it isn’t necessary to pass in these fields when instantiating a new Mayan language object.

Bear in mind that each language will still require its own name and numSpeakers.*/
  Mayan() {
    super("Ki'che'", 2330000, "Central America", "verb-object-subject");
  }
  /* Mayan languages have an interesting grammatical feature: ergativity.

Override the getInfo() method for Mayan so that if we called getInfo() on a Mayan language like Ki’che’, we’d get the following info:

Ki'che' is spoken by 2330000 people mainly in Central America.
The language follows the word order: verb-object-subject
Fun fact: Ki'che' is an ergative language.*/
  @Override
  public void getInfo() {
    System.out.println(this.name+" is spoken by "+this.numSpeakers+ " people mainly in "+this.regionsSpoken+". The language follows the word order: "+this.wordOrder+". Fun fact: Ki'che' is an ergative language.");
  }
}