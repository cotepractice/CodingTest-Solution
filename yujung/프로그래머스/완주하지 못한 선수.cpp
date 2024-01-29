#include <string>
#include <vector>
#include<map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map<string,int> map;
    for(auto inter1: completion){
        map[inter1]+=1;
    }
    for(auto inter2: participant){
        map[inter2]-=1;
        if(map[inter2]<0){
            return inter2;
        }
    }
}