
/*
 * Challenge 1 problems.
 *
 * Fill in the sections marked ... to answer the questions given.
 */

class Challenge1{

    public static void main(String[] args){
    
    // Problem 1
    // What is the sum of the numbers from 1 to 10?
    int sum = 0;
    int counter = 1;
    while(counter<=10) {
		sum += counter;
		counter++;
    }
    System.out.println("The sum is " + sum + ", which should be 55");
    
    // Problem 2
    // What is the sum of the numbers from 1 to 20?
    int sum = 0;
    for(int i = 1; i <= 20; i++) {
		sum += i;
		
    }
    System.out.println("The sum is " + sum + ", which should be 210");
    
    // Problem 3
    // Print out the even numbers from 2 to 30
    for(int i = 2; i <= 30; i+=2){
        System.out.println(i);
    }
    
    // Problem 4
    // Print out the odd numbers from 1 to 17
    int counter = 1;
    while(counter<=15) {
        counter+=2;
        System.out.println(counter);
    }
    }
}