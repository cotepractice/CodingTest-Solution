package PROGRAMMERS.완주하지_못한_선수;

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> info = new HashMap<>();
        for (String person : participant){
            int n = info.getOrDefault(person, 0);
            info.put(person, n+1);
        }

        for (String person : completion){
            int n = info.get(person);
            if (n-1 == 0){
                info.remove(person);
            } else{
                info.put(person, n-1);
            }
        }
        for (String person : info.keySet()){
            answer = person;
        }
        return answer;
    }
}