
import java.io.*;
public class RandomAccessFileExample {
 public static void main(String[] args) {
 try {
 // Create a RandomAccessFile object with read-write mode
 RandomAccessFile file = new RandomAccessFile("data.txt", "rw");
 // Write data to the file
 String data1 = "Hello";
 String data2 = "World";
 file.writeUTF(data1);
 file.writeUTF(data2);
 // Move the file pointer to the beginning of the file
 file.seek(0);
 // Read data from the file
 String readData1 = file.readUTF();
 String readData2 = file.readUTF();
 System.out.println("Data read from file:");
 System.out.println(readData1);
 System.out.println(readData2);
 // Move the file pointer to the ending of the file
 file.seek(file.length());
 // Append new data to the file
 String newData = "Java!";
 file.writeUTF(newData);
 // Move the file pointer to the beginning of the file
 file.seek(0);
 // Read data from the file again after appending
 readData1 = file.readUTF();
 readData2 = file.readUTF();
 String readData3 = file.readUTF();
   System.out.println("Data read from file after appending:");

 System.out.println(readData1);

 System.out.println(readData2);

 System.out.println(readData3);
 // Close the file

 file.close();

 } catch (IOException e) {

 System.out.println("An error occurred: " + e.getMessage());

 e.printStackTrace();

 }

 }

}
