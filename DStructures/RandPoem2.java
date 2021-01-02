
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/*
 * Sample for how to read from a file
 */


class RandPoem2{

    public static void main(String args[]){

    
    // Read a file
    try { 
        FileReader f = new FileReader("shakespeare.txt");
        BufferedReader reader = new BufferedReader(f);
        String line = null;

        int word = 0;
        int lline = 0;
        int stanza = 0;
        
        while (word < 7 && lline < 4 && stanza < 4) {

        String wordToUse = getWordToUse(reader);

        if(word < 7){
            System.out.print(wordToUse + " ");
            word++;
        }

        if(word == 7){
            System.out.print("\n");
            word = 0;
            lline++;
        }

        if(lline == 4){
            System.out.print("\n");
            lline = 0;
            stanza++;
        }
            
        } // end of while loop
        reader.close();
    } catch (IOException x) {
        System.err.format("IOException: %s\n", x);
    }
    
    } // End of main


    
    /**
     * Produce one word from an array of words
     * return either:
     *    null if the line is not desirable (subjective...)
     *    the word from the array that youlike
     */
    static String getWordToUse(BufferedReader reader) throws IOException{
    boolean  foundWord = false;
    String[]   words = null;
    int             index = 0;
    
    while(foundWord == false){
        String line = reader.readLine();
        words = line.trim().split(" ");

        if(words.substring.(words.length - 1, words.length).equals(r)); // Move along if the line is short
        foundWord == true;

        int l = words.length;
        index = (int)Math.floor(Math.random() * l);
        foundWord = true;
    }
    return words[index];
    }
}