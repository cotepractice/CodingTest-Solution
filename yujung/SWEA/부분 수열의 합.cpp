#include <iostream>
#include <vector>
using namespace std;

int T, N, K, count;
vector<int> number;

void dfs(int i, int result) {
    if (result == K) {
        count++;
        return;
    }
    if (i == N) {
        return;
    }
    dfs(i + 1, result + number[i]);
    dfs(i + 1, result);
}

int main() {
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> N >> K;
        number.resize(N);
        for (int i = 0; i < N; i++) {
            cin >> number[i];
        }
        count = 0;
        dfs(0, 0);
        cout << "#" << test_case << " " << count << endl;
    }
    return 0;
}
