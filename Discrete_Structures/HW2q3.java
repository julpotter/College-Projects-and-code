
public class HW2q3{
    public static void main(String[] args)//Compile error; capitalized S
	{
      double a = 5.0;
      double b = 12.0;
      double c = 0.0; //Compile error; int instead of double
      System.out.println("I have a right-triangular garden.");
      System.out.println("The west wall has length " + a + " yards"); //Compile error; missing ;
      System.out.println("The south wall has length " + b + " yards");
      c = Math.sqrt(a*a + b*b); //Runtime error; bad math
      System.out.println("The northeast wall will have length " + c + " yards");
    }
}