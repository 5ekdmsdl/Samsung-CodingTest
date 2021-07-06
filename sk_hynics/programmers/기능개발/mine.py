#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> day;
    
    for(int i = 0 ; i < progresses.size(); i++){
        double required_day = (100 - progresses[i]) / static_cast<double>(speeds[i]);
        double gap = required_day - (static_cast<int>(required_day));
        // cout << required_day<< static_cast<int>(required_day)<<gap << endl;
        if(gap){
            required_day += 1;
        }
        day.push_back(static_cast<int>(required_day));
    }
    for(auto d: day){
        cout << d << endl;
    }
    // 7 3 9
    int now = day[0];
    int cnt = 0;
    for(auto d : day){
        
        if(d <= now){
            cnt += 1;
        }
        else{
            answer.push_back(cnt);
            cnt = 1;
            now = d;
        }
        cout << d << now << cnt << endl;
    }
    answer.push_back(cnt);
    return answer;
}
