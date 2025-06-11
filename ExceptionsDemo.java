import java.io.File;
import java.io.FileReader;
import java.io.FileNotFoundException;
// Custom Exception
class InvalidAgeException extends Exception {
 public InvalidAgeException(String message) {
 super(message);
 }
}
public class ExceptionsDemo {
 // Method to demonstrate custom exception
 public static void register(String name, int age) throws InvalidAgeException {
 if (age < 18) {
 throw new InvalidAgeException("User must be at least 18 years old.");
 } else {
 System.out.println("Registration successful for user: " + name);
 }
 }
 public static void main(String[] args) {
 //Handling Checked Exception
 try {
 File file = new File("myfile.txt");
 // This line can throw FileNotFoundException
 FileReader fr = new FileReader(file);
 } catch (FileNotFoundException e) {
 System.out.println("File not found: " + e.getMessage());
 }
 //Handling Unchecked Exception
 try {
 int[] arr = {1, 2, 3};
 // Accessing an out-of-bound index
 System.out.println(arr[6]);
 } catch (ArrayIndexOutOfBoundsException e) {
 System.out.println("Array index out of bounds: " + e.getMessage());
 }
 // Finally block to perform cleanup operations
 finally {
 System.out.println("Cleanup operations can be performed here.");
 }
 // Demonstrate custom exception handling
 System.out.println("Demonstrating Custom Exception:");
 try {
 // Invalid age for registration
 register("Madhu", 17);
 } catch (InvalidAgeException e) {
 System.out.println("Custom Exception Caught: " + e.getMessage());
 }
 }
}
