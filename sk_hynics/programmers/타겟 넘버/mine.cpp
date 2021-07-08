#include <string>
#include <vector>
#include <iostream>
using namespace std;

int dfs(int cnt, int t, int pm, int result, const vector<int>* ns, vector<int> pms){
    if(cnt == ns->size()){
        // cout << result << endl;
        // for(auto p : pms){
        //     cout << p;
        // }
        // cout << endl;
        if(result == t) return 1;
        else return 0;
    }
    
    int n = (*ns)[cnt];
    if(pm == 0) result -= n;
    else result += n;
    
    pms.push_back(pm);
    
    int rtv = 0;
    rtv += dfs(cnt+1, t, 0, result, ns, pms);
    rtv += dfs(cnt+1, t, 1, result, ns, pms);
    
    return rtv;
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    answer += dfs(0,target,0,0, &numbers , {});
    // cout << "a" << answer << endl;
    answer += dfs(0,target,1,0, &numbers, {});
    
    return answer/2;
}
