

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/*
 * Sample for how to read from a file
 */


class RandPoem1{

    public static void main(String args[]){

    
    // Read a file
    try { 
        FileReader f = new FileReader("shakespeare.txt");
        BufferedReader reader = new BufferedReader(f);
        String line = null;

        int word = 0;
        int lline = 0;
        int stanza = 0;
        
        while ((line = reader.readLine()) != null &&
           (word < 7 && lline < 4 && stanza < 4)) {

        String[] words = line.trim().split(" ");
        String wordToUse = getWordToUse(words);
        if(wordToUse == null)
            continue;
        

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
    static String getWordToUse(String[] w){
    if(w.length < 5)
        return null;

    if(Math.random() < 0.9)
        return null;

    int l = w.length;
    int index = (int)Math.floor(Math.random() * l);
    return w[index];
    }
}