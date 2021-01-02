/**
* Class to write doubledactyls
*/
class DoubleDactyl extends MeteredPoem{
	
	/**
	*Here we implement the generatePoem() method that was
	*declared in our superclass Poem
	*/
	String generatePoem(){
		poem =
		writeLineWithMeter("'--'--") + "\n" +
		writeLineWithMeter("'--'--") + "\n" +
		writeLineWithMeter("'--'--") + "\n" +
		writeLineWithMeter("'--") + "\n" + "\n" +
		writeLineWithMeter("'--'--") + "\n" +
		writeLineWithMeter("'--'--") + "\n" +
		writeLineWithMeter("'--'--") + "\n" +
		writeLineWithMeter("'--");
	}
}