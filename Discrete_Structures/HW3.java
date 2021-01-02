

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/*
 * Sample for how to read from a file
 */


class Homework3{

    public static void main(String args[]){


        // Read a file
        try { 
            // Book reader
            FileReader f = new FileReader("C:\\Users\\Julian\\Documents\\CompSci\\DStructures\\JaneAusten.txt");         
            BufferedReader reader = new BufferedReader(f);
            // Pronunciation reader
            FileReader g = new FileReader("C:\\Users\\Julian\\Documents\\CompSci\\DStructures\\cmupron.txt");            
            BufferedReader rhymingReader = new BufferedReader(g);
            rhymingReader.mark(3139728); // Set the reset point to the start of file
            String line = null;

            int word = 0;
            int lline = 0;
            int stanza = 0;

            while (word < 7 && lline < 4 && stanza < 4) {

                String wordToUse = getWordToUse(reader);
                String rhymingWord = getRhymingWord(reader, rhymingReader, "EY0 T");

                if(word < 6){
					
                    System.out.print(wordToUse + " ");
                    word++;
                }

                if(word == 6){
                    System.out.print(getRhymingWord(reader, rhymingReader, "EH1 R"));
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
     * Finds words that end with the phonemes given in String r
     * @param reader            The buffered reader wrapped around the literature we get words from
     * @param rhymingReader        The buffered reader wrapped around cmupron.txt
     * @param r                    The string containing the phonemes we wish to rhyme with
     * @return                    A word having those phonemes at the end.
     * @throws IOException
     */
    static String getRhymingWord(BufferedReader reader, BufferedReader rhymingReader, String r) throws IOException{
        String[]   words = null;
        String line;
        
        while((line = reader.readLine()) != null){
            line = line.replaceAll("[^a-zA-Z ]", "");
            words = line.trim().toUpperCase().split(" ");

            if(words.length < 5) // Move along if the line is short
                continue;

            for(String w : words){
				if(lookup(rhymingReader, w).endsWith(r)){
				 return w;
				 
				}

 
                // Put code here that says:
                // "If w ends with the phonemes in r, return it"
                // This line below looks up string w in the dictionary. Good line to make use of.
               
            }
        }
        
        // If we get here, then we didn't find a matching word
        return "Couldn't find the desired rhyme: " + r;
    }
    
    /**
     * Looks up a word w in the cmupron file, and returns the line containing that word 
     * @param rr BufferedReader object that wraps the cmupron file
     * @param w  The English word we wish to find in that file
     * @return   The line in the file that has the pronunciation for word w
     * @throws IOException
     */
    static String lookup(BufferedReader rr, String w) throws IOException{
        String[]   words = null;
        String line;
        rr.reset();
        while((line = rr.readLine()) != null){
            // This will loop through all the lines in the pronunciation file
            // You should put code here to find the word w in the dictionary
            // Probably best to return all of "line"
            // And then have the getRhymingWord method check the end
            if(line.startsWith(w))
                return line;
        }
        
        // If we get here, then we didn't find a matching word
        return "Not in dictionary: " + w;
    }
}