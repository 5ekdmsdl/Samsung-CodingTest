#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    if(scoville.size() == 0) return -1;
    priority_queue<int, vector<int>, greater<int>> q;
    
    for(auto s:scoville){
        q.push(s);
    }
    
    while(1){
        int sm1 = q.top();
        q.pop();
        if(sm1 >= K){
            return answer;
        }
        else if(q.size() == 0){
            return -1;
        }
        else{
            int sm2 = q.top();
            q.pop();
            int mixed = sm1 + sm2*2;
            q.push(mixed);
            answer += 1;
        }
    }
    
    return answer;
}
