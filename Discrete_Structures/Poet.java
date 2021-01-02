import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;

/**
 * Class of static methods and fields  useful for writing poems
 */
class Poet{

    /**
     * The pronunciations array will hold the cmupron.txt file
     */
    static String[] pronunciations = null; // initializing it to null

    /**
     * the wordList array will hold our Word objects. 
     * Then each word will know its own pronunciation
     */
    static Word[] wordList = null;         // our large array of Word objects

    /**
     * maps words to the Word objects that contain that word
     */
    static HashMap<String, Word> wordMap = null;

    /**
     * vocab holds the name of the file we'll get words from
     */
    private static String vocab = null;
    static BufferedReader vocabReader = null;



    /**
     * Produce one word from a file handed to the method
     * return either:
     *    null if the line is not desirable (subjective...)
     *    the word from the array that you like
     * The word is produced sort of randomly
     */
    static String getWord(BufferedReader reader){
	boolean  foundWord = false;
	String[]   words = null;
	int             index = 0;

	while(foundWord == false){

	    String line;
	    try{
		line = reader.readLine();
	    } catch(IOException e){
		e.printStackTrace();
		return null;
	    }
	    line = line.replaceAll(",", "");
	    words = line.trim().split(" ");

	    if(words.length < 5) // Move along if the line is short
		continue;

	    int l = words.length;
	    index = (int)Math.floor(Math.random() * l);
	    foundWord = true;
	}
	return words[index];
    }

    /**
     * Finds words that end with the phonemes given in r
     */
    static String getRhymingWord(String r){
	// We check to see if we've read and pre-processed the
	// cmupron.txt file. If not, we do it now.
	if(pronunciations == null)
	    buildPronunciations();

	// We check to see if we've opened the vocab file
	// If not, we do it now
	if(vocabReader == null)
	    openVocabReader();

	String[]   words = null;

	while(true){
	    String line = null;
	    try{
		line = vocabReader.readLine();
	    } catch(IOException e){
		e.printStackTrace();
		return null;
	    }
	    line = line.replaceAll("[^a-zA-Z ]", "");
	    words = line.trim().split(" ");

	    if(words.length < 5) // Move along if the line is short
		continue;

	    for(String w : words){
		String wupper = w.toUpperCase();

		// Binary search pronunciations array for wupper
		int lower = 0;
		int upper = pronunciations.length - 1;
		while(lower <= upper){
		    int guess = (lower + upper) / 2;
		    String x = pronunciations[guess];
		    if(x.startsWith(wupper + " ")){ // We've found wupper
			if(x.endsWith(r)){
			    return w;
			}
			break;
		    }

		    // check to see how wupper+" " compares to guess
		    if(pronunciations[guess].compareTo(wupper + " ") < 0) // guess < wupper
			lower = guess + 1;
		    else
			upper = guess - 1;
		}
		/*
		// Loop through the pronunciations file to find wupper
		// Check to see if it rhymes. If so, return it, if not, break.
		for(String x : pronunciations){
		if(x.startsWith(wupper + " ")){
		if(x.endsWith(r)){
		return w;
		}
		break; 
		}
		}*/



	    }
	}
    }

    static String getRW(String phonemes){
	ArrayList<String> rw = new ArrayList<String>();
	for(String w : wordMap.keySet()){
	    if(wordMap.get(w).endsWith(phonemes))
		return wordMap.get(w).word;
	}
	return "Nono";
    }

    static String writeLineWithMeter(String meter){
	return "";
    }

    /**
     * Builds the pronunciation array of Strings.
     * Operates by "side effects" 
     * Does not return a value, rather, just does the work and leaves 
     * the change behind.
     */
    static void buildPronunciations(){
	// Open up the cmupron.txt file for reading
	try{
	    FileReader g = null;
	    g = new FileReader("cmupron.txt");
	    BufferedReader rhymingReader = new BufferedReader(g);
	    String line = null;
	    pronunciations = new String[110906];

	    // Generate the pronunciations array
	    int index = 0;
	    while((line = rhymingReader.readLine()) != null){
		pronunciations[index] = line;
		index++;
	    }
	    rhymingReader.close();
	} catch(IOException e){
	    e.printStackTrace();
	}
    }


    static void newBuildPronunciations(){
	// Open up the cmupron.txt file for reading
	try{
	    FileReader g = null;
	    g = new FileReader("cmupron.txt");
	    BufferedReader rhymingReader = new BufferedReader(g);
	    String line = null;

	    // Read the cmpupron file
	    while((line = rhymingReader.readLine()) != null){
		String[] parts = line.trim().split(" ");
		if(!wordMap.containsKey(parts[0]))
		    continue;
		Word w = wordMap.get(parts[0]);
		ArrayList<String> phonemes = new ArrayList<String>();
		ArrayList<Integer> stresses = new ArrayList<Integer>();
		for(int i = 1; i < parts.length; i++){
		    String letters = parts[i].replaceAll("[0-9]", "");
		    if(letters.length() != 0)
			phonemes.add(letters);
		    String number  = parts[i].replaceAll("[^0-9]", "");
		    if(number.length() != 0)
			stresses.add(Integer.parseInt(number));
		}
		// Copy the phonemes ArrayList into a fixed-size array
		String[] p = new String[phonemes.size()];
		for(int i = 0; i < phonemes.size(); i++)
		    p[i] = phonemes.get(i);
		w.phonemes = p; // Set it in the Word object
				
				// Copy the stresses Array list into a fixed-size array 
		int[] s = new int[stresses.size()];
		for(int i = 0; i < stresses.size(); i++)
		    s[i] = stresses.get(i);
		w.meter = s; // Set it in the Word object
	    }
	    rhymingReader.close();
	} catch(IOException e){
	    e.printStackTrace();
	}
    }



