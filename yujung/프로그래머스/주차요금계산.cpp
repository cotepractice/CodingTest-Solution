#include<iostream>
#include<map>
#include<vector>
#include<sstream>
using namespace std;
map<string, int> mapset;

int time_diff(string in, string out) {
	int h = stoi(in.substr(0, 2));
	int m = stoi(in.substr(3, 2));
	int h2 = stoi(out.substr(0, 2));
	int m2 = stoi(out.substr(3, 2));
	int diff = (h2 - h) * 60 + (m2 - m);
}

vector<int> solution(vector<int> fees, vector<string> records) {
	vector<int> answer;
	map<string, vector<string>> m;
	stringstream s;
	for (auto record : records) {
		s.str(record);
		string time, number, inout; s >> time >> number >> inout; //sstream은 \n이나 ' '를 제외하고 불러옴 
		m[number].push_back(time);
		s.clear(); //버터 비워야 다음 값들 불러올 수 있음
	}
	for (auto a : m) {
		if (a.second.size() & 1) // it.second.size() 키 값의 사이즈가 홀수 인지 아닌지 검사 
			a.second.push_back("23:59");//"23:59" 추가

		vector<string> times = a.second;
		int total = 0;
		for (int i = 0; i < times.size() - 1; i += 2) {
			total += time_diff(times[i], times[i + 1]); //시간 총 합산
		}

		int price = fees[1];
		if (total > fees[0]) {
			price += ceil((total - fees[0]) / (double)fees[2]) * fees[3]; //주차 요금 계산
		}

		answer.push_back(price);
	}

	return answer;
}

