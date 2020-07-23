package Baekjoon.리스트;

import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class problem5397_keylogger {
    public static List<Character> keyList;
    public static List<String> wordList;
    public static int checkCondition(int currentIndex, char lineCharacter){
        switch (lineCharacter){
            case '<':
                return moveLeft(currentIndex);
            case '>':
                return moveRight(currentIndex);
            case '-':
                return checkDelete(currentIndex);
            default:
                keyList.add(currentIndex, lineCharacter);
                currentIndex++;
        }
        return currentIndex;
    }
    public static int moveLeft(int currentIndex){
        if(currentIndex > 0){
            currentIndex--;
        }
        return currentIndex;
    }
    public static int moveRight(int currnetIndex){
        if(currnetIndex < keyList.size()){
            currnetIndex++;
        }
        return currnetIndex;
    }
    public static int checkDelete(int currentIndex){
        if(currentIndex > 0 && currentIndex <= keyList.size()){
            keyList.remove(--currentIndex);
        }
        return currentIndex;
    }
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int number = Integer.parseInt(br.readLine());
        int index = 0;
        wordList = new LinkedList<>();
        for(int i = 0; i<number; i++){
            String line = br.readLine();
            index = 0;
            keyList = new LinkedList<>();
            int lineLength = line.length();
            for(int j = 0; j<lineLength; j++){
                index = checkCondition(index, line.charAt(j));
            }
            StringBuilder sb = new StringBuilder();
            for(Character each : keyList){
                sb.append(each);
            }
            wordList.add(sb.toString());
            keyList.clear();
        }
        for(String each : wordList){
            System.out.println(each);
        }
    }
}
