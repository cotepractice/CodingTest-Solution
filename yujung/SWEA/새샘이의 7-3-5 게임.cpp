#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

//vector보다 array가 빠름
using namespace std;

int main() {
    // 입력 스트림 설정
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        vector<int> arr(7);
        for (int i = 0; i < 7; ++i) {
            cin >> arr[i];
        }

        set<int> hs;

        for (int i = 0; i < arr.size() - 2; ++i) {
            for (int j = i + 1; j < arr.size() - 1; ++j) {
                for (int k = j + 1; k < arr.size(); ++k) {
                    hs.insert(arr[i] + arr[j] + arr[k]);
                }
            }
        }

        vector<int> list(hs.begin(), hs.end());
        sort(list.begin(), list.end(),greater<int>());
        cout << '#' << tc << ' ' << list[4] << '\n';
    }

    return 0;
}
