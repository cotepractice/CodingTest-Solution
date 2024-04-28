#include <iostream>
#include <string>

using namespace std;

// 문자열을 주어진 횟수만큼 이어붙이는 함수
string repeatString(const string& str, int times) {
    string result;
    for (int i = 0; i < times; ++i) {
        result += str;
    }
    return result;
}

int main() {
    int T;
    cin >> T;

    for (int tc = 0; tc < T; tc++) {
        string S, T;
        cin >> S >> T;
        
        int s_len = S.size();
        int t_len = T.size();

        // 문자열 S를 T의 길이만큼 반복한 결과와 문자열 T를 S의 길이만큼 반복한 결과가 같으면 조건을 만족
        if (repeatString(S, t_len) == repeatString(T, s_len)) {
            cout << "#" << tc + 1 << " yes" << endl;
        } else {
            cout << "#" << tc + 1 << " no" << endl;
        }
    }

    return 0;
}
