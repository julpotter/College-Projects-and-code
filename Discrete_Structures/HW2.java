// Framework for HW 2

public class HW2{
    // Define fields here
    static String firstname;
    static String middleInitial;
    static String lastname;
    static String age;

    public static void main(String[] args){
    // Give values to fields here
    firstname = "Julian";
    middleInitial = "S";
    lastname = "Potter";
    age = "20";

    System.out.println(firstname + " " + middleInitial + ". " +
               lastname + " is " + age + " years old");


    System.out.println("The first two characters of the last name are " + lastname.substring(0,2));

	
    System.out.println("The last two characters of the last name are " 
	+ lastname.substring((lastname.length() - 2), lastname.length()));

    int result = Integer.parseInt(age);
	
    System.out.println("Next year, that person's age will be " + (result + 1));

    }
}