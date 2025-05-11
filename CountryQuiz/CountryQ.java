// Java (CIT 215): Lab 8
// Program: Country Gui w/ Quiz
// Due Date: 04-01-2025
// Author: sim

public class CountryQ {
    private final String name;
    private final String capital;
    private final String language;
    private final String imagefile;

    public CountryQ(String name, String capital, String language, String imagefile) {
        this.name = name;
        this.capital = capital;
        this.language = language;
        this.imagefile = imagefile;
    }

    public String getName() { return name; }
    public String getCapital() { return capital; }
    public String getLanguage() { return language; }
    public String getImagefile() { return imagefile; }

    @Override
    public String toString() {
        return String.format("This is %s! \n💡Fun Fact💡\nThe capital is %s and its primary language is %s!",
                name, capital, language);
    }
}
