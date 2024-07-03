#include <string>
#include <vector>
#include<set>
using namespace std;

bool find_same(set<int> & a, set<int> & b,int n){
    for(auto num: a){
        int find_v=n-num;
        if(b.find(find_v)!=b.end()){
            a.erase(num);
            b.erase(find_v);
            return true;
        }
    }
    return false;
}

int solution(int coin, vector<int> cards) {
    int answer = 1;
    set<int> have;
    set<int> tmp;
    int start=cards.size()/3;
    int n=cards.size()+1;
    
    for(int i=0; i<start;i++){
        have.insert(cards[i]);
    }
    for(int i=start; i<cards.size();i+=2){
        tmp.insert(cards[i]);
        tmp.insert(cards[i+1]);
        if(have.size()>=2&&find_same(have,have,n)){
            answer++;
        }else if(coin>=1&&have.size()>=1&&find_same(have,tmp,n)){
            answer++;
            coin--;
        }else if(coin>=2&&have.size()>=0&&find_same(tmp,tmp,n)){
            answer++;
            coin-=2;
        }else{
            break;
        }
    }
    return answer;
}