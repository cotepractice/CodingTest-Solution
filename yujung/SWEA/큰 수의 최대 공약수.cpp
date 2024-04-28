#include <iostream>
#include <string>
#include <vector>
using namespace std;
//unsigned long long으로 64비트 이상 다르기 힘듬.->문자열로 해결
int main() {
    int T;
    cin >> T;

    vector<string> answer(T);

    for (int i = 0; i < T; ++i) {
        string A, B;
        cin >> A >> B;
        string num;
        if (A == B) {
            num = A;
        } else {
            num = "1";
        }

        cout << "#" << i + 1 << " " << num << "\n";
    }

    return 0;
}