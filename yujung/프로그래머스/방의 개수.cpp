#include <string>
#include <vector>
#include <map> 
using namespace std; 
int dx[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dy[] = { 0, 1, 1, 1, 0, -1, -1, -1 }; 


int solution(vector<int> arrows) {
    int answer = 0;
    map<pair<int,int>,bool> node_visit;
    map<pair<pair<int,int>,pair<int,int>>,bool> edge_visit;
    int x=0;
    int y=0;
    node_visit[{0,0}]=true;
    for(int i=0; i<arrows.size();i++){
        int dir=arrows[i];
        for(int j=0; j<2;j++){
            int nx=x+dx[dir];
            int ny=y+dy[dir]; //nx와 ny가 있으면 
            
            if(node_visit[{nx,ny}]==true&&edge_visit[{{x,y},{nx,ny}}]==false){
                answer++;
            }
            
            node_visit[{nx,ny}]=true;
            edge_visit[{{x,y},{nx,ny}}]=true;
            edge_visit[{{nx,ny},{x,y}}]=true;
            x=nx;
            y=ny;
        }
    }
    return answer;
}