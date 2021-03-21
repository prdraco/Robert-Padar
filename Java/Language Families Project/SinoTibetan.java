/* The Sino-Tibetan family has the second highest number of native speakers of any language family.

Tab over to SinoTibetan.java and build out an empty SinoTibetan class that inherits from Language.*/
class SinoTibetan extends Language {
  /* Like the Mayan language family, Sino-Tibetan languages share several traits in common. In this case:

regionsSpoken: "Asia"
wordOrder: "subject-object-verb"
Build a constructor for SinoTibetan that so that it isn’t necessary to pass in these fields when instantiating a new SinoTibetan language object.

Remember — each language will still require its own name and numSpeakers.*/
  SinoTibetan(String languageName) {
    super("SinoTibetan", 147000, "Asia", "subject-object-verb");
    /* In the constructor, below where you called super(), change the wordOrder to "subject-verb-object" if this.name contains "Chinese".*/
    if (languageName.contains("Chinese")) {
      this.wordOrder = "subject-verb-object";
    }    
  }
}