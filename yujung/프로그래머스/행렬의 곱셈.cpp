#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
        int n=arr1.size();
    int l=arr2[0].size();
    int m=arr2.size();
    vector<vector<int>> answer;
   

    for(int i=0; i<n;i++){
        vector<int> v;
        
        for(int j=0; j<l;j++){
            int sum=0;
            for(int k=0; k<m; k++){
                sum+=arr1[i][k]*arr2[k][j];
            }
            v.push_back(sum);
        }
        answer.push_back(v);
    }

    return answer;
}