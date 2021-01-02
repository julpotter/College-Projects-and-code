

class DumbPoem extends MeteredPoem{

    @Override
    String generatePoem(){
    
    int word = 0;
    int lline = 0;
    int stanza = 0;

    Poet.setVocab("shakespeare.txt");
    poem = "";
        
    while (word < 7 && lline < 4 && stanza < 4) {

        String rhymingWord = Poet.getRhymingWord("IY0");
        //System.out.println(poem);

        if(word < 6){
        poem = poem + rhymingWord + " ";
        word++;
        }
        
        if(word == 6){
        poem = poem + rhymingWord + " ";
        word++;
        }

        if(word == 7){
        poem = poem + "\n";
        word = 0;
        lline++;
        }

        if(lline == 4){
        poem = poem + "\n";
        lline = 0;
        stanza++;
        }
            
    } // end of while loop
    return poem;
    }
}