/*
 * Author: Teja Kavallappa
 * Date: August 31 2015
 * CountWords.java - Accepts a string and prints out the number
 * of words in the string
 * */
import java.util.Scanner;
import java.io.*;
public class CountWords{ 
    public static void main(String[] args){
        String fileName = "./../blns.txt";
        try{
            File textFile = new File(fileName);
            Scanner readFile = new Scanner(textFile);
            System.out.println("Reading in file "+ fileName);
            System.out.println("Number of words in file = " + countWords(readFile));

        }
        catch(FileNotFoundException e){
            System.out.println("File " + fileName + " not found.");
        }

    }
    private static int countWords(String sentence){
        if (sentence == null)   
            return 0;
        char ch;
        int numWords = 0;
        boolean endWord = false;
        for(int i = 0; i < sentence.length(); i++){
            ch = sentence.charAt(i);
            if(ch == ' ' && endWord == false){
                numWords++;
                endWord = true;
            }
            else if (ch != ' ' && endWord == true){
                endWord = false;
            }
        }
        numWords++;
        return numWords;
    }

    //Overloading
    private static int countWords(Scanner readFile){
        //Warning: Do not print out lines to terminal
        String line;
        int numWords = 0;
        while(readFile.hasNext()){
            line = readFile.nextLine();
            numWords += countWords(line);
        }
        return numWords; 
    }
}
