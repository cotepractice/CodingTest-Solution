#include<iostream>
#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int solution(vector<int> stones, int k) {
	int end = *max_element(stones.begin(), stones.end());
	int start = 1;
	while (start <= end) {
		int mid = (start + end) / 2;
		int max_v = 0;
		int v = 0;
		for (int i = 0; i <= stones.size(); i++) {
			if (i == stones.size()) {
				max_v = max(max_v, v);
				continue;
			}
			if (stones[i] - mid < 1) v++;
			else {
				max_v = max(max_v,v);
				v = 0;
			}
		}
		if (max_v >= k) end = mid - 1;
		else start = mid + 1;
	}
	return start;
}