    /**
     * Open the vocab reader
     */
    static void openVocabReader(){
	try{
	    FileReader f = new FileReader(vocab);
	    vocabReader = new BufferedReader(f);
	} catch(FileNotFoundException e){
	    e.printStackTrace();
	}
    }


    /**
     * Set the name of the file we should get our words from.
     * That is, the vocab filename
     */
    public static void setVocab(String filename){
	vocab = filename;
	buildDataStructuresForNewFile();
	newBuildPronunciations();
    }

    /**
     * Builds wordMap and fills the words with data from language-information files
     */
    private static void buildDataStructuresForNewFile(){
	// Read the vocab file, and build the initial wordMap
	openVocabReader();	               // Create the BufferedReader for our file
	wordMap = new HashMap<String, Word>(); // Initial, empty map

	try{
	    String line = null;
	    while((line = vocabReader.readLine()) != null){
		line = line.replaceAll("[^a-zA-Z ]", "");
		// words is an array of clean words (Strings) from the text
		String[] words = line.trim().split(" ");
		for(String w : words){
		    if(wordMap.containsKey(w))
			continue;
		    Word word = new Word();
		    word.word = w;
		    wordMap.put(w, word);
		}
	    }
	} catch(IOException e){
	    e.printStackTrace();
	}
	System.out.println("Found " + wordMap.size() + " words in " + vocab);	
    }

    /**
     * Reads the cmupron.txt file and generates a Word object for each entry
     */
    public static void makeWordList(){ //Delete
	// Open up the cmupron.txt file for reading
	try{
	    FileReader f = null;
	    f = new FileReader("cmupron.txt");
	    BufferedReader rhymingReader = new BufferedReader(f);
0	    wordList = new Word[110906];

	    // Generate the wordList array
	    int index = 0;
	    while((line = rhymingReader.readLine()) != null){
		Word w = new Word();
		String[] lineParts = line.split(" ");
		w.word = lineParts[0].toUpperCase();
		w.meter = getMeter(line); // XXX Your HW: Write getMeter. Stub is below
		// The line below is for seeing if your function works. Delete it after testing.
		//System.out.println(line + " --> " + (Arrays.toString(w.meter)));
		wordList[index] = w;
		index++;
	    }
	    rhymingReader.close();
	} catch(IOException e){
	    e.printStackTrace();
	}
    }


    /**
     * Creates an array of ints corresponding to the stresses in the given string.
     * For example: 
     * "BRASHERS  B R AE1 SH ER0 Z" --> [1, 0]
     * "SUPERMINICOMPUTER  S UW1 P ER0 M IH2 N IH0 K AH0 M P Y UW2 T ER0" --> [1, 0, 2, 0, 0, 2, 0]
     */
    static int[] getMeter(String cmuline){
		String meter = cmuline.replaceAll("[a-zA-Z ]", "");
		String[] meter2 = meter.split("");
		int[] meterInts = new int[meter2.length];
		
		for (int i = 0; i < meter2.length; i++){
			int m = Integer.parseInt(meter2[i]);
			meterInts[i] = m;
		}
			
		return meterInts;
    }

    /**
     * Read the mpos.txt file to get parts of speech for our words
     * Each line of this file looks like: abbreviate*t
     * word, then *, then the part of speech.
     */
    static void readPOSFile(){
	try { 
	    FileReader f = new FileReader("mpos.txt");
	    BufferedReader reader = new BufferedReader(f);
	    String line = null;
	    int linesRead = 0;
	    while ((line = reader.readLine()) != null) {
		linesRead++;
		if(linesRead % 10000 == 0)
		    System.out.print("" + (int)(linesRead * 100 / 232123) + "% ");	
		String[] parts = line.split("\\*");
		Word foundIt = searchWordList(parts[0].toUpperCase());
		if(foundIt == null)
		    continue;
		foundIt.partOfSpeech = parts[1];
	    }
	    System.out.println("");
	    reader.close();
	} catch (IOException x) {
	    System.err.format("IOException: %s\n", x);
	}
    }


    /** 
     * Search our wordList for a particular word
     * Return the Word for word w, or null if it's not in wordList
     */
    static Word searchWordList(String w){
	// Binary search pronunciations array for wupper
	int lower = 0;
	int upper = wordList.length - 1;
	while(lower <= upper){
	    int guess = (lower + upper) / 2;
	    if(wordList[guess].word.equals(w))
		return wordList[guess];

	    // check to see how wupper+" " compares to guess
	    if(wordList[guess].word.compareTo(w) < 0) // guess < wupper
		lower = guess + 1;
	    else
		upper = guess - 1;
	}

	// If we make it to here, then the word is not in our word list
	return null;
    }


}
