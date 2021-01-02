public class Thing{
	int t;
	string s;
	
}

//

public class ThingTester{
	public static void main(String[] args){
		Thing thing1 = new Thing();
		thing1.t = 17
		thing1.s = "Love";
		
		Thing thing2 = new Thing();
		thing2.t = 20;
		thing2.s = "Hate";
		
		print(thing1);
		print(thing2);
		
		
	}
	
	static void print(thing thg){
		System.out.println("Thing:" + thg.t + "," + thg.s);
}