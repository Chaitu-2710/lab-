Encapsulation:
 The fields of the class are private and accessed through getter and setter methods.*/
class Person {
 // private fields
 private String name;
 private int age;
 // constructor
 public Person(String name, int age) {
 this.name = name;
 this.age = age;
 }
 // getter and setter methods
 public String getName() {
 return name;
 }
 public void setName(String name) {
 this.name = name;
 }
 public int getAge() {
 return age;
 }
 public void setAge(int age) {
 this.age = age;
 }
 /* Abstraction:
 The displayInfo() method provides a simple interface to interact with the object.*/
 public void displayInfo() {
 System.out.println("Name: " + name);
 System.out.println("Age: " + age);
 }
}
/* Inheritance:
 Employee is a subclass of Person, inheriting its properties and methods.*/
class Employee extends Person {
 // private field
 private double salary;
 // constructor
 public Employee(String name, int age, double salary) {
 super(name, age);
 this.salary = salary;
 }
 // getter and setter methods
 public double getSalary() {
 return salary;
 }
 public void setSalary(double salary) {
 this.salary = salary;
 }
 /* Polymorphism:
 Overriding the displayInfo() method to provide a specific implementation for Employee.*/
 @Override
 public void displayInfo() {
 super.displayInfo();
 System.out.println("Salary: " + salary);
 }
}
public class OopPrinciplesDemo {
 public static void main(String[] args) {
 // Demonstrating encapsulation and abstraction
 Person person = new Person("Madhu", 30);
 System.out.println("Person Info:");
 person.displayInfo();
 System.out.println("====================");
 // Demonstrating inheritance and polymorphism
 Employee employee = new Employee("Naveen", 26, 50000);
 System.out.println("Employee Info:");
 employee.displayInfo();
 }
}
