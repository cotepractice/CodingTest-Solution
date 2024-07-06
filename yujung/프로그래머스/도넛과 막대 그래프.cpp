#include <vector>
#include<map>
using namespace std;

int res[4];
map<int,pair<int,int>> dict;
vector<int> solution(vector<vector<int>> edges) {
    int central=0;
    int n=edges.size();
    for(int i=0; i<edges.size();i++){
        dict[edges[i][0]].first++;
        dict[edges[i][1]].second++;
    }
  
    
    for(auto d:dict){
        int key=d.first;
        pair<int,int> node=d.second;
       if(node.second==0&&node.first>=2)res[0]=key;
       if(node.second>0&&node.first==0)res[2]++;
       if(node.second>=2&&node.first>=2)res[3]++;
            
    }
    
   res[1]=dict[res[0]].first-res[3]-res[2];
    vector<int> answer({res[0],res[1],res[2],res[3]});
    return answer;
}