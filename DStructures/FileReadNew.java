import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class FileReadNew {
	private static Object String;

	public static void main(String args[]) {

		// read a file
		try {
			FileReader f = new FileReader("shakespeare.txt");
			BufferedReader reader = new BufferedReader(f);

			int word = 0;
			int lline = 0;
			int stanza = 0;

			String r = "r";

			while (word < 7 && lline < 4 && stanza < 4) {
				String wordToUse = getWordToUse(reader, r);

				if (word < 7) {
					System.out.print(wordToUse + " ");
					word++;
				}
				if (word == 7) {
					System.out.print("\n");
					word = 0;
					lline++;
				}
				if (lline == 4) {
					System.out.println("\n");
					lline = 0;
					stanza++;
				}
			}
			reader.close();
		} catch (IOException x) {
			System.err.format("IOException: %s\n", x);
		}
	} // end of main

	/**
	 * make a thing that returns all words that end in r where r equals
	 * something like "ate"
	 * 
	 * for each string in my array I need you to check if it ends with r if it
	 * ends in r change the flag to true
	 */
	static String getWordToUse(BufferedReader reader, String r)
			throws IOException {
		boolean foundWord = false;
		String[] words = null;
		int index = 0;

		while (foundWord == false) {
			String line = reader.readLine();
			words = line.trim().split(" ");
			for (String word : words) {
				String last = word.substring(word.length() - r.length());
				if (last.equals(r)) {
					return word;
				} else {
					continue;
				}
			}
		}
		int l = words.length;
		index = (int) l;
		foundWord = true;
		{
			return words[index];
		}
	}

}