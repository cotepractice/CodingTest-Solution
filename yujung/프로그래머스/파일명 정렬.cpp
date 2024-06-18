#include <string>
#include <vector>
#include<algorithm>
using namespace std;

struct file{
    int idx;
    string head;
    int number;
};

bool cmp(file & a,file & b){
    if(a.head==b.head){
        if(a.number==b.number){
            return a.idx<b.idx;
        }else{
            return a.number<b.number;
        }
    }else{
        return a.head<b.head;
    }
}
vector<string> solution(vector<string> files) {
    vector<string> answer;
       vector<file> v;
    for(int i=0; i<files.size();i++){

        vector<int> tmp;
        
        for(int j=0; j<files[i].size();j++){
            if(isdigit(files[i][j])){
                tmp.push_back(j);
            }
            
          
            
        }
        file fi;
     
        fi.idx=i;
   
        string head;
        for(int t=0;t<tmp[0];t++){
            head+=tolower(files[i][t]);
        }
             fi.head=head;
        fi.number=stoi(files[i].substr(tmp[0],tmp.size()));
  

            v.push_back(fi);
   
        
          
        
    }
    sort(v.begin(),v.end(),cmp);
    
    for(int i=0; i<v.size();i++){
        answer.push_back(files[v[i].idx]);
    }
    
    return answer;
}