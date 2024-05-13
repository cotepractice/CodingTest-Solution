#include <string>
#include <vector>
#include<set>
using namespace std;



int solution(vector<int> elements) {
    int answer = 0;
    set<int> s;
    int idx=0;
    int n=elements.size();
     for(int i=0; i<n;i++){
         s.insert(elements[i]);
     }
    for(int i=2; i<=n;i++){
        elements.push_back(elements[idx]);
        //n
        for(int j=0; j<elements.size()-i+1;j++){
            int sum=0;
            for(int k=j;k<j+i;k++){
                sum+=elements[k];
            }
            s.insert(sum);
        }
        idx++;
    }
  
    answer=s.size();
    return answer;
}